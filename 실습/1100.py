metrix_=[list(input())for _ in range(8)]
horse=0
for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            if metrix_[i][j]=='F':
                horse+=1
print(horse)
