a=0
b=input()
Li_=[]
Li_.append(b)
while b!='고무오리 디버깅 끝':
    b=input()
    Li_.append(b)
Li_.pop()
Li_.pop(0)
for i in range(len(Li_)):
    if Li_[i]=='문제':
        a+=1
    elif a==0 and Li_[i]=='고무오리':
        a+=2
    else:
        a-=1    
if a==0:
    print('고무오리야 사랑해')
else:
    print('힝구')                
