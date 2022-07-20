#import sys
#sys.stdin = open("1933input.txt", "r")
#ex)약수는 나눴을때 나머지가 0이 나와야하고 약수는 자기자신~1까지 가능하다.
#for 문으로 
T=int(input())
for t in range(1,T+1):
    a=T%t
    if a==0:
        print(t,end=" ")
