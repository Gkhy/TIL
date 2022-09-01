text=input()
li_=[]
for i in text:
    if i not in 'CAMBRIDGE':
        li_.append(i)
for i in li_:
    print(i,end='')       


