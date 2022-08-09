N,M=map(int,input().split())
metrix_=[list(map(int,input().split())) for _ in range(N)]

T=int(input())
#list 써서 접근했는데 계속 시간초과 떠서
#다른 분꺼 보니까 int로 접근하셨길래 
#보고 바꿨더니 바로 통과...
for _ in range(T):
    sum=0   
    i,j,x,y=map(int,input().split())
    for z in range(i-1,x):
        
        for e in range(j-1,y):
            sum+=(metrix_[z][e])
    print(sum)        