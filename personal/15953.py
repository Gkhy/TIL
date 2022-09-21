import sys
T=int(sys.stdin.readline())

for i in range(T):
    ap=0
    bp=0
    a,b=map(int,sys.stdin.readline().strip().split())
    if a==1:
        ap=5000000
    elif 1<a<4:
        ap=3000000
    elif 4<=a<=6:
        ap=2000000
    elif 7<=a<=10:
        ap=500000
    elif 11<=a<=15:
        ap=300000
    elif 16<=a<=21:
        ap=100000
    if b==1:
        bp=5120000
    elif 2<=b<=3:
        bp=2560000
    elif 4<=b<=7:
        bp=1280000
    elif 8<=b<=15:
        bp=640000
    elif 16<=b<=31:
        bp=320000                       
    print(ap+bp)

