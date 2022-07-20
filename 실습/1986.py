import sys
sys.stdin = open("1986input.txt", "r")
T=int(input())
for i in range(1,T+1):
    n=int(input())
    cnt=0
    for N in range(1,n+1):
        if N%2==0:
            cnt-=N
        else:
            cnt+=N
    print('#%d'%i, cnt)   





