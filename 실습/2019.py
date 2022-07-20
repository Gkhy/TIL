import sys
sys.stdin=open('2019input.txt','r')

T=int(input())
#2**n
for t in range(T+1):
    a=2**t
    print(a,end=' ')
