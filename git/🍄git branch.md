# 🍄git branch

- Git Flow(협업에서의 흐름)에서 branch를 이용함

- 줄기(master, 현 시점에서의 버전 ) 하나를 두고 가지를 쳐서 각자 개발
- merge로 통합 

- HEAD 현재 있는 브랜치

## 🐌branch commands

- git branch name  브랜치 생성
-  git branch 생겨난 브랜치 목록
- git checkout name 해당 브랜치로 이동
- git checkout -b name 해당 브랜치 생성 및 이동
- git branch -d name 해당 브랜치 삭제

----

## 🦢branch merge 

- fast forward
  - master에서 수정x 그저 추가됨
  - master에서 바로 git merge
- merge commit
  - 다른 파일이 수정되어 있는 상황
  - git merge 가능

- merge commit conflict
  - 같은 파일의 같은 곳이 branch마다 다르게 되어있을 경우 충돌 발생
  - 해당 파일 눌러서 확인후 변경
  - git merge 가능

## 🦄협업 모델

1. Feature Branch Workflow
   - shared repository model(저장소 소유권 o)
2. forking workflow
   - fork & pull model(저장소 소유권 x)

----

$ git restore -- staged 파일이름.확장자

->  add를 실수로 한 파일도 다시 되돌리기 가능

$ git restore 파일이름.확장자

-> 변경사항 버리기

