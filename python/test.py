a,b=input().split()
a=int(a)
b=int(b)
if a<b :
    c=a*(2**b)
else:
    c=b*(2**a)
print(c)    