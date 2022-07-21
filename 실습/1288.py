import sys
sys.stdin=open('1288input.txt','r')
T=int(input())
for a in range(1,T+1):
    I=int(input())
    cnt=0
    set1=set()
    while len(set1)!=10:
        cnt+=1
        b=I*cnt
        for i in str(b):
            set1.add(i)

    
    print(f'#{a} {b}')


