T=int(input())
for _ in range(T):
    a,b=input().split()
    la=len(a)
    lb=len(b)
    li1=[]
    li2=[]
    if la!=lb:
        print(f'{a} & {b} are NOT anagrams.')
    else: 
        for i in range(la):
            li1.append(ord(a[i]))
            li2.append(ord(b[i]))
        ans1=sum(li1)
        ans2=sum(li2)
        if ans1==ans2:
            print(f'{a} & {b} are anagrams.')
        else:
            print(f'{a} & {b} are NOT anagrams.')         
            
