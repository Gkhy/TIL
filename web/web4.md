오늘 배운 거 table,form,input,label,
boottrap....

# table

<table> 태그 사용

- thead(header)
- tbody(body)
- tfoot(footer)
의 세가지로 이루어져 있음

각각의 행은 tr로 생성하고

그안 내부 칸칸은 th(thead) 나 td(나머지 두개)로 생성

모두 html 문서의 body부분에 넣어줘야함

-  colspan(세로병합), rawspan(가로병합)

- caption 제목 또는 표설명을 나타낸다.

# form

- 데이터를 서버에 제출하기 위한 태그

<form>

- 속성으로 action이 있음

- action은 데이터가 보내질 주소(url)가 입력됨

- 속성에 이 외(method....enctype...) 더 있지만 나중에 더 자세히  

# input

<input> 태그로 사용함

- 입력데이터를 받는 용

- 속성으로는

    - name: form control에 적용되는 이름. 밑에 값과 같이 보내짐, 생략x

    - value: form control이 가지는 값. 위에 이름과 같이 보내짐

    - type: 타입 지정

    - required,readonly,autofocus,autocomplete,disabled.....

# input label

- input의 편의성을 위해 존재함

<label>로 사용함

- 속성인 for을 사용하여 input의 id와 연결시킴

- 내용을 입력해 input에 대한 설명을 추가함

## input type

- text:텍스트 입력을 받음

- password: *로 가려진 비밀번호 입력을 받음

- email: 이메일을 입력받음, 물론 이메일의 형식 ....@...com <- 이런거 아니면 제출이 안됨

- number: min,max,step 속성 사용, 숫자 범위 설정하고 받음

- file: accept 속성 사용, 파일 타입 지정을 하고 받음

- 항목 중 선택: checkbox:다중 선택 가능, raido: 단일 선택만 가능

- color: 컬러 선택

- date: 날짜 선택

- hidden: 사용자 입력 받지x 보이지도 않는 input

# bootstrap

- 웹 디자인 프레임 워크, 그리드 시스템 채택

- CDN: 유저에게 가까운 서버를 통해 컨텐츠를 빠르게 전달하는 여러개의 외부 서버를 가진 시스템(링크로 가져와서 사용하면 됨)

## spacing

- margin 과 padding을 조작함

형태는 {property}{sides}-{size} 이다.

- property 자리엔 m or p가 들어감

- sides엔 t(top), b(bottom), s(start), e(end), x(x좌표범위),y(y좌표범위),blank(4방향 다 넣어줌)

- size는 rem이 기준임, 3이 1rem이고
1이 0.25 2이 0.5 
4가 1.5 5가 3
auto도 가능

- color
    - bg- (특정컬러)

    - text-(특정컬러)


- TEXT
    - text-위치(배치)

    - text-decoration-none(언더바 삭제)

    - fw-(폰트 스타일)

    - fst-(```)

- display

    576픽셀 이하는 클래스중의 x
    sm, md, lg, xl, xxl의 크기가 존재한다.

    d-{value}

    d-{breakpoint}-{value}

    특정 화면 이하나 이상에서 숨기는 것도 가능
    ex)
    d-{breakpoint}{none} d-{breakpoint}{value} 
    
    주의! 지정된 중단점보다 큰 화면에도 같이 영향을 줌!



- position
    position-(위치)-(요소정렬)
