#First Repeating Element

a=[10,2,3,4,5,6,7,3,5]

s=set()
for i in a:
    if i not in s:
        s.add(i)
    else:
       print(i)
       break 



