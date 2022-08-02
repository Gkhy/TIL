T=int(input())
import heapq
heap=[]
heapq.heapify(heap)
list_=[]

for i in range(T):
    a=int(input())
    heapq.heappush(heap,a)
for i in heap:
    if i>=0:
        list_.append(i)
    else:
        list_.append(-i)
print(list_)
print(heap)               