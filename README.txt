Script Example Below

scene = Scene("Forest.png","17Y Girl","Hello")
scene.addCharacter("Girl_Normal.png",canvasCenterX,canvasCenterY+100) 
scenes.append(scene)
scene = Scene("Space.png","Hero","Hellooooo")
scene.addCharacter("Hero_Smile.png",canvasCenterX,canvasCenterY+100) 
scene.addCharacter("Girl_Smile.png",canvasCenterX-250,canvasCenterY+100) 
scenes.append(scene)

'scenes' is list of Scenes
You should add 
scene = Scene("Background Image Path include file type","speecher,"speech") 
for background image and Speech in scene
if you need character or something, you can use
scene.addCharacter("Image File path",X postion of Image,Y position of image)

after character add, you should append scene on list like

scenes.append(scene)
