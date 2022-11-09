n = int(input())
mine = [list(input()) for _ in range(n)]
open = [list(input()) for _ in range(n)]
result = [["."] * n for _ in range(n)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, 1, -1, 1, 0, -1]
for y in range(n):
    for x in range(n):
        if mine[y][x] == "." and open[y][x] == "x":
            cnt = 0
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if mine[ny][nx] == "*":
                    cnt += 1
            result[y][x] = cnt
        if mine[y][x] == "*" and open[y][x] == "x":
            for a in range(n):
                for b in range(n):
                    if mine[a][b] == "*":
                        result[a][b] = "*"
for i in range(n):
    for j in range(n):
        print(result[i][j], end="")
    print()
