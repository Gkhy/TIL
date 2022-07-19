import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for t in range(1,T+1):
    a, b = map(int, input().split())
    print( "#%d %d %d" % (t, a//b, a%b) )