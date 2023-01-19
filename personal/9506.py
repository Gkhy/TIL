while True:
    n = int(input())
    if n == -1:
        break
    list = []
    a = 1
    while a < n:
        if n % a == 0:
            list.append(a)
        a += 1
    if sum(list) == n:
        print(f"{n} = ", end="")
        print(*list, sep=" + ")
    else:
        print(f"{n} is NOT perfect.")
