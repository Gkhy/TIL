T=int(input())
for _ in range(T):
    r,e,c=map(int,input().split())
    if r<(e-c):
        print('advertise')
    else:
        if r==e-c:
            print('does not matter')
        else:
            print('do not advertise')    
