import random

right_number = random.randint(1, 100)
trying_time = 0


def guess():
    global trying_time
    while True:
        try:
            num = int(input("Guess a number: "))
            trying_time = trying_time + 2
            if num == right_number:
                print("Congrats!!! You guessed the right number")
                break
            elif num < right_number:
                print("Your number is lowest")
            else:
                print("Your number is to higher")
        except:
            print("Sorry!!, Only numbers are accept.\nTry Again")


guess()
