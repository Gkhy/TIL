N = int(input())
ta, tb = map(int, input().split())
V = int(input())
p = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
stack = []
res = [0] * (N + 1)
for v in range(V):
    a, b = map(int, input().split())
    p[a] += [b]
    p[b] += [a]
visited[ta] = 1
for i in p[ta]:
    if visited[i] == 0:
        visited[i] = 1
        stack.append(i)
        res[i] = 1
        while stack:
            now = stack.pop()
            for adj in p[now]:
                if visited[adj] == 0:
                    visited[adj] = 1
                    stack.append(adj)
                    res[adj] = res[now] + 1
if res[tb] == 0:
    print(-1)
else:
    print(res[tb])
