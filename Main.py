from tkinter import *
import pygame
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

barPath = "Bar_Text.png"
buttonPath = "Button.png"
nameBarPath = "Bar_Name.png"
imageFolder = "image/"
voiceFolder = "voice/"

nameFont = "Helvetica 15"
textFont = "Helvetica 20"
uiFont = "Courier 10"

encounterSpace = 130

##############################################


imagePath = {}
scenes = list()
encounterDict = {}
branchDict = {}
parameterDict= {}
tmpBranchDict={}

class Scene:

	def __init__(self,backgroundImagePath,speecher,speech,voice = 0):
		self.backgroundImagePath = backgroundImagePath
		self.speecher = speecher
		self.speech = speech
		self.voice = voice
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

	def addSelect(self,select,parameterName,factor):
		self.selectList.append(SelectList(select,parameterName,factor))

class SelectList:

	def __init__(self,select,parameter,factor):
		self.select = select
		self.parameter = parameter
		if parameter not in parameterDict:
			parameterDict[parameter] = 0
		self.factor = factor

class Branch:

	def __init__(self,scene):
		self.scene = scene
		self.branchList = []

	def addBranch(self,destination,condition,conditionNumber):
		self.branchList.append(BranchList(destination,condition,conditionNumber))

class BranchList:
	def __init__(self,destination,condition,conditionNumber):
		self.destination = destination
		self.condition = condition
		self.conditionNumber = conditionNumber

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
			if scenes[sceneNumber].voice != 0:
				voice.stop()
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
	sceneNumber += 1
	checker()

def imageLoader(path):

	if path in imagePath:
		return imagePath[path]
	else:
		imagePath[path] = PhotoImage(file= imageFolder+path)
		return imagePath[path]

def update():
	print("출력했습니다")
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
		canvas.create_image(namePostionX,namePostionY,image=imageLoader(nameBarPath))
		
	canvas.create_text(namePostionX,namePostionY,text = scenes[sceneNumber].speecher,font = nameFont)
	wordType(scenes[sceneNumber].speech,0)
	global voice
	if scenes[sceneNumber].voice != 0:
		voice = pygame.mixer.Sound(voiceFolder+scenes[sceneNumber].voice)
		voice.play()
	saveButton = Button(root,text = "Save",command = lambda: saver(),relief=FLAT,compound= CENTER,image =imageLoader(buttonPath),font = uiFont )
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
	"""
	if sceneNumber in tmpBranchDict:
		print(tmpBranchDict[sceneNumber].branchList[1].condition)
		print(len(tmpBranchDict[sceneNumber].branchList))
		#for i in range(0,len(tmpBranchDict))
		print(parameterDict)
		for i in range(0,len(tmpBranchDict[sceneNumber].branchList)):
			#if tmpBranchDict[sceneNumber].branchList[i].condition
			print(tmpBranchDict[sceneNumber].branchList[i].condition)

			if parameterDict[tmpBranchDict[sceneNumber].branchList[i].condition] >= tmpBranchDict[sceneNumber].branchList[i].conditionNumber:
				sceneNumber = tmpBranchDict[sceneNumber].branchList[i].destination
	"""
	if sceneNumber == len(scenes):
		Press = False
	elif sceneNumber in  encounterDict:
		Press = False
		encounterShower()
		"""
		if encounterDict[sceneNumber].check == False:
			Press = False
			encounterShower()
		else:
			update()
			print("이거 나오긴함?")
		"""
		
	elif sceneNumber in tmpBranchDict:
		branchStat = False
		branch = tmpBranchDict[sceneNumber].branchList
		for i in range(0,len(branch)):
			if parameterDict[branch[i].condition] >= branch[i].conditionNumber:
				branchStat = True
				if sceneNumber != branch[i].destination:
					sceneNumber = branch[i].destination
					if sceneNumber in encounterDict: #만약 이동한씬이 인카운터 씬아라면, 바로 그전으로 이동시킴
						sceneNumber -= 1
					checker() #이동한 씬에서 또 다른 씬이동이나 질문지가 있는지 검사함
					break
				else:
					update() #조건이 만족했는데 자기 자신으로 이동하라는 경우 그냥 진행함
					break #일단 위에서부터 조건만족이 걸리면 더이상 탐색안함
		if branchStat == False:
			update()

			"""
			if i <= len(branch):
				update()
				print("읎데여")
			"""
		#update()
		#print("여기한번 나옴")
	else:
		update()
		print("정상상황에 의한 업데이트")
	"""
	elif sceneNumber in branchDict:
		if parameterDict[branchDict[sceneNumber]["condition"]] >= branchDict[sceneNumber]["conditionNumber"]:
			sceneNumber = branchDict[sceneNumber]["destination"]

			update()
		else:
			update()

	else:
		update()
	"""


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
	
	startButton = Button(root,anchor = W,text ="New Game",command = lambda:newStart(),relief=FLAT,compound= CENTER,image =imageLoader(buttonPath),font = uiFont )
	startButton_window = canvas.create_window(canvasSizeX - 100,canvasSizeY - 120,window = startButton)
	

	loadButton = Button(root,anchor = W, text = "Load Game",command = lambda:loader(),relief=FLAT,compound= CENTER,image =imageLoader(buttonPath),font = uiFont )
	loadButton_window = canvas.create_window(canvasSizeX - 100,canvasSizeY - 50,window = loadButton)

#############################	
canvas = Canvas(root, width=canvasSizeX, height=canvasSizeY)
canvas.pack()
pygame.mixer.init()