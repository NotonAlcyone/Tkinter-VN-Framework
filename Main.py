from tkinter import *
from Stat import *
from pygame import mixer
import openpyxl
import json
import os



root = Tk()
imagePath = {}
parameterDict = {}
musicDict = {}

def xlLoader():
	global sceneData
	if os.path.isfile("data.xlsx"):
		row = openpyxl.load_workbook('data.xlsx').active.rows
		arr = []
		next(row) #
		for i in row:
			data = {}
			if i[1].value == "Scene":
				data = {"sceneType":"Scene","Music":i[2].value,"scene":{"BGpath":i[4].value,"Speecher":i[5].value,"Speech":i[6].value,"Voice":i[7].value,}}
				if i[8].value != None:
					data["scene"]["character"] = eval(i[8].value)
				if i[9].value != None:
					data["branch"] = eval(i[9].value)
			elif i[1].value == "Encounter":
				data = {"sceneType":"Encounter","Music":i[2].value}
				data["encounter"] = eval(i[3].value)
			arr.append(data)
		sceneData = arr

def scriptLoader(): # json 불러오는거
	global sceneData
	if os.path.isfile("orgindata.json"): # 스크립트 json 데이터가 있으면
		file = open("orgindata.json","r") # json 데이터 열어서
		sceneData = json.loads(file.read()) # sceneData 에 변환해서 넣어줌

def imageLoader(path): # 이미지 불러오는거
	global imagePath
	if path in imagePath: # 이미 불러왔던 이미지라면 있던거 리턴
		return imagePath[path]
	else: # 처음 불러오는 이미지면 불러와서 넣어주고 리턴
		imagePath[path] = PhotoImage(file = imageFolder + path) 
		return imagePath[path]

wordPress = False
press = True
def keyPressed(event): # 키 눌렸을때 호출 함수
	global press
	global wordPress
	if press == True: # 키 잠금이 안걸렸다면
		voiceStop()
		if wordPress == False: # 대사가 전부 작성되었으면
			sceneMover(False,1) # 다음씬으로 넘기기
		else: # 대사가 전부 작성이 안되었으면
			wordCancel() # 대사 작성 스킵

def voiceStop():
	global voice
	if "scene" in sceneData[sceneNumber]:
		data = sceneData[sceneNumber]["scene"] # 짧게
		if "Voice" in data and data["Voice"] != None:
			voice.stop()

text = []
def wordType(str, counter, x, y, speed):
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
	wordType(sceneData[sceneNumber]["scene"]["Speech"], 0, textPositionX, textPositionY, 0)

def sceneMover(move, amount):
	global sceneNumber
	if move == True: # 이동이라면
		sceneNumber = amount # 해당값으로 이동
	else: # 이동이 아니면
		sceneNumber += amount # 해당 값만큼 더함
	update() # 화면에 반영

def sceneDraw(): # 일반 씬 드로우
	global voice
	global sceneData
	global sceneNumber
	canvas.delete("all")
	data = sceneData[sceneNumber]["scene"] # 짧게
	canvas.create_image(canvasCenterX,canvasCenterY, image = imageLoader(data["BGpath"])) # 캔버스에 배경 출력
	if "character" in data:
		for i in range(0,len(data["character"])):# 캔버스에 캐릭터 표기된만큼 출력
			character = data["character"][i] 
			canvas.create_image(character["X"],character["Y"], image = imageLoader(character["imagePath"]))
	if data["Speecher"] != "" and nameBarStat == True: # 말하는 사람이 있으면 이름과 대사박스 출력, UI에 따른 화자창 미존재 고려
		canvas.create_image(namePostionX, namePostionY, image = imageLoader(nameBarPath))
		canvas.create_text(namePostionX,namePostionY,text = data["Speecher"],font = nameFont, fill= nameFontColor)
	if data["Speech"] != "": # 대사 있으면 대사박스 출력
		canvas.create_image(speechBarPositionX, speechBarPositionY, image = imageLoader(barPath))
		wordType(data["Speech"], 0, textPositionX, textPositionY, int(textTypeSpeed * 1000))
	if saveButton == True:
		saveButton1 = Button(root, text = "Save", command = saver, relief = FLAT, compound = CENTER, image = imageLoader(buttonPath), font = uiFont)
		saveButton_window = canvas.create_window(canvasSizeX - 100, 50, window = saveButton1)
	if "Voice" in data and data["Voice"] != None:
		print("보이스 나가요")
		voice = mixer.Sound(voiceFolder + data["Voice"])
		voice.set_volume(voiceVolume / 10)
		voice.play()	

