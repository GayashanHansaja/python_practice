print("welcome to the car game")
operation=""

while True:
    operation=input()

    if operation=="help":
        print("start : start the car and go")
        print("Stop : stop the car")
        print("Quit : exit")

    elif operation=="start":
        print("we are going")

    elif operation=="stop":
        print("Stoppng the car")

    elif operation=="quit":
        print("exiting the game")
        break
    else:
        print("I don't understand that")