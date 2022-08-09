T=int(input())
for _ in range(T):
    S=int(input())
    n=int(input())
    for i in range(n):
        a,b=map(int,input().split())
        S+=a*b
    print(S)    