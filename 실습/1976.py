#import sys
#sys.stdin = open("1976input.txt", "r")
T=int(input())
for i in range(1,T+1):
    t1,m1,t2,m2=map(int,input().split())
   
    # T끼리 더했을때 12보다 크면 12를 빼준값이 시간
    #그렇지 않다면 T1+T2는 그대로 더한값
    #m1+m2는 60이 되기 전까지 즉 59까지는 그대로 내버려둠
    #60이 넘으면 T에 +1 m1+m2은 60을 빼줌(m1+m2는 무조건120(=2시간)보다 작을 수 밖에 없음)
    if t1+t2>=13:
        t12=t1+t2-12
    else: t12=t1+t2
    if m1+m2<60:
        m12=m1+m2
    elif m1+m2>=60:
        m12=m1+m2-60
        t12+=1
    print(f'#{i} {t12} {m12}')    

