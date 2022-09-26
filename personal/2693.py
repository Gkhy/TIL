N=int(input())
for i in range(N):
    li=list(map(int,input().split()))
    a=max(li)
    li.remove(a)
    b=max(li)
    li.remove(b)
    c=max(li)

    print(c)        