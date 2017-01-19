# Tkinter VisualNovel Framework



### What is this?
Python Framework for making VisualNovel

### How to Script

* Script start with
```python
from Main import *
```

* Script end with
```pyhton
mainScene("main image")
root.mainloop()
```

##### Add Scene and Character

* Function **addcharacter()** can use as image output
* All scene code must be end with **scenes.append(scene)**

```python
scene = Scene("Background Image Name","Speecher","Speech")
scene.addCharacter("Image Name",X Position,Y Position)
scenes.append(scene)
```
##### Add Encounter

* All Encounter code must be end with **encounterDict[encounter scene number] = encounter**
* Button click will give true to condition

```python
encounter = Encounter(encounter scene number)
encounter.addSelect("Ask 1","Condition")
encounter.addSelect("Ask 2","Condition")
encounterDict[encounter scene number] = encounter
```
##### Add Branch

* If condition on encounter is true, branchmaker will move  scene from CheckScene to Destination
```python
branchMaker(CheckScene,Destination,"Condition")
```

##### Etc.
* You can change name by follow code
```python
root.title('Program Name')
```

### What you need

What you need is **Python 3**




## Contacts
* [NotonAlcyone](notonalcyone@gmail.com) E-mail for contacts

