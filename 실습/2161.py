from collections import deque
T=int(input())
queue= deque(range(1,T+1))
list_=[]

while len(queue)>1:
    add_=0
    add_=queue.popleft()
    list_.append(add_)
    queue.append(queue.popleft())
print(*list_,*queue)    
