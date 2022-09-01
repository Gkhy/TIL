A=input()
N=int(A)
hs=0
for i in range(1,N+1):
    if i<100:
        hs+=1
    elif i<1000:
        a=i%10
        b=(i//10)%10
        c=((i//10)//10)%10
        if a-b==b-c:
            hs+=1
print(hs)            
    

            





