## git test comparing consequence

----

​	비교군 총 네가지

1. remote에 만든 내용을 clone 해서 desktop에 복제 ,

​	그 후, remote에 새 파일 작성, 동시에 local에 새 파일 작성(fast-forwards) (수업에서 했던 것 복습)

​	---> 결과적으로 local에 만들었던 repository가 push되지 않고 에러메세지 뜸, 거기서 보면 git pull 해서 local에서 동기화부터 하라고 	함--> pull해서 동기화 후엔 '자동으로' merge됨----> 그 후에 add 나 commit은 할 필요 없었음---> 바로 push

 	---->결론적으로, local에서 생성된 파일과 remote에서 생성된 파일 모두 양쪽에 서로 저장할 수 있었음

​	경험상, remote에는 해당 버전이 없고 local에만 추가되거나 수정될 경우엔 아무 문제 없이 remote에 올라가기에

​	반대로 loca은 이전 버전, remote에만 add file을 한 후 새 버전을 만들면 어떻게 될지 실험해봄  

 	2. remote에 만든 내용을 clone한 후  , github에서 remote 버전에만 새 파일을 생성, 그 다음 clone한 이전버전을 local에서 remote로 push하려함

  	마찬가지로 에러메세지 뜸 이번에도 git pull 하라고 함---> 했음---> 그 후  차이점: 이번엔 auto merge가 아니라 updating이라고 뜸

 	----> 결론적으로, local에 없고 remote에만 존재하던 파일이 양쪽에 모두 생성되고 같은 버전 공유

 	3. 이전 버전을 가지고 둘 다 (원격, 로컬) 같은 파일의 같은 부분을 수정한 뒤 push하면 내용 수정요청이 뜨기때문에, 양쪽을 같은 버전으로 두고 local의 같은 부분을 수정해봄--->그냥 업데이트로 인식 잘 올라감
 	4. 이번엔 양 쪽 다 수정해 봄---> 역시 pull 요청 뜸---> 1번과 같이 자동 merge시도는 했으나 실패함, 같은 브랜치인데도 merge요청 나옴---> 일단 remote에 있는 내용을 밑으로 내려 위치를 수정해봄---> 새버전 생성--->push 성공

---

🧩결론: remote에는 local에서 보내는 버전이 자신보다 현재의 자신의 버전이거나 그것을 포함하고 있는 이후의 버전이여야 함 

안그러면 pull 요구함

