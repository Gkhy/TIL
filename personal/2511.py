A=list(map(int,input().split()))
B=list(map(int,input().split()))
wl=[]
for i in range(10):
    if A[i]>B[i]:
        wl.append('A')
    else:
        if A[i]<B[i]:
            wl.append('B') 
        else:
            wl.append('D')
print((wl.count('A'))*3+wl.count('D'),(wl.count('B'))*3+wl.count('D'))            
if wl.count('A')<wl.count('B'):
    print('B')
elif wl.count('A')>wl.count('B'):
    print('A')
else:
    if wl.count('D')==10:
        print('D')
    else:
        T=''.join(wl)
        T=T.replace('D','')
        T=list(T)
        print(T.pop())


