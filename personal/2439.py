T=int(input())
for i in range(1,T+1):
    for k in range(T-i):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print()            
