N,M=map(int,input().split())
metrix_=[list(map(int,input().split())) for _ in range(N)]

T=int(input())

for _ in range(T):
    sum=0   
    i,j,x,y=map(int,input().split())
    for z in range(i-1,x):
        
        for e in range(j-1,y):
            sum+=(metrix_[z][e])
    print(sum)        