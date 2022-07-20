import sys
sys.stdin = open("2050input.txt", "r")

T=list (input())
for t in range(len(T)):
    print(ord(T[t])-64, end=' ')