numbers={
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"
}

phone_number =input("Enter a phone number: ")
result = ""
for digit in phone_number:
    if digit in numbers:
        result+=numbers.get(digit)
print(result, end=" ")