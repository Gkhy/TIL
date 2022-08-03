n,m=map(int,input().split())
metrix_=[list(input()) for _ in range(n)]
hang=0
yeol=0

for _ in range(n):
    if 'X' not in metrix_[_]:
        hang+=1
for i in range(m):
    cnt=0
    for _ in range(n):
        if metrix_[_][i]!='X':
            cnt+=1
    if cnt== n:
        yeol+=1
print(max(yeol,hang))