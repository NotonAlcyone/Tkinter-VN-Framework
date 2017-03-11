from Main import *




root.title('Missile Continuous Launch System')#VN's nickname in korea :)

scene = Scene("Forest.png","17Y","안녕 고양아아아아아아아아아아아아아아아아아아")
scene.addCharacter("Character_Normal.png",canvasCenterX,canvasCenterY+100)
scenes.append(scene)

scene = Scene("Forest.png","Cat","myaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
scene.addCharacter("Cat_Normal.png",canvasCenterX - 250,canvasCenterY+100)
scene.addCharacter("Character_Normal.png",canvasCenterX + 250,canvasCenterY+100)
scenes.append(scene)

scene = Scene("Forest.png","17Y","나랑같이 우주로 올라갈래?")
scene.addCharacter("Cat_Normal.png",canvasCenterX - 250,canvasCenterY+100)
scene.addCharacter("Character_Normal.png",canvasCenterX + 250,canvasCenterY+100)
scenes.append(scene)

scenes.append(scene) #선택지씬

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

scenes.append(scene)

scene = Scene("BackGround.png","17Y","할퀴지 마!")
scene.addCharacter("Cat_Normal.png",canvasCenterX - 250,canvasCenterY+100)
scene.addCharacter("Character_Normal.png",canvasCenterX + 250,canvasCenterY+100)
scenes.append(scene)

scene = Scene("BackGround.png","17Y","으앜 니 혀 바늘 돋았지")
scene.addCharacter("Cat_Normal.png",canvasCenterX - 250,canvasCenterY+100)
scene.addCharacter("Character_Normal.png",canvasCenterX + 250,canvasCenterY+100)
scenes.append(scene)

scene = Scene("BackGround.png","","",False)#background OnlyScene
scenes.append(scene)

#############################
encounter = Encounter(3)
encounter.addSelect("따라간다","Peaceful",1)
encounter.addSelect("따라가지않는다","Negative",1)
encounterDict[3] = encounter

encounter = Encounter(9)
encounter.addSelect("할퀸다","Nega",1)
encounter.addSelect("핥는다","Peac",1)
encounterDict[9] = encounter
#############################

branchMaker(6,7,"Peaceful",1)
branchMaker(4,6,"Negative",1)
branchMaker(11,12,"Nega",1)
branchMaker(10,11,"Peac",1)

mainScene("Forest.png")

root.mainloop()