N,M=map(int,input().split())
li=[[0]*(N+1) for _ in range(N+1)]
graph=[[]for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    li[a][b]=1
    graph[a].append(b)

print(li)
print(graph)