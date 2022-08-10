W=[]
K=[]
for _ in range(10):
    W.append(int(input()))
for _ in range(10):
    K.append(int(input()))
W.sort(reverse=1)

K.sort(reverse=1)
print(W[0]+W[1]+W[2],K[0]+K[1]+K[2])            