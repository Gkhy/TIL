N=int(input())
metrix_=[list(input()) for _ in range(N)]
yeol=0
hang=0

for n in range(N):
    cnt=0
    for i in range(N):
        if metrix_[n][i]=='.':
            cnt+=1
        else:
            if cnt>=2:
                hang+=1
            
            cnt=0
    if cnt>=2:
        hang+=1
    cnt=0           

for i in range(N):
    cnt=0
    for n in range(N):
        if metrix_[n][i]=='.':
            cnt+=1
        else:
            if cnt>=2:
                yeol+=1
            cnt=0
    if cnt>=2:
        yeol+=1
    cnt=0                        

print(hang,yeol)                