from Main import *




root.title("Someone's Fragment")

scene = Scene("Background.png","","옆집에서 여자 둘이서 다투는 소리가 들린다...")
scenes.append(scene)

scene = Scene("Background.png","","엿들어볼까..?")
scenes.append(scene)

scenes.append(scene)

scene = Scene("Background.png","???","...꺼야?")
scenes.append(scene)

scene = Scene("Background.png","???","귀찮아아아아아앙~")
scenes.append(scene)

scene = Scene("Background.png","???","귀찮다고 집에만 있으면 어떡해 세린아! 나가서 운동도 하고 돈도 벌어야지!")
scenes.append(scene)

scene = Scene("Background.png","세린","돈이라면 많아~ 아무것도 안해도 상관없어~ 안그래?")
scenes.append(scene)

scene = Scene("Background.png","???","그게 너네 부모님돈이지 니 돈이냐!")
scenes.append(scene)

scene = Scene("Background.png","세린","하... 이 이야기 안꺼내기로 했잖아","Voice.wav")
scenes.append(scene)

scene = Scene("Background.png","???","틀린말은 아니잖아")
scenes.append(scene)

scene = Scene("Background.png","","창문을 통해보면 무슨 일인지 볼수있을텐데... 어떻게 하지?")
scenes.append(scene)

scenes.append(scene)

scene = Scene("Background.png","세린","아 알았어 나가면 되잖아")
scene.addCharacter("Serin_Normal.png",canvasCenterX,canvasCenterY+100)
scenes.append(scene)

scene = Scene("Background.png","???","하여튼 게으른걸로는 우주 최강이라니까...")
scene.addCharacter("Friend_Look.png",canvasCenterX-300,canvasCenterY+100)
scene.addCharacter("Serin_Normal.png",canvasCenterX+300,canvasCenterY+100)
scenes.append(scene)

scene = Scene("Background.png","세린","흑...맞아... 나 그냥 죽어버릴래")
scene.addCharacter("Friend_Look.png",canvasCenterX-300,canvasCenterY+100)
scene.addCharacter("Serin_Crying.png",canvasCenterX+300,canvasCenterY+100)
scenes.append(scene)

scene = Scene("Background.png","???","또또또 그 소리... 빨리 같이 나가자 따라와")
scene.addCharacter("Friend_Normal.png",canvasCenterX-300,canvasCenterY+100)
scene.addCharacter("Serin_Crying.png",canvasCenterX+300,canvasCenterY+100)
scenes.append(scene) #13

scene = Scene("Background.png","","다시 정적이 감돈다...")
scenes.append(scene)

scene = Scene("Background.png","","엿듣는건 나쁜거니까...")
scenes.append(scene)

scene = Scene("Background.png","","엿보는건 나쁜거니까...")
scenes.append(scene)

scene = Scene("Background.png","","잠이나 더 자야지...")
scenes.append(scene)

###
encounter = Encounter(2)
encounter.addSelect("엿듣는다","Fine",1)
encounter.addSelect("포기한다","ListenX",1)
encounterDict[2] = encounter

encounter = Encounter(11)
encounter.addSelect("엿본다","Fine",1)
encounter.addSelect("포기한다","LookX",1)
encounterDict[11] = encounter

###

branchMaker(3,17,"ListenX",1)
branchMaker(18,19,"ListenX",1)

branchMaker(12,19,"LookX",1)

branchMaker(17,19,"Fine",2)

###

mainScene("main.png")

root.mainloop()