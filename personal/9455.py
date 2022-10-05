N = int(input())
for _ in range(N):
    m, n = map(int, input().split())
    a = [[input().split() for _ in range(n)] for _ in range(m)]
for i in range(n):
    for j in range(m):
        if a[j][i] == 1:
            f = m - 2 - j
