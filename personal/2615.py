import sys

input = sys.stdin.readline

omok = [list(map(int, input().split())) for _ in range(19)]
D = [(0, 1), (1, 0), (-1, 1), (1, 1)]
for i in range(19):
    for j in range(19):
        if omok[i][j] != 0:
            target = omok[i][j]

            for a, b in D:
                cnt = 1
                nx = i + a
                ny = j + b
                while 0 <= nx < 19 and 0 <= ny < 19 and omok[nx][ny] == target:
                    cnt += 1

                    if cnt == 5:
                        if (
                            0 <= i - a < 19
                            and 0 <= j - b < 19
                            and omok[i - a][j - b] == target
                        ):
                            break
                        if (
                            0 <= nx + a < 19
                            and 0 <= ny + b < 19
                            and omok[nx + a][ny + b] == target
                        ):
                            break
                        print(target)
                        print(i + 1, j + 1)
                        sys.exit(0)
                    nx += a
                    ny += b
print(0)
