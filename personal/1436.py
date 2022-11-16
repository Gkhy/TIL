n = int(input())
cnt = 0
N = 0
while True:
    if "666" in str(N):
        cnt += 1
    if cnt == n:
        print(N)
        break
    N += 1
