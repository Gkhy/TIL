N=int(input())

while True:
    if len(str(N))== str(N).count('4')+str(N).count('7'):
        print(N)
        break
    N-=1