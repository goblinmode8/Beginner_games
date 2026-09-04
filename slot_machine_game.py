# 🎰 SLOT MACHINE

import random

MAX_LINES = 4
MAX_BET = 100
MIN_BET = 1

ROWS = 4
COLS = 4

# Symbols displayed on slot machine
symbol_count = {
    "🍒": 8,
    "🍋": 10,
    "🍊": 8,
    "⭐": 20,
    "💎": 12
}

symbol_value = {
    "🍒": 20,
    "🍋": 4,
    "🍊": 2,
    "⭐": 2,
    "💎": 3
}

# line 1 = 0
def check_winnings(columns,lines, bet, values):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        # checks symbol in first column in first row
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break

        else:
            # winnings = multiplier * symbol
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

# SPIN THE SLOT MACHINE
    # Randomly generate symbols
    # Create the slot machine grid
    # Display it
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        # make coppy of symbols list so the count reduces for the next spin
        current_symbols = all_symbols[:]        # current = copy
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)      # all column to columns list

    return columns


# Print slot machine layout so the print vertical
def print_slot_machine(columns):
    print(" 🎰 SPIN  🎰")    # transposing
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


# Get number of lines from user
def get_number_of_lines():
    while True:
        lines = input("🎰 Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)        # convert to mae a numeric number
            if 1 <= lines <= MAX_LINES:     # validate input is inbetween two value
                break
            else:
                print("Enter valid number of lines!")
        else:
            print("Please enter a number.")

    return lines


# GET USER DEPOSIT
def deposit():
    while True:
        print("  🐲 WELCOME TO DRAGON SLOT MACHINE 🐲 ")
        amount = input("\n💰 How much do you want to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)        # convert to mae a numeric number
            if amount > 0:
                break
            else:
                print("Please enter a number greater than 0!")
        else:
            print("Please enter a number.")

    return amount       # Add deposit to balance


# Get users input on how many lines they want to bet on & how much they want to bet per line
def get_bet():
    while True:
        amount = input("🎰 What would you like to bet on each line? $ ")
        if amount.isdigit():
            amount = int(amount)        # convert to mae a numeric number
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please bet a number between ${MIN_BET} and ${MAX_BET}!")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        # Make sure user can afford bet
        if total_bet > balance:
            print(f"You do not have enough money!, your current balance is ${balance}")
        else:
            break

    print("\n🎰 You bet", lines, "lines")
    print(f"🎰 Your bet ${bet} \n🎰 Total bet ${total_bet}\n")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)  # fills slots
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_count)
    if winnings > 0:
        print(f"\n💰 Winnings: ${winnings} NICE JOB! 💰")
    else:
        print("\n💸 No winnings this spin!")
    if winning_lines:
        print("🎉 You won lines:", *winning_lines)


    # winnings - bet
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"\n💰Current balance is ${balance}")
        answer = input("\n🐲 Press enter to play (q to quit)")
        if answer == "q":
            print("thanks for playing 🐲")
            break
        balance += spin(balance)

main()
