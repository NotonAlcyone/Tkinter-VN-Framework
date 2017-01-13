from tkinter import *

root = Tk()
root.title('Missile Continuous Launch System')#VN's nickname in korea :)

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

sceneNumber = 0 #scene



class Scene:
	backgroundImagePath = ""
	speech = ""
	speecher = ""
	character = []

	def __init__(self,backgroundImagePath,speecher,speech):
		self.backgroundImagePath = backgroundImagePath
		self.speecher = speecher
		self.speech = speech
		self.character = []
		

	def addCharacter(self,imagePath,x,y):
		self.character.append(Character(imagePath,x,y))

class Character:
	imagePath = ""
	positionX = 0
	positionY = 0

	def __init__(self,imagePath,x,y):
		self.imagePath = imagePath
		self.positionX = x
		self.positionY = y

def KeyPressed(event):

	canvas.delete('all')
	global sceneNumber
	sceneNumber += 1

	update()
	print(sceneNumber)

imagePath = {}	
def imageLoader(path):
	if path in imagePath:
		return imagePath[path]
	else:
		imagePath[path] = PhotoImage(file=path)
		return imagePath[path]

def update():
	call = scenes[sceneNumber]
	canvas.create_image(canvasCenterX,canvasCenterY,image = imageLoader(call.backgroundImagePath))
	
	for i in range(0,len(call.character)):
		charCall = call.character[i]
		canvas.create_image(charCall.positionX,charCall.positionY,image = imageLoader(charCall.imagePath))

	canvas.create_image(speechBarPositionX,speechBarPositionY,image=imageLoader("Bar.png"))
	canvas.create_text(namePostionX,namePostionY,text = scenes[sceneNumber].speecher,anchor = W)
	canvas.create_text(textPositionX,textPositionY,text =  scenes[sceneNumber].speech,font=(40),anchor = W)



canvas = Canvas(root, width=canvasSizeX, height=canvasSizeY)
canvas.pack()

scenes = list()
########################### Script Start ###########################
"""


"""
############################ Script End ############################

update()
canvas.bind("<Button-1>",KeyPressed)
root.mainloop()