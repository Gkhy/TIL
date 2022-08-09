T=int(input())
for _ in range(T):
    a=0
    N,M=map(int,input().split())
    
    for i in range(N,M+1):
        a+=str(i).count('0')
    print(a)    
