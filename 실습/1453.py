
N=int(input())
List_=list(map(int,input().split()))
set_=set()
for _ in range(N):
    
    set_.add(List_[_])
print(len(List_)-len(set_))    
