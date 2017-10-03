# Tkinter Visualnovel Framework

GUI로 tkinter를, 음악부분에 pygame을 사용한 비주얼 노벨 프레임워크입니다.

![image](https://user-images.githubusercontent.com/15938440/31112802-cc4c35e8-a850-11e7-977d-bd42acaa39f1.png)

## 사용 언어및 라이브러리

* Python 3
* tkinter
* [pygame](https://www.pygame.org/)

## 사용법

스크립트를 엑셀로 작성하고, Main.py를 실행시켜 빌드합니다.  
기타 수치등은 Stat.py에서 설정합니다.

![git](https://user-images.githubusercontent.com/15938440/31081520-1cd9a354-a7c7-11e7-99ca-d19f160c5822.png)

* DATA.xlsx 를 예제로 첨부했습니다.


### 엑셀시트 작성법
#### 씬넘버
0부터 시작하는, 씬의 번호입니다. 순서대로 출력됩니다.
#### 씬타입
씬의 종류입니다. Scene는 일반 씬, Encounter는 선택지 씬 입니다.
#### BGM
씬에서 재생되는 음악입니다. 파일명을 입력 해주세요.
#### 인카운터 (선택지)
![sample2](https://cloud.githubusercontent.com/assets/15938440/23822344/e1d831b4-068e-11e7-9b7c-c0ea917d8600.png)
```json
[{"select":"질문1","parameter":"질문1 값", "factor":"질문1 값 변동치"}, {"select": "질문2", "parameter": "질문2 값", "factor": "질문2 값 변동치"}, { "select": "질문 3", "parameter": "질문3 값", "factor": "질문3 값 변동치"}]
```
#### 씬_배경
씬의 뒷 배경입니다. 파일명을 입력 해주세요.  
이하 씬_ 으로 시작되는 모든 구성은 씬타입이 Scene일때만 사용됩니다.
#### 씬_화자
씬에서 말하는 사람을 나타냅니다. 입력하지 않으면 창이 출력되지 않습니다.
#### 씬_대화
씬의 대화를 나타냅니다. 입력하지 않으면 창이 출력되지 않습니다.
#### 씬_음성
해당 씬에서 사용될 음성을 나타냅니다. 입력하지 않으면 음성이 출력 되지 않습니다.
#### 씬_캐릭터
```json
[{"imagePath": "캐릭터1 파일명", "X": "캐릭터1 X좌표", "Y": "캐릭터1 Y좌표"}, {"imagePath": "캐릭터2 파일명", "X": "캐릭터2 X좌표", "Y": "캐릭터2 Y좌표"}]
```
#### branch(분기점)
```json
[{"condition":"값","conditionNum":"값조건","destination":"이동위치"}]
```
값조건은 문자열이 아닌 숫자로 작성해주세요
해당 값이 값 조건 보다 클 경우 이동위치로 씬을 이동합니다


### 추가 예정
* 수정 가능한 모든 수치를 엑셀로 관리 가능한 기능

## 라이선스
None, 맘대로 사용하세요

## 기타
* 프로젝트에 관한 질문은 [메일](notonalcyone@gmail.com)로 부탁드립니다.
* 예시로 사용된 이미지와 음성은 [김연수](https://www.facebook.com/yeonsooyura)님이 수고해주셨습니다.
