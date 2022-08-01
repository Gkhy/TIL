T=int(input())
for _ in range(T):
    list_=[]
    answer=0
    words=input()
    for i in words:
        if i== '(':
            list_.append(i)
        else:
            if len(list_)==0:
                answer=1
                break
            list_.pop()
    if answer>0 or len(list_)>0:
        print('NO')
    else:
        print('YES')                
