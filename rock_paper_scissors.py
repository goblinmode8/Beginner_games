# ask user to make choice
# if choice is not valid
    # print error
# computer makes choice
    # print choice using emojis
# determine winner
# ask user if they wanna continue
# if not game over

import random

# declare constants
ROCK = "r"
PAPER = "p"
SCISSORS = "s"

# implement D R Y
emojis = {"ROCK": "🪨", "PAPER": "📝", "SCISSORS": "✂️"}
# print(emojis.keys())                  # dict_keys(['r', 'p', 's'])
choices = tuple(emojis.keys())     # ('r', 'p', 's')

print("welcome to rock paper scissors game :) \n")

def get_user_choice():
    while True:
        user_choice = input("rock, paper, scissors? (r/p/s): ").lower()
        # if user_choice != "r" or user_choice != "p" or user_choice != "s":
        if user_choice in choices:
            return user_choice          # instead of breaking out of loop
        else:
            print("You guessed wrong :( plz enter valid choice: ")

def display_choice(user_choice, computer_choice):
    # printing choices as emojis
    print(f"user choice is {emojis[user_choice]}")
    print(f"computer choice is {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("whoops TIE!")
    elif (          # double (()) allows multi lines
        (user_choice == "ROCK" and computer_choice == "SCISSORS") or
        (user_choice == "PAPER" and computer_choice == "ROCK") or
        (user_choice == "SCISSORS" and computer_choice == "PAPER")):
        print("You win!")
    else:
        print("You lost!")


def play_game():
    user_choice = get_user_choice()     # calls function

    computer_choice = random.choice(choices)

    display_choice(user_choice, computer_choice)        # pass arguments

    determine_winner(user_choice, computer_choice)

def main():
    while True:
        play_game()

        should_continue = input("Do you want to play again? (y/n): ").lower()

        if should_continue == "n":
            print("\nThank you for playing!")
            break

main()
# refactoring = changing structure of code without changing its functionality
# modularization = breaking down a large program into smaller reusable parts called modules or functions
    # messy room into organized boxes
