from tkinter import *
from Stat import *
import pygame
import os

root = Tk()
imagePath = {}
scenes = list()
encounterDict = {}
parameterDict = {}
branchDict = {}
musicDict = {}
musicDefDict = {}
gameTheme = None

class Scene:
	def __init__(self, backgroundImagePath, speecher, speech, voice = None):
		self.backgroundImagePath = backgroundImagePath
		self.speecher = speecher
		self.speech = speech
		self.voice = voice
		self.character = []
	def addCharacter(self, imagePath, x, y):
		self.character.append(Character(imagePath, x, y))

class Character:
	def __init__(self, imagePath, x, y):
		self.imagePath = imagePath
		self.positionX = x
		self.positionY = y

class Encounter:
	def __init__(self, startScene):
		self.startScene = startScene
		self.selectList = []
	def addSelect(self, select, parameterName, factor):
		self.selectList.append(SelectList(select, parameterName, factor))

class SelectList:
	def __init__(self, select, parameter, factor):
		self.select = select
		self.parameter = parameter
		if parameter not in parameterDict:
			parameterDict[parameter] = 0
		self.factor = factor

class Branch:
	def __init__(self, scene):
		self.scene = scene
		self.branchList = []
	def addBranch(self, destination, condition, conditionNumber):
		self.branchList.append(BranchList(destination, condition, conditionNumber))

class BranchList:
	def __init__(self, destination, condition, conditionNumber):
		self.destination = destination
		self.condition = condition
		self.conditionNumber = conditionNumber

def sceneTester():
	for i in range(0,len(scenes)):
		if i in encounterDict:
			print("{i} 선택지 씬 입니다.".format(i=i))
			encounter = encounterDict[i].selectList
			for j in range(len(encounter)):
				print("	[{select}] 선택시 ({parameter}) 수치 {factor} 만큼 변화".format(select = encounter[j].select,parameter = encounter[j].parameter, factor = encounter[j].factor))

		else:
			print("{i} {speech}".format(i=i,speech  = scenes[i].speech))


def branchTester():
	for i in range ( 0, len(scenes)):
		if i in branchDict:
			print("씬 넘버 {i}".format(i = i))
			branch = branchDict[i].branchList
			for j in range(0,len(branch)):
				print("조건 {condition}이 {conditionNumber} 이상일때 {destination} 으로 이동".format(condition =branch[j].condition, conditionNumber =branch[j].conditionNumber,destination = branch[j].destination))
			print("----------------")

def musicTester():
	for i in range(0,len(scenes)):
		if i in musicDict:
			print("{i}번 씬에 재생되는 음악은 {music} 입니다.".format(i = i,music = musicDict[i]))



wordPress = False
press = True
def keyPressed(event):
	global press
	global wordPress
	global sceneNumber
	if press == True:
		if wordPress == False:
			voiceStop()
			sceneMover(False, 1)
			wordPress = True
			checker()
		elif wordPress == True:
			wordCancel()

def voiceStop():
	if scenes[sceneNumber].voice != None:
		voice.stop()

def sceneMover(move, amount):
	global sceneNumber
	if move == True:
		sceneNumber = amount
	else:
		sceneNumber += amount

text = []
def wordType(str, counter, x, y, speed):
	global press
	global wordPress
	wordPress = True
	if counter <= len(str) - 1:
		global text
		global textInvoke
		if str[counter] == "\n":
			if autoLineAddMove == True:
				for i in range(0, len(text)):
					canvas.move(text[i],0,-lineHeight)
			textInvoke = canvas.after(0, lambda: wordType(str, counter + 1, textPositionX, y + lineHeight, speed))
		elif str[counter] == " ":
			textInvoke = canvas.after(speed, lambda: wordType(str, counter + 1, x + (letterSpace / 2), y, speed))
		elif str[counter] in specialWord:
			text.append(canvas.create_text(x, y, text = str[counter], anchor = NW, font = textFont, fill = textFontColor))
			textInvoke = canvas.after(speed, lambda: wordType(str, counter + 1, x + (letterSpace / 2), y, speed))
		else:
			text.append(canvas.create_text(x, y, text = str[counter], anchor = NW, font = textFont, fill = textFontColor))
			textInvoke = canvas.after(speed, lambda: wordType(str, counter + 1, x + letterSpace, y, speed))
	else:
		wordPress = False
		text = []

