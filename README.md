# Tkinter VisualNovel Framework

## Basic 

* Code start with
```python
from Main import *
```

* Code End with
```pyhton
update()
canvas.bind("<Button-1>",KeyPressed)
root.mainloop()
```

##### Add Scene

* Function **addcharacter()** can use as image output
* All scene code must be end with **scenes.append(scene)**

```python
scene = Scene("Background Image Name","Speecher","Speech")
scene.addCharacter("Image Name",X position of character,Y position of character)
scenes.append(scene)
```
##### Add Encounter

* All Encounter code must be end with **encounterDict[encounter scene number] = encounter**

```python
encounter = Encounter(encounter scene number)
encounter.addSelect("Ask 1","Condition")
encounter.addSelect("Ask 2","Condition")
encounterDict[encounter scene number] = encounter
```
##### Add Branch

* If condition is true, branchmaker will move  scene from CheckScene to Destination
```python
branchMaker(CheckScene,Destination,"Condition")
```

##### Etc.
* You can change name by follow code
```python
root.title('Program Name')
```





#### Contacts
* [NotonAlcyone](notonalcyone@gmail.com) E-mail me for contacts

