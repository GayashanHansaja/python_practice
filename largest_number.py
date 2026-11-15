numbers=[3, 5, 2, 8, 1]

max=numbers[0]

for num in numbers:
    if max<num:
        max=num

print(max)