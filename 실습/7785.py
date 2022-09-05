n=int(input())
li_=[]
dic_={}
for _ in range(n):
    a,b=input().split()
    dic_[a]=b
for key in dic_:
    if dic_[key]=='enter':
        li_.append(key)
li_.sort(reverse=1)
for i in range(len(li_)):
    print(li_[i])            