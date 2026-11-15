print("Welcome to the Guessing Game!")

Number=8
print(type(Number))
chances = 3

while chances > 0:
    chances -= 1
    guessing=int(input("insert you guessed number: "))
    print(type(guessing))

    if guessing== Number:
        print("you have won")
        break
    elif chances >0:
        print("try again")
else:
        print("you have lost")

