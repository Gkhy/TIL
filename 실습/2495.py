
for i in range(3):
    cnt=1
    li=[]
    S=input()
    for j in range(7):

        if S[j]==S[j+1]:
            cnt+=1
        else:
            li.append(cnt)
            cnt=1
        if j==6:
            li.append(cnt)
    a=max(li)           
    print(a)            
