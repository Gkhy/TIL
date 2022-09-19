
S=list(input())
li=[]
a=list(map(ord,S))
for i in a:
    if 45<i and i<97:
        li.append(i)
li=list(map(chr,li))
li="".join(li)
print(li)       


