#4 2
#2
#3 1
#2
#4 2
a,b=map(int,input().split())
answer='YES'
for _ in range(b):
    n=int(input())
    list_=list(map(int,input().split()))
    for i in range(1,n):#1
        if list_[i-1]< list_[i]:
            answer='NO'
            break
    if answer=='NO':
        break
print(answer)    

