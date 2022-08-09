list_=[]
for _ in range(9):
    n=int(input())
    list_.append(n)
total=sum(list_)    
for i in range(8):
    for j in range(i+1,9):
        if total-(list_[i]+list_[j])==100:
            answer1=list_[i]
            answer2=list_[j]
            break
list_.remove(answer1)
list_.remove(answer2)
list_.sort()
for _ in list_:
    print(_)

