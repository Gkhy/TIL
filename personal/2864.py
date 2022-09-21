a,b=input().split()
a1=[]
b1=[]
a2=[]
b2=[]
for i in a:
    if i =='6':
        a1.append('5')
    else:
        a1.append(i)    
for e in b:
    if e =='6':
        b1.append('5')
    else:
        b1.append(e)
a1=''.join(a1)
b1=''.join(b1)             
min=int(a1)+int(b1)
for c in a:
    if c=='5':
        a2.append('6')
    else:
        a2.append(c)    
for d in b:
    if d=='5':
        b2.append('6')
    else:
        b2.append(d)     
a2=''.join(a2)
b2=''.join(b2)         
max=int(a2)+int(b2)
print(min,max)