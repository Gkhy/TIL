import sys
N=int(sys.stdin.readline().strip())
dic={}
a=0
for _ in range(N):
    n=sys.stdin.readline().strip()
    if n=='ENTER':
        dic.clear()
    elif n not in dic:
        dic[n]=1
        a+=1
print(a)        
