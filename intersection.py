# intersection.py

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

result = []

for num in a:
    if num in b:
        result.append(num)

print(result)