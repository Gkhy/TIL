### 함수란?

특정 기능을 하는 코드의 묶음

사용자 함수?
- 사용자가 만들 수 있음
함수를 사용하면 반복문이나 조건문을 사용하는 것 보다 더욱 간단하게 결과 도출 가능

함수는 
- 1.선언,호출
- 2.입력
- 3.범위
- 4.결과값

으로 나눠짐

함수는 return한 뒤 실행이 종료됨, 반드시 값 한가지만 return함 명시적 return이 없더라도 None이 반환된다.
,을 사용해 튜플로 반환시킬 수 있다.

parameter, Argument
각각 내부에서 사용되는 parameter과 호출할 때 사용되는 Argument로 나뉜다.

positional arguments:위치에 따라 전달됨

keyword arguments: 변수의 이름으로 전달가능

다만 keyword의 방식이 먼저 사용된 뒤에 positional을 사용할 수는 없다.

기본값을 설정해서, 정의된 것보다 더 적은 argument들로 호출 가능

다수의 argument 사용도 가능하다. 이때 argument는 튜플로 묶여서 처리됨(사용법은 parameter에 *를 붙임) 또한 딕셔너리로 묶여서 처리하는 방법도 있는데 이는 (parameter에 **를 붙힌다.)

## scope
함수는 내부에 local scope 생성

객체는 수명주기가 존재하며

built -in scope
파이썬이 실행된 이후부터 영구적

global scope
모듈이 호출된 시점 이후 혹은 인터프리터가 끝나면 끝

local scope
함수가 종료하면 끝

식별자들은 이름공간에 저장됨

local

Enclose

Global

Built in
순으로 이름을 찾아감
이는 LEGB Rule이라 불림

