print("Good morning")
Weight= int(input("Please enter your weight:"))
Unit=input("Is it kilograms(K) or labs(L)")

if Unit.upper()=="L":
    converted=Weight * 0.45
elif Unit.upper()=="K":
    converted=Weight / 0.45

print(converted)
