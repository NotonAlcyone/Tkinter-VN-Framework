# Tkinter Visualnovel Framework

tkinter 라이브러리를 사용한 비주얼 노벨 프레임워크입니다.

![sample](https://cloud.githubusercontent.com/assets/15938440/23822326/83f86082-068e-11e7-9805-c2ccef352f1a.png)

## 사용프로그램
	
* Python 3
* tkinter 
* [pygame](https://www.pygame.org/)

## 사용법

프로젝트의 main.py 를 임포트 하고 씬,선택지,분기점등을 추가한 후 최하단에 root.mainloop()를 넣고 빌드합니다.
```python
from main import *
#################
script here
#################
mainScene("시작화면 이미지")
root.mainloop()
```

### 씬 설정

#### 배경, 대사, 음성 추가
![sample3](https://cloud.githubusercontent.com/assets/15938440/23822359/181ea488-068f-11e7-88af-5f59f0241b90.png)

```python
scene = Scene("배경 이미지 경로", "화자", "대사", "음성 경로")
```
* 배경이미지 경로,화자,대사,음성 경로 모두 문자열로 입력 받습니다.
* 배경이미지와 음성은 ***.png 식으로 확장자이름도 전부 작성해줍니다.
* 화자를 공백으로 넣고싶으시다면 "" 로 빈문자열을 넣어주세요.
* 대사에 개행이 필요하다면 \n을 포함시킵니다. ex) "안녕하세요.\n반갑습니다."
* 화자나 대사창이 공백일경우 해당하는 창이 등장하지 않습니다
* 음성 경로를 작성하지 않으면 음성이 없는 것으로 간주합니다


#### 이미지 추가
```python
scene.addCharacter("이미지 경로", X 좌표, Y 좌표)
```
* 이미지 경로는 문자열, X와 Y좌표는 정수를 입력 받습니다.

#### 마무리
```python
scenes.append(scene)
```
* 위에서 설정된 설정들을 실제로 씬리스트에 넣습니다.
* 최초로 추가된 0번씬부터 시작해서 씬 넘버가 1씩 증가하며 저장됩니다.
* 단독으로 사용할경우 비어있는 씬이 씬리스트에 추가됩니다.

#### 참고사항
* **씬넘버는 0부터 시작됩니다**
* 모든 이미지는 스틸샷으로 출력되며 GIF를 출력시킬경우 가장 첫 프레임만 출력됩니다.

### 선택지 설정
![sample2](https://cloud.githubusercontent.com/assets/15938440/23822344/e1d831b4-068e-11e7-9b7c-c0ea917d8600.png)
#### 선택지 추가
```python
encounter = Encounter(씬 넘버)
```
* 씬넘버는 정수형을 입력받습니다.

#### 대답 추가
```python
encounter.addSelect("질문 대답", "조건 이름",조건의 증가치)
```
* 질문 대답과 조건 이름 모두 문자형을 입력 받습니다
* 조건 이름은 기본적으로 0 값을 가지게 되며, 실제로 버튼이 눌렸을경우 증가치만큼 증가합니다.

#### 마무리
```python
encounterDict[씬 넘버] = encounter
```
* 씬 넘버는 정수형이고, 반드시 선택지를 추가했을때의 씬넘버와 같아야 합니다.

#### 참고사항
* **씬넘버는 0부터 시작됩니다**
* 선택지에 추가질문이 출력되지 않기에, 이전 씬에서 관련 이야기를 두는것을 추천합니다.
* 선택지가 삼입된 씬은 출력되지 않습니다. 해당씬은 빈씬으로 두는것을 추천합니다.
* 선택지의 도착씬은 겹쳐도 문제가 없지만, 출발씬은 겹칠경우 가장 나중에 등록한 정보만 등록됩니다.

### 분기점 설정
#### 분기점 시작
```python
branch = Branch(출발 씬 넘버)
```
* 출발 씬넘버는 정수형을 입력 받습니다.
* 출발씬을 출력하기 이전에 선택지에서 설정한 조건의 값이 조건상태보다 크거나 같을경우 씬을 강제로 도착 씬으로 옮깁니다


#### 분기점 추가
```python
branch.addBranch(도착 씬 넘버,"조건 이름",조건 상태)
```
* 도착 씬넘버, 조건상태는 정수형을, 조건이름은 문자열을 입력 받습니다.
* 사용된 조건이름은 반드시 선택지설정에서 미리 설정되어 있어야 합니다.
* 만약 여러개의 조건이 만족된다면, 그 중 가장 처음에 등록된 분기점 설정을 따릅니다

#### 마무리
```python
branchDict[출발 씬 넘버] = branch
```
* 도착 씬넘버는 정수를 입력 받습니다.
* 반드시 분기점을 추가했을때의 출발 씬 넘버와 같아야 합니다.

### 음성과 이미지 경로 설정
* 기본 이미지 경로는 imageFolder 함수에서, 기본 음성 경로는 voiceFolder 함수에서 교체할수있습니다
* 대화창, 버튼, 이름창의 이름을 바꾸고싶다면 해당하는 Path 함수를 설정해주세요

### 타이틀과 시작화면 설정
```python
root.title("프로그램 이름")
mainScene("시작화면 이미지")
```
* 따로 설정해주지 않는다면 "tk"로 출력됩니다.
* 시작화면은 반드시 설정해주세요

### 플로우차트
![diagram](https://cloud.githubusercontent.com/assets/15938440/25658869/007f541e-3040-11e7-9c4c-36fae45f933f.png)


## 라이센스
MIT License

## 기타
* 프로젝트에 관한 질문은 [메일](notonalcyone@gmail.com)로 부탁드립니다.
* 예시의 이미지와 음성은 [유라](https://www.facebook.com/Astralsoo)님이 수고해주셨습니다.
