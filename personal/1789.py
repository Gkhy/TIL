n = int(input())
a = 0
b = 0
while b < n:
    a += 1
    b += a
if b > n:
    a -= 1
    b -= a
print(a)
