c = int(input())
visited = [0] * (c + 1)
n = int(input())
graph = [[] for i in range(c + 1)]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]


def dfs(v):
    visited[v] = 1
    for g in graph[v]:
        if visited[g] == 0:
            dfs(g)


dfs(1)
print(sum(visited) - 1)
