list_=[]
for _ in range(5):
    a=int(input())
    list_.append(a)
print(int(sum(list_)/5))
list_.sort(reverse=1)
print(list_[2])    