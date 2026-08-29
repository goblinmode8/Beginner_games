# generates random number between 1-100
# loop
    # ask user to make a guess
    # invalid answer
        # error message
    # if number < guess
        # "Too low"
    # if number > guess
        # "Too high"
    # else when guess is correct
        # print a rewarding message

import random

# number = computer's secret number
number = random.randint(1, 100)

while True:
    try:
        # guess  = user's guess
        guess = int(input("Please enter a guess between 1 - 100: "))

        if guess < number:
            print("You guessed too LOW")

        elif guess > number:
            print("You guessed too HIGH")

        else:
            print("You guessed correctly!!! 🎉")
            break

    except ValueError:
        print("You guessed something invalid")
