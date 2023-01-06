행, 열 = map(int, input().split())
parking = []
for _ in range(행):
    parking.append(input())
cb0 = 0
cb1 = 0
cb2 = 0
cb3 = 0
cb4 = 0
for ㅎ in range(행):
    for ㅇ in range(열):
        if ㅎ + 1 == 행 or ㅇ + 1 == 열:
            break
        a = parking[ㅎ][ㅇ]
        b = parking[ㅎ + 1][ㅇ]
        c = parking[ㅎ][ㅇ + 1]
        d = parking[ㅎ + 1][ㅇ + 1]
        one = a + b + c + d
        if "#" in one:
            continue
        else:
            car = one.count("X")
            if car == 0:
                cb0 += 1
            elif car == 1:
                cb1 += 1
            elif car == 2:
                cb2 += 1
            elif car == 3:
                cb3 += 1
            elif car == 4:
                cb4 += 1
print(cb0, cb1, cb2, cb3, cb4, sep="\n")