def wordCancel():
	global wordPress
	global text
	wordPress = False
	canvas.after_cancel(textInvoke)
	for i in range(0, len(text)):
		canvas.delete(text[i])
	text = []
	wordType(scenes[sceneNumber].speech, 0, textPositionX, textPositionY, 0)
	
def call(parameter, factor):
	global sceneNumber
	global press
	press = True
	parameterDict[parameter] += factor
	sceneMover(False, 1)
	checker()

def imageLoader(path):
	if path in imagePath:
		return imagePath[path]
	else:
		imagePath[path] = PhotoImage(file = imageFolder + path)
		return imagePath[path]

def update():
	global voice
	global gameTheme
	global playStat
	canvas.delete('all')
	global sceneNumber
	call = scenes[sceneNumber]
	canvas.create_image(canvasCenterX, canvasCenterY, image = imageLoader(call.backgroundImagePath))
	
	for i in range(0, len(call.character)):
		charCall = call.character[i]
		canvas.create_image(charCall.positionX, charCall.positionY, image = imageLoader(charCall.imagePath))
	if scenes[sceneNumber].speech != "":
		canvas.create_image(speechBarPositionX, speechBarPositionY, image = imageLoader(barPath))
	if scenes[sceneNumber].speecher != "" and nameBarStat == True:
		canvas.create_image(namePostionX, namePostionY, image = imageLoader(nameBarPath))
		
	canvas.create_text(namePostionX, namePostionY, text = scenes[sceneNumber].speecher, font = nameFont, fill= nameFontColor)
	wordType(scenes[sceneNumber].speech, 0, textPositionX, textPositionY, int(textTypeSpeed * 1000))

	if scenes[sceneNumber].voice != None:
		voice = pygame.mixer.Sound(voiceFolder + scenes[sceneNumber].voice)
		voice.set_volume(voiceVolume / 10)
		voice.play()

	if saveButton == True:
		saveButton1 = Button(root, text = "Save", command = saver, relief = FLAT, compound = CENTER, image = imageLoader(buttonPath), font = uiFont)
		saveButton_window = canvas.create_window(canvasSizeX - 100, 50, window = saveButton1)

	if ingameBGM == False:
		return
	if sceneNumber not in musicDict:
		gameTheme.fadeout(800)
		playStat = False
		return
	if gameTheme == musicDefDict[musicDict[sceneNumber]] and playStat == True:
		return
	if gameTheme != None:
		gameTheme.fadeout(800)
		musicChecker(musicDict[sceneNumber])
		return
	musicChecker(musicDict[sceneNumber])

def musicChecker(Name):
	global playStat
	global gameTheme
	playStat = True
	gameTheme = musicDefDict[Name]
	gameTheme.set_volume(BGMVolume / 10)
	gameTheme.play(loops = -1)

def saver():
	global sceneNumber
	global parameterDict
	file = open("saver.txt", 'w+')
	savelist=[str(sceneNumber) + "\n", str(parameterDict)]
	file.writelines(savelist)
	file.close()

def checker():
	global sceneNumber
	global press
	global parameterDict
	if sceneNumber == len(scenes):
		press = False
		if ingameBGM == True:
			gameTheme.stop()
	elif sceneNumber in  encounterDict:
		press = False
		encounterShower()
	elif sceneNumber in branchDict:
		branchStat = False
		branch = branchDict[sceneNumber].branchList
		for i in range(0, len(branch)):
			if parameterDict[branch[i].condition] >= branch[i].conditionNumber:
				if sceneNumber == branch[i].destination:
					break
				branchStat = True
				sceneMover(True, branch[i].destination)
				if sceneNumber in encounterDict:
					sceneMover(False, -1)
				checker()
				break
		if branchStat == False:
			update()
	else:
		update()

