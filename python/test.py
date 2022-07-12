from re import S


numbers = [0, 20, 100]
max=0
for i in numbers :
    if max < i :
        max=i
numbers.remove(max)
s=0
for t in numbers :
    if s < t :
        s= t
print(s)