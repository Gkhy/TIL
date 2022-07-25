시퀀스Vs컬렉션 메소드
# 시퀀스
문자열(string)
## 문자열 탐색
- s.find(x) x의 첫번째 위치를 반환함, 없으면 -1

vs

- s.index(x) x의 첫번째 위치를 반환, 없으면 오류 발생
## 문자열변경
- s.replace(old,new[,count])
count는 해당 숫자만큼 반복한다는 의미
바꿀 대상을 새로운 글자로 바꿔줌

- s.strip([chars])공백이나 특정 문자 제거

strip lstrip rstrip

문자 지정x--> 공백 제거

s.split(sep=None,maxsplit=-1)
문자열을 특정 단위로 나눈뒤 리스트로 반환

'separator'.join([iterable])

반복가능한 컨테이너 요소들을 구분자로 합쳐
문자열 반환

## 리스트
- L.append(x):리스트의 마지막에 항목 x를 추가
- L.insert(i,x): 인덱스 i에 항목 x를 삽입
- L.remove(x): 리스트 최좌측의 x항목을 삭제 없다면 에러
- L.pop(): 가장 오른쪽 항목 반환 후 삭제
- L.pop(i): i에 있는 항목을 반환 후 삭제
- L.extend(m): 순회형 m의 모든 항목이 리스트 끝에 +됨
- L.reserve(): 거꾸로 정렬
- L.index(x,start,end): 가장 앞의 x 인덱스 반환
- L.sort(): 리스트 정렬
- L.count(x): 리스트에서 x가 몇개 있는지 반환
- L.clear():모든 항목 삭제

# 컬렉션
## 세트
s.copy():얕은 복사본이 반환

s.add(x):x가 없다면 추가

s.pop(): 랜덤 반환 후 해당 항목 삭제 비어있을 경우는 에러

s.remove(x):항목 x를 삭제 

s.discard(x):x가 있는 경우 x를 삭제

s.update(t):세트 t에 있는 모든 항목 중 s에 없는 것들만 s에추가해줌

s.clear():모든 항목 제거

## 딕셔너리

d.clear() 모두 삭제

d.keys() : 모든 키 뷰 반환

d.values() 모든 값을 담은 뷰 반환

d.items() 모든 키-값 쌍 담은 뷰 반환

d.get(k) 키 k의값을 반환 없으면 none

d.get(k,v) 키k의 값을 반환 없으면 v 반환

d.pop(k) 키k값 반환 k인 항목을 삭제, 없으면 에러

d.pop(k,v) 키k값 반환 키k항목을 삭제, 없으면 v반환

d.update([other]) d를 other 로 덮어씀