def encounterShower():
	global sceneNumber
	encount = encounterDict[sceneNumber].selectList
	encounterStart = (canvasSizeY - len(encount) * encounterSpace) / 2
	for i in range(0, len(encount)):
		button = Button(root, text = encount[i].select, command = lambda i = i: call(encount[i].parameter, encount[i].factor), relief = FLAT, compound = CENTER, image = imageLoader("Bar_Select.png"), font = nameFont)
		button_window = canvas.create_window(canvasCenterX, encounterStart + i * encounterSpace, window = button)

def loader():
	global sceneNumber
	global parameterDict
	titleMusicCheck()
	if os.path.isfile("saver.txt"):
		file = open("saver.txt", 'r')
		data = file.readlines()
		sceneMover(True, int(data[0][:-1]))		
		parameterDict = eval(data[1])
		if sceneNumber in encounterDict:
			sceneMover(False, -1)
		update()
		canvas.bind("<Button-1>", keyPressed)
	else:
		sceneNumber = 0
		update()
		canvas.bind("<Button-1>", keyPressed)

def newStart():
	titleMusicCheck()
	global sceneNumber
	sceneNumber = 0
	update()
	canvas.bind("<Button-1>", keyPressed)

def titleMusicCheck():
	if titleBGM == True and ingameBGM == False:
		gameTheme.fadeout(800)
		playStat = False

def musicQueue(startNumber, endNumber, musicName):
	for i in range(startNumber, endNumber+1):
		musicDict[i] = musicName
	if musicName not in musicDefDict:
		musicDefDict[musicName] = pygame.mixer.Sound(voiceFolder + musicName)

def mainScene(background):
	if titleBGM == True:
		global gameTheme
		gameTheme = pygame.mixer.Sound(voiceFolder + titleBGMPath)
		gameTheme.set_volume(BGMVolume / 10)
		gameTheme.play(loops = -1)
		playStat = True

	canvas.create_image(canvasCenterX, canvasCenterY, image = imageLoader(background))
	startButton = Button(root, anchor = W, text = "New Game", command = newStart, relief = FLAT, compound = CENTER, image = imageLoader(buttonPath), font = uiFont)
	startButton_window = canvas.create_window(canvasSizeX - 100, canvasSizeY - 120, window = startButton)
	if saveButton == True:
		loadButton = Button(root, anchor = W, text = "Load Game", command = loader, relief = FLAT, compound = CENTER, image = imageLoader(buttonPath), font = uiFont)
		loadButton_window = canvas.create_window(canvasSizeX - 100, canvasSizeY - 50, window = loadButton)




def jsonParser():
	for i in range(0,len(data)):
		t = str(i+1)
		if data[t]["sceneType"] == "Scene":
			trueData = data[t]["scene"]
			if "Voice" in trueData:
				scene = Scene(trueData["BGpath"],trueData["Speecher"],trueData["Speech"],trueData["Voice"])
				scenes.append(scene)		
			else:
				scene = Scene(trueData["BGpath"],trueData["Speecher"],trueData["Speech"])
				scenes.append(scene)
		elif data[t]["sceneType"] == "Encounter":
			scenes.append(scene)
			encounter = Encounter(t)
			for j in range(0,len(data[t]["encounter"] )):
				sht = data[t]["encounter"]
				encounter.addSelect(sht["select"], sht["parameter"], int(sht["factor"]))
			encounterDict[t] = encounter
		if "branch" in data[t]:
			branch = Branch(t)
			for k in range(0,len(data[t]["branch"])):
				shr = data[k]["branch"]
				branch.addBrach(int(shr["destination"]),shr["condition"],int(shr["conditionNum"]))
			branchDict[t] = branch
#############################	
canvas = Canvas(root, width = canvasSizeX, height = canvasSizeY)
canvas.pack()
pygame.mixer.init()