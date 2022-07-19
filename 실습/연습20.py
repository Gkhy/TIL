a=(input())
b=len(a)
c=int(a)
e=[]
for i in range(b):
    d=int(c%10)
    e.append(d)
    c=c/10
print(sum(e))