#주어진 숫자를 뒤집은 결과를 출력하시오. 
#* 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지
a=int(input())
b=0
while a>0:
    b=b*10
    c=a%10
    b+=c
    a=a//10
print(b)
