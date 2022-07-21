import sys
sys.stdin = open("1989input.txt", "r")
T=int(input())

for t in range(1,T+1):
    A=input()
    for a in A:
        if A==A[::-1]:
            e=1
        else: e=0
    print(f"#{t} {e}")        
    
        