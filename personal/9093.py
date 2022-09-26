T=int(input())
for i in range(T):
    li=list(input().split())
    for j in li:
        print(j[::-1],end=' ')