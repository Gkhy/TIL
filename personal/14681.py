X=int(input())
Y=int(input())
if X>0 and Y>0:
    print('1')
elif X>0 and Y<0:
    print('4')
else:
    if X<0 and Y<0:
        print('3')
    else:
        print('2')            