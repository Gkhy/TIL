
import sys
sys.stdin = open("1284input.txt", "r")
T=int(input())
for t in range(T):
    P,Q,R,S,W=map(int,input().split())
    A=W*P
    if W<=R:
        B=Q
    else:
        B= Q+(W-R)*S
    if A>=B:
        C=B
    elif A<B:
        C=A
    print(f'#{t+1} {C}')            