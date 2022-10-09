N = int(input())
for _ in range(N):
    m, n = map(int, input().split())
    a = [input().split() for _ in range(m)]

    r = 0
    for i in range(n):
        b = m - 1
        for j in range(m - 1, -1, -1):
            if a[j][i] == "1":
                r += b - j
                b -= 1
    print(r)
