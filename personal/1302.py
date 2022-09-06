N=int(input())
dic_={}
li_=[]
for _ in range(N):
    a=input()
    if a not in dic_:
        dic_[a]=1
    elif a in dic_:
        dic_[a]+=1
for i in dic_:
    if dic_[i]==max(dic_.values()):
        li_.append(i)
li_.sort()
print(li_[0])                