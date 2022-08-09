T=int(input())
for _ in range(T):
    list_=list(map(int,input().split()))
    list__=list_[1:]
    gap=[]
    M=max(list__)
    m=min(list__)
    list__.sort(reverse=1)
    l=len(list__)
    for i in range(l):
        if i !=l-1 :
            gap.append(abs(list__[i]-list__[i+1]))
    lg=max(gap)
    print(f'Class {_+1}')
    print(f'Max {M}'","f' Min {m}'","f' Largest gap {lg}')


