import sys
S=0

while(True):
    a=0
    S=sys.stdin.readline().rstrip()
    if S=='.':
        break

    li1=[]
    for i in S:
        if i=='[':
            li1.append(i)
        elif i=='(':
            li1.append(i)    
        elif i==']':
            try:
                b=li1.pop()
                if b!='[':
                    print('no')
                    a=1
                    break
            except:
                print('no')
                a=1
                break  
        elif i==')':
            try:
                b=li1.pop()
                if b!='(':
                    print('no')
                    a=1
                    break
            except:
                print('no')
                a=1
                break    
    if len(li1)!=0 and a==0:
        print('no')
    elif a==0:
        print('yes')                


