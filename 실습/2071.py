import sys
sys.stdin = open("2071input.txt", "r")
T=int(input())
for t in range(1,T+1):
    a=map(int,input().split())
    b=round(sum(a)/10)
    print("#%d %d" %(t,b))
