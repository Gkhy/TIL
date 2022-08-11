S,K,H=map(int,input().split())
if S+K+H>=100:
    print('OK')
else:
    if min(S,K,H)==S:
        print('Soongsil')
    else:
        if min(S,K,H)==H:
            print('Hanyang')    
        else:
            print('Korea')        