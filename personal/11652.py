N=int(input())
dic_={}
for _ in range(N):
    a=int(input())
    if a not in dic_:
        dic_[a]=1
    elif a in dic_:
        dic_[a]+=1
c=max(dic_.values())




                    