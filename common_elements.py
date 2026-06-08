#Common Elements use set
a = [1,2,3,4]
b = [3,4,5,6]


s=set()
for i in a :
    if i in b:
        s.add(i)
print(s)
