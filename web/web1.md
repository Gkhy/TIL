# 웹 사이트 구성

- (HTML(구조,뼈대)+CSS(장식)+javascript
(동작))

## HTML(hyper text Markup Language)

- 하이퍼링크를 통해서 다른 문서들로 이동이 가능한 마크업 랭귀지(데이터,문서의 구조를 설계하는 언어)

- .html의 형식을 띄고있음

- 웹 페이지를 설계하기 위한 언어(프로그래밍 언어는x)

### 기본 구조
```

<!DOCTYpe html>
<html>
<head>
    <meta>
    <title>
</head>
<body>

</body>
</html>
```

- html
html 문서의 시작

- head
컨텐츠x 양식으로 존재하는 것들, 일종의 부품으로 생각됨

    - title
    - meta
    - link
    - script
    - style

- body
컨텐츠o

### element(요소)

- 태그+컨텐츠

### 속성(attribute)

- 태그에 부가적인 정보들 추가 가능
- 요소의 시작 태그에 작성

-태그와 상관없이 사용가능한 HTML Global Attribute도 있음

#### HTML Global Attribute

- id
- Class
- title
- data-*
- tabindex

### 렌더링

- HTML을 사용자가 보는 웹사이트로 바꾸는 것

### DOM트리

- 텍스트로 이루어진 HTML에 대한 모델
- 렌더링을 하기 위함

### 인라인/블록

- 블록-div
한 줄 전체가 적용
- 인라인-span
글자처럼 적용


## CSS

- 스타일을 지정하기위함(HTML은 뼈대,CSS는 살)

- 스타일을 적용할 HTML 요소를 선택

- 중괄호 안에 속성+값을 넣는다

    - 속성은 어떤 기능을 선택할지이고

    - 값은 그 기능의 할당시킬 값을 의미

### CSS 정의 방법

- 인라인

적용할 태그 앞부분에 style 속성+값을 입력

- 내부참조
HEAD 태그 내에 STYLE 속성을 넣고 사용

- 외부참조
CSS파일을 HEAD 태그내에 LINK를 사용해 가져와서 사용

### 기초 선택자

- 요소 선택자
태그를 직접 선택

- Class 선택자
.로 시작하며 , 해당 클래스의 항목 선택

- id 선택자
#로 시작, 아이디가 적용된 항목 선택

- 일반적으로 한 문서당 한번만 사용함
여러번 사용해도 되지만 한번만 사용하는걸 추천함 