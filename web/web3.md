# CSS

## CSS 포지션
- 이것이 변경되면 기준점이 변경됨.

1. static:
아무것도 안했을때 가지는 기본값

2. relative
static 기준으로 offset됨, normal flow를 따름(눈에 보기엔 위치가 변경된거 같아 보이지만 실제론x)

3. absolute
부모/조상 요소를 참조하여 움직임,
normal flow(좌상에서 시작)을 벗어나있음

4. fixed
normal flow 따르지x 뷰포트가 기준임

5. sticky
기본적으론 static이나,
일정 이상의 임계점을 넘기면 fixed로 바뀜

## CSS Layout
- 요소취합,위치 등을 제어하는 것

display,float,position,flexbox가 여기 속함

### float
박스를 왼쪽 혹은 오른쪽으로 이동시킴
ex) float:left

float:right

### FLEXBOX

- 축
    - 메인 축, 교차축
- 구성 요소
    - 컨테이너(부모요소)
    , 아이템(자식요소) 

사용시 좌->우,상->하의 normal flow에서 벗어나서
reverse사용 가능

자동적으로는 
수직정렬, 아이템들의 너비,높이,간격 동일

### FLEX 속성

- 배치 설정
    - flex-direction
    진행 방향 설정
    (row,column,
    row-reverse,column-reverse)

    - flex-wrap
    컨테이너에서 오버플로우 되었을 시에,
    메인 축의 다른 줄로 이동시킴
    (설정x시엔 nowrap임)

--->둘다 같이 사용하는 경우가 많이때문에 flex-flow라는 속성으로 동시에 사용 가능 첫번째 값이 direction 두번째값이 wrap

- 공간 배분

메인 축을 기준으로 함, 집단적으로 적용됨

- justify-content(메인축을 기준으로)
+align-content(교차축을 기준으로, 아이템이 한줄뿐이다? 변화x)
(direction에 따라 메인축이나 교차축이 바뀌기 때문에 유동적)

    - flex-start
    - flex-end
    - center
    - space-between
    - space-around
    - space-evenly

- 정렬
    - align-items
    모든 아이템을 교차축 기준으로 정렬

    - align-self
    교차축기준.위와달리 개별아이템에 적용 

    - stretch(기본)

    - flex-start
    시작부분으로 정렬
    - flex-end

    - 끝으로 정렬
    
    - center
    중간부분으로 정렬
align-item의 경우 여기서 + baseline(컨테이너 시작위치에 정렬)

+ 추가적으로

- flex-glow: 남는 부분을 아이템에 나눠줌

- order:  배치순서의 값(숫자가 크다고 앞으로 가는게 아님 적을수록 앞으로 감)