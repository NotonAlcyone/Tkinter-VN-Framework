from tkinter import *

root = Tk()


canvasSizeX = 800 #canvas size 
canvasSizeY = 600 
canvasCenterX = canvasSizeX/2
canvasCenterY = canvasSizeY/2

speechBarPositionX = canvasCenterX
speechBarPositionY = 500

namePostionX = 50
namePostionY = 450
textPositionX = 50
textPositionY = 480

sceneNumber = 0 #scne



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
		self.check = 0

	def addSelect(self,select,parameterName):
		self.selectList.append(SelectList(select,parameterName))

class SelectList:

	def __init__(self,select,parameter):
		self.select = select
		self.parameter = parameter
		parameterDict[parameter] = 0

Press = 1
def KeyPressed(event):
	global Press
	if Press == 1:
		global sceneNumber
		sceneNumber += 1
		checker()
		

calling = lambda parameter : call(parameter)
def call(parameter):
	global sceneNumber
	global Press
	Press = 1
	parameterDict[parameter] = 1
	encounterDict[sceneNumber].check = 1
	sceneNumber += 1
	checker()


def imageLoader(path):
	if path in imagePath:
		return imagePath[path]
	else:
		imagePath[path] = PhotoImage(file="image/"+path)
		return imagePath[path]

def update():
	canvas.delete('all')
	global sceneNumber
	call = scenes[sceneNumber]

	canvas.create_image(canvasCenterX,canvasCenterY,image = imageLoader(call.backgroundImagePath))
	
	for i in range(0,len(call.character)):
		charCall = call.character[i]
		canvas.create_image(charCall.positionX,charCall.positionY,image = imageLoader(charCall.imagePath))

	canvas.create_image(speechBarPositionX,speechBarPositionY,image=imageLoader("Bar.png"))
	canvas.create_text(namePostionX,namePostionY,text = scenes[sceneNumber].speecher,font = "Helvetica 10",anchor = W)
	canvas.create_text(textPositionX,textPositionY,text =  scenes[sceneNumber].speech,font="Helvetica 15",anchor = W)

def checker():
	global sceneNumber
	global Press
	if sceneNumber  == len(scenes):
		Press = 0
	elif sceneNumber in  encounterDict:
		if encounterDict[sceneNumber].check == 0:
			Press = 0
			encounterShower()
		else:
			update()
	elif sceneNumber in branchDict:
		if parameterDict[branchDict[sceneNumber]["condition"]] == 1:
			sceneNumber = branchDict[sceneNumber]["destination"]
			update()
		else:
			update()

	else:
		update()

def branchMaker(scene,destination,condition):
	branchDict[scene] = {"destination":destination,"condition":condition}

def encounterShower():
	global sceneNumber
	global Press 
	for i in range(0,len(encounterDict[sceneNumber].selectList)):
		button = Button(root,text = encounterDict[sceneNumber].selectList[i].select,command = lambda i = i: calling(encounterDict[sceneNumber].selectList[i].parameter) )
		button_window = canvas.create_window(canvasCenterX,canvasCenterY + i*50,window = button)
		

canvas = Canvas(root, width=canvasSizeX, height=canvasSizeY)
canvas.pack()