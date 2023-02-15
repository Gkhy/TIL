M, n = map(int, input().split())
a = [0, 0]
dir = "e"
count = 0
for i in range(n):
    d, v = input().split()
    v = int(v)
    if d == "MOVE":
        if dir == "e" and 0 <= a[0] + v <= M:
            a[0] = a[0] + v
        elif dir == "w" and 0 <= a[0] - v <= M:
            a[0] = a[0] - v
        elif dir == "s" and 0 <= a[1] - v <= M:
            a[1] = a[1] - v
        elif dir == "n" and 0 <= a[1] + v <= M:
            a[1] = a[1] + v
        else:
            print("-1")
            break
    elif d == "TURN":
        if v == 0:
            if dir == "e":
                dir = "n"
            elif dir == "w":
                dir = "s"
            elif dir == "s":
                dir = "e"
            elif dir == "n":
                dir = "w"
        if v == 1:
            if dir == "e":
                dir = "s"
            elif dir == "w":
                dir = "n"
            elif dir == "s":
                dir = "w"
            elif dir == "n":
                dir = "e"
    count += 1
if count == n:
    for i in a:
        print(i, end=" ")
