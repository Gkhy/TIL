# CSS 기본 스타일

## 크기의 단위
- 픽셀(px)

    - 모니터 화소, 픽셀의 크기 변화x
    - --->고정적

- 퍼센트(%)

    - 차지하는 비율,
    - 가변적임

- em
    - 상속 영향 O
    - 위,부모 요소에 배수단위인 사이즈임

- rem
    - 부모요소, 위 요소의 영향x
    - 최상위 요소 사이즈 기준 배수로 사이즈를 가짐

- 뷰포트
    - 웹 사이트 크기를 기준으로 상대적인 사이즈
    - 변동o

## 선택자

- 기본 선택자
    - 전체

     선택자, 요소 선택자
    - 클래스

    선택자, 아이디 선택자, 속성 선택자

## CSS 적용 우선순위

1. !important
2. 우선 순위:
인라인>id>class 
3. CSS 파일 로딩순서

## CSS 상속
- 상속 되는 것
안되는 것이 존재

## CSS Box model

- CSS 원칙
모든 요소는 기본적으로 네모(박스모델)
    -  위->아래
    - 왼쪽->오른쪽

- 하나의 박스를 이루는 것

margin
(상자 바깥의 여백, 배경색 지정에 영향x)



border
(테두리)



padding
(내부 여백, 배경색, 이미지 적용o)



content
(글, 이미지 등 내용)

## 박스 사이즈

- box-sizing은 content box의 크기 

- border까지 포함한 너비는 border-box

## css display

- 크기와 배치에 영향을 줌

### 대표적 디스플레이?

- block

    - 줄바꿈o

    - 화면 크기 전체의 가로 크기

    - 블록 내부에 인라인 요소 포함 가능

- inline

    - 줄 바꿈x
    - content 너비만큼의 가로 크기
    - width,height,margin-top,margin-bottom 지정 x
    - 상하여백은
    line-height o

    






