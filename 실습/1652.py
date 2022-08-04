N=int(input())
metrix_=[list(input()) for _ in range(N)]
yeol=0
hang=0
if N!=0:
    for n in range(N):
        for i in range(N-1):
            if metrix_[n][i] !='X'and metrix_[n][i+1]!='X':
                hang+=1
                break
    for i in range(N):
        for n in range(N-1):
            if metrix_[n][i]!='X' and metrix_[n+1][i]!='X':
                yeol+=1
                break
else: 
    hang=0
    yeol=0            
print(hang,yeol)                