def encounterDraw():
	global sceneNumber
	global sceneData
	encount = sceneData[sceneNumber]["encounter"]
	encounterStart = (canvasSizeY - len(encount) * encounterSpace) / 2
	for i in range(0,len(encount)):
		encounterBUtton = Button(root,text = encount[i]["select"],relief = FLAT, compound = CENTER, image = imageLoader("Bar_Select.png"), font = nameFont, command = lambda i = i: encounterCall(encount[i]["parameter"], encount[i]["factor"]))
		encounterButton_window = canvas.create_window(canvasCenterX, encounterStart + i * encounterSpace, window = encounterBUtton)

def encounterCall(parameter,factor):
	global sceneNumber
	global press
	press = True
	if parameter in parameterDict:
		parameterDict[parameter] += factor
	else:
		parameterDict[parameter] = factor
	sceneMover(False, 1)

def saver():
	global sceneNumber
	global parameterDict
	file = open("saver.txt", 'w+')
	savelist=[str(sceneNumber) + "\n", str(parameterDict)]
	file.writelines(savelist)
	file.close()

def loader():
	global sceneNumber
	global parameterDict
	global sceneData
	if os.path.isfile("saver.txt"):
		file = open("saver.txt", 'r')
		data = file.readlines()
		parameterDict = eval(data[1])
		sceneNum = int(data[0][:-1])
		if sceneData[sceneNum]["sceneType"] == "Encounter":
			sceneMover(True,sceneNum -1)
		else:
			sceneMover(True,sceneNum)
		canvas.bind("<Button-1>", keyPressed)
	else:
		sceneNumber = 0
		update()
		canvas.bind("<Button-1>", keyPressed)

def update():
	global press
	global sceneData
	global sceneNumber
	if sceneNumber == len(sceneData): # 현 씬번호가 마지막 씬 번호라면
		print("키막힘")
		press = False # 클릭 막음
	elif "branch" in sceneData[sceneNumber]:
		branch = sceneData[sceneNumber]["branch"]
		branchStat = False
		for i in range(0, len(branch)): # 분기점 배열크기만큼 돌려서
			if branch[i]["condition"] in parameterDict and int(parameterDict[branch[i]["condition"]]) >= int(branch[i]["conditionNum"]) : # 만약 같은게 현 파라미터에 있고 그값이 적용되어야 한다면
				branchStat = True
				if sceneData[branch[i]["destination"]]["sceneType"] == "Encounter": # 도착씬이 인카운터면 바로 이전씬으로
					sceneMover(True,int(branch[i]["destination"])-1)				
				else:
					sceneMover(True,int(branch[i]["destination"])) # 이동
				break
		if branchStat == False:
			drawCall() #만약 위에서 발견안됬으면 해당씬 그리기
	else:
		drawCall()

def drawCall():
	global press
	global sceneData
	global sceneNumber
	if sceneData[sceneNumber]["Music"] != "":
		music(sceneData[sceneNumber]["Music"])
	if sceneData[sceneNumber]["sceneType"] == "Scene": # 출력 해야하는게 일반 씬 이라면
		sceneDraw()
	elif sceneData[sceneNumber]["sceneType"] == "Encounter": # 출력 해야되는게 질문씬 이라면
		press = False # 버튼을 누르지 않고는 다음거 못가게
		encounterDraw()

def music(path):
	global currentMusic
	global currentMusicName
	if 'currentMusic' not in globals():
		currentMusicName = path
		musicPlay(path)
	if currentMusicName != path:
		currentMusic.fadeout(800)
		musicPlay(path)

def musicPlay(path):
	global currentMusic
	global currentMusicName
	musicPath = voiceFolder + path
	currentMusicName = path
	currentMusic = mixer.Sound(musicPath)
	currentMusic.set_volume(BGMVolume / 10)
	currentMusic.play(loops = -1)

def mainScene():
	xlLoader() # 엑셀 불러옴
	#scriptLoader() # 스크립트 불러옴
	if titleBGMPath != "":
		print("노래달려욧")
		music(titleBGMPath)

	canvas.create_image(canvasCenterX,canvasCenterY,image = imageLoader(background)) # 타이틀 이미지 그림

	startButton = Button(root,anchor = W, text = "New Game", command = newStart, relief = FLAT, compound = CENTER, image= imageLoader(buttonPath),font = uiFont) # 시작 버튼 그림
	startButton_window = canvas.create_window(startButtonPosX, startButtonPosY, window = startButton)

	if saveButton == True:
		loadButton = Button(root, anchor = W, text = "Load Game", command = loader, relief = FLAT, compound = CENTER, image = imageLoader(buttonPath), font = uiFont)
		loadButton_window = canvas.create_window(canvasSizeX - 100, canvasSizeY - 50, window = loadButton)

def newStart():
	global sceneNumber
	sceneNumber = 0 #새로 시작할때는 0부터
	update()
	canvas.bind("<Button-1>", keyPressed)
	root.bind("<space>", keyPressed)

canvas = Canvas(root, width = canvasSizeX, height = canvasSizeY)
canvas.pack()
root.title("Someone's Fragment")
mixer.init()
mainScene()
root.mainloop()