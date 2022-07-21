import sys
sys.stdin = open("1926input.txt", "r")

T=int(input())
S=['3','6','9']

for i in range(1,T+1):
    i=str(i)
    cnt=0
    for i1 in i:
        if i1 in S:
            cnt+=1
    if cnt==0:
        print(i,end=' ')        
    else:
        print(cnt*'-',end=' ')
   



