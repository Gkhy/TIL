n,m=map(int,input().split())
dic_={}
c=0
li_=[]
for i in range(n):
    a=input()
    if a not in dic_:
        dic_[a]=1
for j in range(m):
    b=input()
    if b not in dic_:
        dic_[b]=1
    else:
        dic_[b]+=1 
for key,value in dic_.items():
    if value>=2:
        c+=1
        li_.append(key)
li_.sort()        
b="\n".join(li_)        
print(c)
print(b)                          