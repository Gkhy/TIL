N=int(input())
li_=[]
li=[[] for _ in range(10)]
for _ in range(N):
    a,b=map(int,input().split())
    li[a-1].append(b)
cnt=0    
for i in range(10):
    for k in range(len(li[i])-1):
        if li[i][k]!= li[i][k+1]:
            cnt+=1       
print(cnt)