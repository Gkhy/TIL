n = int(input())
for _ in range(n):
    li = list(input().split())
    li[0] = float(li[0])
    ans = li[0]
    for l in li:
        if l == "@":
            ans = ans * 3
        elif l == "%":
            ans = ans + 5
        elif l == "#":
            ans = ans - 7
    print("%.2f" % ans)
