#15)
b=-1
word=list(input())
for i in word :
    b+=1
    if i in 'a':
        break
else:
    print(-1)
print(b)

