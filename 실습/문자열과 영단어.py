number1=[0,1,2,3,4,5,6,7,8,9]
number2=['zero','one','two','three','four','five','six','seven','eight','nine']
s=input()
for i in number2:
    s=s.replace(i,str(number1[(number2.index(i))]))
print(int(s))    