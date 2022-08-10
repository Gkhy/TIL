a=int(input())
b=int(input())
c=int(input())
if a==60 and b==60 and c==60:
    print('Equilateral')
else: 
    if a+b+c==180 and a==b or a==c or c==b: 
        print('Isosceles')
    else:
        if a+b+c==180 and a!=b and b!=c and a!=c:
            print('Scalene')
        else: 
            if a+b+c!=180:
                 print('Error')         
