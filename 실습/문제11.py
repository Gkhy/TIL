#2단부터 9단까지 반복하여 구구단을 출력하세요.
#* 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.

number=[2,3,4,5,6,7,8,9]
i=[1,2,3,4,5,6,7,8,9]

for a in number:
    print (f'{a}단')
    for b in i :
        c=a*b
        print (f'{a} x {b} = {c}')