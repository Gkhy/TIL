T=5
li_=[]
S_=''
for _ in range(T):
    S=input()
    li_.append(S)
for i in range(15):
    for j in range(5):
        if i <len(li_[j]):
            S_+=li_[j][i]
print(S_)            



