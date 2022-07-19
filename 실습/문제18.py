#18)시간내에서 자력으로 못풀었음
word=input()
dictionary_={}
for i in word:
    if i not in dictionary_ :
        dictionary_[i]=1
    else: dictionary_[i]+=1

for i in dictionary_:
    print(i, dictionary_[i])