T=int(input())
N=int(input())
count=0
for i in range(N):
    a,b=map(int,input().split())
    count+=(a*b)
if count==T:
    print('Yes')
else:
    print('No')        
