def creater(x):
    a=x
    for _ in str(x):
        a+=int(_)

    return a

li_=[]
for i in range(1,10000):
    li_.append(creater(i))
for j in range(1,10001):
   if j not in li_:
    print(j)    

