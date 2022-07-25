# 파이썬 심화

## List Comprehension

[<expression> for <변수> in <interable>]
[<expression> for <변수> in <iterable> if <조건식>]

## Dictionary Comprehension

{key: value for <변수> in <iterable>}
{key: value for <변수> in <iterable> if <조건식>}

## lambda[parameter]
람다함수란 이름없는 함수=익명함수

return문 못가짐

간편 조건문을 제외하고 조건문 반복문 못가짐

함수 정의 후 사용보다 빠르고 간결

def못 쓰는 곳에서도 사용가능

## filter
filter(function,iterable)
순회가능한 데이터구조의 모든 요소에
함수 적용
그 중 결과가
True인 것들만 filter object로 반환

## pip 파이썬 패키지 관리자
pip install ~~ 패키지 설치

pip uninstall~~ 패키지 삭제

pip list 설치된 패키지 리스트 확인

pip show SomePackage 위에 보다 더 상세하게 확인 가능

pip freeze 설치된 패키지의 비슷한 목록을 만들지만 
인스톨에 사용하는 방식으로 출력
해당하는 목록을 requirements.txt로 만들어 관리

pip install -r requirements.txt

목록에 적혀 있는 것들 다운

## 가상환경 
가상환경 생성
python -m venv<폴더명>

비활성화는 deactivate 명령어 사용

source venv/Scripts/activate
활성화/비활성화
