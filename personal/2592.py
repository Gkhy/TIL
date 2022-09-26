a=0
dic={}
for i in range(10):
    b=int(input())
    a+=b
    if b not in dic:
        dic[b]=1
    else:
        dic[b]+=1
c=max(dic,key=dic.get)
print(int(a/10))
print(c)                    