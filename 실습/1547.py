T=int(input())
list_=[1,2,3]

for i in range(T):
    a,b=map(int,input().split())
    c=list_.index(a)
    d=list_.index(b)
    list_[c],list_[d]=list_[d],list_[c]
print(list_[0])
   