import sys
input = sys.stdin.readline

N,M=map(int,input().split())
a=True
for _ in range(M):
    T=int(input())
    Li_=list(map(int,input().split()))
    for i in range(T-1):
        if Li_[i]<Li_[i+1]:
            a=False
            break               
    if not a:
        break                 
print('Yes'if a else 'No')       

