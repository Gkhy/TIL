import sys
S = sys.stdin.read()

list_=[0]*26
for i in S:
    if i.islower():
        list_[ord(i)-97]+=1
for j in range(26):
    if list_[j]==max(list_):
        print(chr(j+97),end='')    