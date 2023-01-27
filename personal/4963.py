import sys

sys.setrecursionlimit(100000)

dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [1, -1, 0, -1, 1, 0, 1, -1]


def dfs(y, x):
    visited[y][x] = 1
    if graph[y][x] == 1:
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < h and 0 <= nx < w:
                if visited[ny][nx] == 0 and graph[ny][nx] == 1:
                    dfs(ny, nx)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    visited = [[0] * w for _ in range(h)]
    land = 0

    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for y in range(h):
        for x in range(w):
            if graph[y][x] == 1 and visited[y][x] == 0:
                dfs(y, x)
                land += 1
    print(land)
