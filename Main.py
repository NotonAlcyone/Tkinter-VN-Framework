from tkinter import *
from Stat import *
import pygame
import os

root = Tk()



imagePath = {}
scenes = list()
encounterDict = {}
parameterDict= {}
branchDict={}

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
		textInvoke = canvas.after(int(textTypeSpeed*1000),lambda:wordType(str,counter+1))
		if counter < len(str):
			canvas.after(int((textTypeSpeed*1000)-1),lambda:wordDelete())
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
		voice.set_volume(voiceVolume/10)
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

	if sceneNumber == len(scenes):
		Press = False
		gameTheme.stop()
	elif sceneNumber in  encounterDict:
		Press = False
		encounterShower()
	elif sceneNumber in branchDict:
		branchStat = False
		branch = branchDict[sceneNumber].branchList
		for i in range(0,len(branch)):
			if parameterDict[branch[i].condition] >= branch[i].conditionNumber:
				if sceneNumber != branch[i].destination:
					branchStat = True
					sceneNumber = branch[i].destination
					if sceneNumber in encounterDict: #만약 이동한씬이 인카운터 씬아라면, 바로 그전으로 이동시킴
						sceneNumber -= 1
					checker() #이동한 씬에서 또 다른 씬이동이나 질문지가 있는지 검사함
					break
				else:#조건이 만족했는데 자기 자신으로 이동하라는 경우 그냥 진행함
					break #일단 위에서부터 조건만족이 걸리면 더이상 탐색안함
		if branchStat == False:
			update()
	else:
		update()

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
	bgmStarter()
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
	bgmStarter()
	global sceneNumber
	sceneNumber = 0
	update()
	canvas.bind("<Button-1>",keyPressed)


def bgmStarter():
	if titleBGM == True:
		titleTheme.fadeout(800)

	if ingameBGM == True:
		gameTheme.play(loops=-1)

#############################

def mainScene(background):

	if titleBGM == True:
		global titleTheme
		titleTheme = pygame.mixer.Sound(voiceFolder + titleBGMPath)
		titleTheme.set_volume(titleBGMVolume/10)
		titleTheme.play(loops=-1)
	if ingameBGM == True:
		global gameTheme
		gameTheme = pygame.mixer.Sound(voiceFolder + ingameBGMPath)
		gameTheme.set_volume(ingameBGMVolume/10)



	canvas.create_image(canvasCenterX,canvasCenterY,image = imageLoader(background))
	
	startButton = Button(root,anchor = W,text ="New Game",command = lambda:newStart(),relief=FLAT,compound= CENTER,image =imageLoader(buttonPath),font = uiFont )
	startButton_window = canvas.create_window(canvasSizeX - 100,canvasSizeY - 120,window = startButton)
	

	loadButton = Button(root,anchor = W, text = "Load Game",command = lambda:loader(),relief=FLAT,compound= CENTER,image =imageLoader(buttonPath),font = uiFont )
	loadButton_window = canvas.create_window(canvasSizeX - 100,canvasSizeY - 50,window = loadButton)

#############################	
canvas = Canvas(root, width=canvasSizeX, height=canvasSizeY)
canvas.pack()
pygame.mixer.init()