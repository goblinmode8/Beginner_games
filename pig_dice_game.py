# 🐷 PIG DICE GAME

import random

print("Welcome to Pig — a dice game where every roll is a gamble! 🎲🐷\n")

# DISPLAY OF GAME RULES
print("🐷 HOW THE GAME WORKS")
print("    In this multiplayer game, players take turns rolling a six-sided die. 🎲\n")
print("    Sounds easy, right?\n")
print("    Well... there's a catch. 👀\n")
print("    Every roll from 2–6 adds to your score for the current turn. ")
print("    BUT if you roll a 1, you lose ALL points from that turn and your turn immediately ends.")
print("    Be smart first player to reach 50 points wins! 🥇\n ")
print("    🎲 WELCOME TO PIG 🎲")


# Randomly generates number between 1 - 6
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


# User input for number of players
while True:
    players = input("Enter number of players (2-4): ")
    if players.isdigit():
        players = int(players)      # string into int
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Please enter a number between 2 and 4.")


# SET UP THE GAME
max_score = 50          # Set winning score to 50
player_score = [0 for _ in range(players)]     # puts 0 as score for every player's score

# PLAYER'S TURN
while max(player_score) < max_score:        # Keep playing until somebody reaches 50.

    # for loop to handle each player's score
    for player_idx in range (players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_score[player_idx], "\n")
        current_score = 0

        while True:
            # repeats until turn is over which is hitting 1, or they stop
            should_roll = input("Would you like to roll a dice (y/n)? ")
            if should_roll.lower() != "y":
                break

            # Roll the die
            value = roll()
            if value == 1:
                print("You rolled a 1 :( turn over.")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:",value, "nice job!")

            print("Your score is:", current_score)
        # Show roll and current turn score
        player_score[player_idx] += current_score
        print("Your total score is:", player_score[player_idx])
        if player_score[player_idx] < max_score:
            print("You can do it!!")

max_score = max(player_score)
winning_idx = player_score.index(max_score)
print("\nPlayer number", winning_idx +1," 🥇YOU WIN!🥇 with a score of:", max_score,"!!!")

