li=[]
cnt=0
for i in range(5):
    li.append(input())
for j in range(5):
    if 'FBI' in li[j]:
        print(j+1,end=' ')
    else:
        cnt+=1
if cnt==5:
    print('HE GOT AWAY!')                        