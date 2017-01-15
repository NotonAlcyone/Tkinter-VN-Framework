from Main import *
root.title('Missile Continuous Launch System')#VN's nickname in korea :)


scene = Scene("Forest.png","17Y","안녕 고양아")
scene.addCharacter("Character_Normal.png",canvasCenterX,canvasCenterY+100)
scenes.append(scene)

scene = Scene("Forest.png","Cat","myaaaaa")
scene.addCharacter("Cat_Normal.png",canvasCenterX - 250,canvasCenterY+100)
scene.addCharacter("Character_Normal.png",canvasCenterX + 250,canvasCenterY+100)
scenes.append(scene)

scene = Scene("Forest.png","17Y","나랑같이 우주로 올라갈래?")
scene.addCharacter("Cat_Normal.png",canvasCenterX - 250,canvasCenterY+100)
scene.addCharacter("Character_Normal.png",canvasCenterX + 250,canvasCenterY+100)
scenes.append(scene)

scenes.append(scene) #Encounter Scene should be stay as empty

scene = Scene("BackGround.png","Cat","myaaaaaa?")
scene.addCharacter("Cat_Normal.png",canvasCenterX - 250,canvasCenterY+100)
scene.addCharacter("Character_Normal.png",canvasCenterX + 250,canvasCenterY+100)
scenes.append(scene)

scene = Scene("BackGround.png","17Y","짠 우주란다!")
scene.addCharacter("Cat_Normal.png",canvasCenterX - 250,canvasCenterY+100)
scene.addCharacter("Character_Normal.png",canvasCenterX + 250,canvasCenterY+100)
scenes.append(scene)

scene = Scene("Forest.png","17Y","흐음 가기싫어도 데려갈거야!")
scene.addCharacter("Cat_Normal.png",canvasCenterX - 250,canvasCenterY+100)
scene.addCharacter("Character_Normal.png",canvasCenterX + 250,canvasCenterY+100)
scenes.append(scene)

scene = Scene("BackGround.png","17Y","ㅋㅋㅋㅋㅋㅋ 어때?")
scene.addCharacter("Cat_Normal.png",canvasCenterX - 250,canvasCenterY+100)
scene.addCharacter("Character_Normal.png",canvasCenterX + 250,canvasCenterY+100)
scenes.append(scene)

scene = Scene("BackGround.png","cat","Mya...")
scene.addCharacter("Cat_Normal.png",canvasCenterX - 250,canvasCenterY+100)
scene.addCharacter("Character_Normal.png",canvasCenterX + 250,canvasCenterY+100)
scenes.append(scene)

#############################
encounter = Encounter(3)
encounter.addSelect("따라간다","Peaceful")
encounter.addSelect("따라가지않는다","Negative")
encounterDict[3] = encounter
#############################

branchMaker(6,7,"Peaceful")
branchMaker(4,6,"Negative")

#############################

update()
canvas.bind("<Button-1>",KeyPressed)
root.mainloop()