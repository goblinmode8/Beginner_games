# ask user to make choice
# if choice is not valid
    # print error
# computer makes choice
    # print choice using emojis
# determine winner
# ask user if they wanna continue
# if not game over

import random

# KEY for values
# "r": ("🪨")
# "p": ("📝")
# "s": ("✂️")

emojis = {"r": "🪨", "p": "📝", "s": "✂️"}
choices = ["r", "p", "s"]

print("welcome to rock paper scissors game :) \n")

while True:
    user_choice = input("rock, paper, scissors? (r/p/s): ".lower())
    # if user_choice != "r" or user_choice != "p" or user_choice != "s":
    if user_choice not in choices:
        print("You guessed wrong :( plz enter valid choice (r/p/s): ")
        continue        # this says yo jump back

    computer_choices = random.choice(choices)

    # printing choices as emojis
    print(f"user choice is {emojis[user_choice]}")
    print(f"computer choice is {emojis[computer_choices]}")

    if user_choice == computer_choices:
        print("whoops TIE!")
    elif (          # double (()) allows multi lines
        (user_choice == "r" and computer_choices == "s") or
        (user_choice == "p" and computer_choices == "r") or
        (user_choice == "s" and computer_choices == "p")):
        print("You win!")
    else:
        print("You lost!")

    should_continue = input("Do you want to play again? (y/n): ").lower()
    if should_continue == "n":
        print("\nThank you for playing!")
        break
