#anagram
a='listen'
b='silent'
c={}
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for j in b:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
if c==d:
    print("ANAGRAM")


