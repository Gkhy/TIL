T=int(input())
round_score=[[],[],[]]
for i in range(T):
    a,b,c=map(int,input().split())
    round_score[0].append(a)
    round_score[1].append(b)
    round_score[2].append(c)
for _ in range(T):
    sum=0
    for i in range(3):
        if round_score[i].count(round_score[i][_])==1:
            sum+=round_score[i][_]
    print(sum)          