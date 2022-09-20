import sys
t=int(sys.stdin.readline())
for i in range(t):
    N=int(sys.stdin.readline())
    li=set(map(int,sys.stdin.readline().strip().split()))
    M=int(sys.stdin.readline())
    li2=list(map(int,sys.stdin.readline().strip().split()))   
    for _ in li2:
        if _ in li:
            print(1)
        else:
            print(0)    
