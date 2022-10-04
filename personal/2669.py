metrix = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for i in range(y1, y2):
            metrix[j][i] = 1
answer = 0
for i in range(101):
    for j in range(101):
        if metrix[i][j] == 1:
            answer += 1
print(answer)
