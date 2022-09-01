T=int(input())
for _ in range(T):
    n,s=input().split()
    n=int(n)-1
    a=s[:n]
    b=s[n+1:]
    s=a+b

    print(s)    

