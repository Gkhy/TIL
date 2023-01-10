import sys

input = sys.stdin.readline
n, v = map(int, input().split())
graph = {m: [] for m in range(1, n + 1)}
visited = [0] * (n + 1)
line = 0
for i in range(v):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
for j in range(1, n + 1):
    if visited[j] == 0:
        visited[j] = 1
        stack = [j]
        line += 1
        while stack:
            now = stack.pop()
            for c in graph[now]:
                if visited[c] == 0:
                    visited[c] = 1
                    stack.append(c)
print(line)
