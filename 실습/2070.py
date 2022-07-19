import sys
sys.stdin = open("2070input.txt", "r")

T=int(input())

for t in range(1,T+1):
    a,b=map(int,input().split())
    if a<b:
        print("#%d <"%t)
    elif a==b:
        print("#%d ="%t)
    elif a>b:
        print("#%d >"%t)
   
