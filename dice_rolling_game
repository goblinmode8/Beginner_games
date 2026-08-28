# ask Roll the dice?
# choice (y/n) or Y/N
# "invalid choice must be (y/n)
# if choice is no exit game
# if choice is yes print out (#,#)
import random

print("welcome! lets roll some dice :)\n")

dice1 = 0
dice2 = 0
user_input = input("Roll the dice? (y/n) ")

while user_input != "n" and user_input != "N":

    if user_input == "y" or user_input == "Y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print("You rolled (", dice1,"," ,dice2 ,")")
    else:
        print("invalid input, please try again")

    user_input = input("Roll the dice? (y/n) ")
