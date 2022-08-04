T=int(input())
list_=[1,0,0]

for i in range(T):
    ca,cb=map(int,input().split())
    if list_[ca-1]==1:
        list_[ca-1]=0
        list_[cb-1]=1
    if list_[cb-1]==1:
        list_[cb-1]=0
        list_[ca-1]=1


print(list_)    
for i in range(3):
    if list_[i]==1:
        print(i+1)
   