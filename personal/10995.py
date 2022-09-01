T=int(input())
for i in range(1,T+1):
    if i%2==0:
        for j in range(1,T+1):
            print(' *',end='')
    else:
        for j in range(1,T+1):
            print('* ',end='')
    print()        
