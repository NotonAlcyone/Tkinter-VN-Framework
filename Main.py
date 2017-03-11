from tkinter import *
import os

root = Tk()

##############################################
canvasSizeX = 1280 
canvasSizeY = 720 
canvasCenterX = canvasSizeX/2
canvasCenterY = canvasSizeY/2

speechBarPositionX = canvasCenterX
speechBarPositionY = 620

namePostionX = 192
namePostionY = 520
textPositionX = 70
textPositionY = 615

sceneNumber = 0

barPath = "Bar_Text.png"
imageFolder = "image/"

nameFont = "Helvetica 15"
textFont = "Helvetica 20"
uiFont = "Helvetica 10"

encounterSpace = 130

##############################################


imagePath = {}
scenes = list()
encounterDict = {}
branchDict = {}
parameterDict= {}

class Scene:

	def __init__(self,backgroundImagePath,speecher,speech):
		self.backgroundImagePath = backgroundImagePath
		self.speecher = speecher
		self.speech = speech
		self.character = []
		

	def addCharacter(self,imagePath,x,y):
		self.character.append(Character(imagePath,x,y))

class Character:

	def __init__(self,imagePath,x,y):
		self.imagePath = imagePath
		self.positionX = x
		self.positionY = y

class Encounter:

	def __init__(self,startScene):
		self.startScene = startScene
		self.selectList = []
		self.check = False

	def addSelect(self,select,parameterName,factor):
		self.selectList.append(SelectList(select,parameterName,factor))

class SelectList:

	def __init__(self,select,parameter,factor):
		self.select = select
		self.parameter = parameter
		if parameter not in parameterDict:
			parameterDict[parameter] = 0
		self.factor = factor

wordPress = False
Press = True #this is buttonPress check(sorry for pascal)
def keyPressed(event):
	global Press
	global wordPress
	if Press == True:
		if wordPress == False:
			global sceneNumber
			sceneNumber += 1
			wordPress = True
			checker()
		elif wordPress == True:
			wordCancel()

def wordType(str,counter):
	global Press
	global wordPress
	wordPress = True
	if counter <= len(str):
		global text
		global textInvoke
		text = canvas.create_text(textPositionX,textPositionY,text= str[:counter],anchor = W,font = textFont)
		textInvoke = canvas.after(100,lambda:wordType(str,counter+1))
		if counter < len(str):
			canvas.after(99,lambda:wordDelete())
	else:
		wordPress = False
def wordDelete():
	canvas.delete(text)
def wordCancel():
	global wordPress
	wordPress = False
	canvas.after_cancel(textInvoke)
	canvas.delete(text)
	canvas.create_text(textPositionX,textPositionY,text= scenes[sceneNumber].speech,anchor = W,font = textFont)

def call(parameter,factor):
	global sceneNumber
	global Press
	Press = True
	parameterDict[parameter] += factor
	encounterDict[sceneNumber].check = True
	sceneNumber += 1
	checker()

def imageLoader(path):

	if path in imagePath:
		return imagePath[path]
	else:
		imagePath[path] = PhotoImage(file= imageFolder+path)
		return imagePath[path]

def update():
	canvas.delete('all')
	global sceneNumber
	call = scenes[sceneNumber]
	canvas.create_image(canvasCenterX,canvasCenterY,image = imageLoader(call.backgroundImagePath))
	
	for i in range(0,len(call.character)):
		charCall = call.character[i]
		canvas.create_image(charCall.positionX,charCall.positionY,image = imageLoader(charCall.imagePath))
	if scenes[sceneNumber].speech != "":
		canvas.create_image(speechBarPositionX,speechBarPositionY,image=imageLoader(barPath))
	if scenes[sceneNumber].speecher != "":
		canvas.create_image(namePostionX,namePostionY,image=imageLoader("Bar_Name.png"))
		
	canvas.create_text(namePostionX,namePostionY,text = scenes[sceneNumber].speecher,font = nameFont)
	wordType(scenes[sceneNumber].speech,0)
	saveButton = Button(root,text = "Save",command = lambda: saver(),relief=FLAT,compound= CENTER,image =imageLoader("Button.png"),font = uiFont )
	saveButton_window = canvas.create_window(canvasSizeX - 100,50,window = saveButton)

def saver():
	global sceneNumber
	global parameterDict
	file = open("saver.txt",'w+')
	savelist=[str(sceneNumber)+"\n",str(parameterDict)]
	file.writelines(savelist)
	file.close()

def checker():
	global sceneNumber
	global Press
	global parameterDict
	if sceneNumber  == len(scenes):
		Press = False
	elif sceneNumber in  encounterDict:
		if encounterDict[sceneNumber].check == False:
			Press = False
			encounterShower()
		else:
			update()
	elif sceneNumber in branchDict:
		if parameterDict[branchDict[sceneNumber]["condition"]] >= branchDict[sceneNumber]["conditionNumber"]:
			sceneNumber = branchDict[sceneNumber]["destination"]
			update()
		else:
			update()

	else:
		update()

def branchMaker(scene,destination,condition,conditionNumber):
	branchDict[scene] = {"destination":destination,"condition":condition,"conditionNumber":conditionNumber}

def encounterShower():
	global sceneNumber

	encounterStart = (canvasSizeY - len(encounterDict[sceneNumber].selectList)*encounterSpace)/2
	for i in range(0,len(encounterDict[sceneNumber].selectList)):
		button = Button(root,text = encounterDict[sceneNumber].selectList[i].select,command = lambda i = i: call(encounterDict[sceneNumber].selectList[i].parameter,encounterDict[sceneNumber].selectList[i].factor),relief=FLAT,compound= CENTER,image =imageLoader("Bar_Select.png"),font = nameFont )
		button_window = canvas.create_window(canvasCenterX,encounterStart + i*encounterSpace,window = button)

#############################
def loader():
	global sceneNumber
	global parameterDict
	if os.path.isfile("saver.txt"):
		file = open("saver.txt",'r')
		data = file.readlines()		
		sceneNumber = int(data[0][:-1])
		parameterDict = eval(data[1])
		if sceneNumber in encounterDict:
			sceneNumber -= 1
		update()
		canvas.bind("<Button-1>",keyPressed)
	else:
		sceneNumber = 0
		update()
		canvas.bind("<Button-1>",keyPressed)
def newStart():
	global sceneNumber
	sceneNumber = 0
	update()
	canvas.bind("<Button-1>",keyPressed)

#############################

def mainScene(background):

	canvas.create_image(canvasCenterX,canvasCenterY,image = imageLoader(background))
	
	startButton = Button(root,anchor = W,text ="New Game",command = lambda:newStart(),relief=FLAT,compound= CENTER,image =imageLoader("Button.png"),font = uiFont )
	startButton_window = canvas.create_window(canvasSizeX - 100,canvasSizeY - 120,window = startButton)
	

	loadButton = Button(root,anchor = W, text = "Load Game",command = lambda:loader(),relief=FLAT,compound= CENTER,image =imageLoader("Button.png"),font = uiFont )
	loadButton_window = canvas.create_window(canvasSizeX - 100,canvasSizeY - 50,window = loadButton)

#############################	
canvas = Canvas(root, width=canvasSizeX, height=canvasSizeY)
canvas.pack()