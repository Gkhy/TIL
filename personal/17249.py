# @==@==(^0^)==@===@ 절.대.태.보.해
tb=input()
# '@=' '=@'
a=0
for i in tb:
    if i=='@':
        a+=1
    elif i==')':
        print(a,end=' ')
        a=0
print(a)            

