import sys
sys.stdin = open("1926input.txt", "r")
#3 6 9 나올때마다 -넣어야함 두번은 --이다
#str으로 접근하면 반복에 용이할것
#print(end=" ")
#cnt에 들어가는 숫자만큼 박수
T=int(input())
S=['3','6','9']

for i in range(T):
    i=str(i)
    cnt=0
    for i1 in i:
        if i1 in S:
            cnt+=1
    if cnt==0:
        print(i,end=' ')        
    else:
        print(cnt*'-',end=' ')
   
i=str(12)
b=i.split(',')
print(b)

