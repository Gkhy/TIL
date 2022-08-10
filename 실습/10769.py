ans1=0
ans2=0

S=input().replace(" ",'')
if ':-)' in S:
    ans1=S.count(':-)')
if ':-(' in S:
    ans2=S.count(':-(')
if ans2>ans1:
    print('sad')
else: 
    if ans1==0 and ans2==0:
        print('none')
    else:
        if ans1==ans2:
            print('unsure')
        else:
            print('happy')    
