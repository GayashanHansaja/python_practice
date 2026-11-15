numbers=[3,5,6,2,2,2,6]

unique=[]

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)