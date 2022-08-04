dh=list(map(int,input().split()))
standard=[1,1,2,2,2,8]
cnt=[]
for i in range(6):
    answer=standard[i]-dh[i]
    print(answer,end=" ") 

