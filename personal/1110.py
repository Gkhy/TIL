cnt=0
D=input()
N=int(D)

while True:
    if int(D)<10:
        D='0'+D
    a=D[0]
    b=D[-1]
    c=int(a)+int(b)
    D=b+(str(c)[-1])
    cnt+=1
    if N==int(D):
        break
print(cnt)    


    