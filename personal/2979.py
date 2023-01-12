a, b, c = map(int, input().split())
car = [list(map(int, input().split())) for _ in range(3)]
last = max(car[0][1], car[1][1], car[2][1])
car_leave = [0] * (last)
for ca in car:
    for i in range(ca[0], ca[1]):
        car_leave[i] += 1
sum = 0
for n in car_leave:
    if n == 1:
        sum += a
    elif n == 2:
        sum += b * 2
    elif n == 3:
        sum += c * 3
print(sum)
