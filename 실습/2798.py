N,M=map(int,input().split())
total=0
max_=0
list_=list(map(int,input().split()))
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            total=list_[i]+list_[j]+list_[k]
            if max_<=total<=M:
                max_=total
print(max_)                 

