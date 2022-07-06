# git 정리

# git: 분산버전 관리 시스템

### 명령어 정리

저장소 처음 만들때
$ git init 로컬저장소 탄생

버전을 기록할 때
$ git add ( ., .., 파일명, 폴더명) 특정 파일 폴더를 로컬저장소에 추가
$ git commit -m '커밋메시지'

추가적으로 git commit만 친다음 길게 줄나눠서 메시지 치는 방식도 있음

상태 확인할 때
$ git status : 1통, 2통, 파일 상태 확인용
$ git log : 커밋 확인

+( -1, --oneline, -2 --oneline )등의 변형이 존재함

• pwd (print working directory) : 현재 디렉토리 출력
• cd 디렉토리이름(change directory) : 디렉토리 이동
• . : 현재 디렉토리, .. : 상위 디렉토리
• ls (list) : 목록
• mkdir (make directory) : 디렉토리 생성
• touch : 파일 생성
• rm 파일명: 파일 삭제하기
• rm –r 폴더명 : 폴더 삭제하기

### config 사용자 정보 추가 및 확인 가능

- git config -global user.name "username"

- git config -global user.email "email"



### 설정확인법

- git config -I

- git config -global-I

- git config user.name

# 🥞밑에 추가적으로 더 있음

----

git 파일 상태는 

- tracked: 이전부터 버전으로 관리되는 파일

  - modified : 이전 버전과 달리 수정된 상태를 뜻함

  - staged: 커밋되기 전 상태 staging area에 있음

  - committed: 커밋 완료 Repository에 위치 

- Untracked: 버전으로 관리된 적 없는 파일(new 파일)

로 나눠진다.

또한 commited되고 로컬저장소에 저장된 버전들을

원격저장소(Remote)에 보내거나(push) 또는 원격저장소에 저장된 버전들을 받아올 수 있다.(pull)

당연히 원격저장소가 존재해야 하기 때문에 먼저 원격저장소를 만들고(수업에서는 github을 이용)

그 후에 로컬저장소와 연결해주는 과정이 필요하다.

- ($ git remote add origin 주소/저장소이름.git)

​	->깃 원격저장소에 추가해라 origin 주소/저장소이름.git

- $ git push 원격저장소이름 브랜치이름

​	-> 이것은 원격저장소로 로컬저장소의 버전을 올림

​		**(단순히 파일,폴더를 올리는 것이 아님!) **

- $ git pull 원격 저장소이름 브랜치이름

​	-> 원격저장소에서 변경된 것들을 받아오고 이력 병합

## .gitignore 파일을 이용해서 버전 관리에서무시하는 방법

Git 저장소에 .gitignore 파일을 생성하고

아래 내용 작성

- 파일의 경우,그냥 이름 or 들어가 있는 폴더명/이름

- 디렉토리의 경우:/폴더명

- 특정 확장자의 경우 *. 확장자명 

- 예외 처리법: !이름.확장자명

***이미 커밋된 경우 삭제하지 않으면 적용되지 않음***