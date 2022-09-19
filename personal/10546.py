import sys
N=int(sys.stdin.readline())
st={}
ed={}

for i in range(N):
    n=sys.stdin.readline().strip()
    if n in st:
        st[n]+=1
    else:
        st[n]=1

for _ in range(N-1):
    n=sys.stdin.readline().strip()
    if n in ed:
        ed[n]+=1
    else:
        ed[n]=1
for i in st:
    if i not in ed:
        print(i)
        break
    elif st[i] !=ed[i]:
        print(i)
        break                

