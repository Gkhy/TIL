N=int(input())
M=input().split()
a=0
b=0
for i in M:
    if a==0 and i=='0':
        a+=1
        b+=1
    if a==1 and i=='1':
        a+=1
        b+=1
    if a==2 and i=='2':
        a=0
        b+=1
print(b)                    
    