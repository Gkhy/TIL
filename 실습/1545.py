import sys
sys.stdin = open("Sampleinput.txt", "r")
T=int(input())
a=[]
for t in range(0,T+1):
    a.append(t)
a.reverse()
for t in a:
    print(t,end=' ')

