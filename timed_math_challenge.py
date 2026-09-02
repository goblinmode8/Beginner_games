# 🧮 MATH SPEED CHALLENGE

import random
import time

print("Welcome to hell aka MATH SPEED CHALLENGE :) \n")

# Operators to use
OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_QUESTIONS = 10


# generate a random math problem for user
def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + str(operator) + " " + str(right)
    answer = eval(expr)    # automatically gives the answer
    return expr, answer

# Create the math problem
expr, answer = generate_problem()
# print("Example: " + expr, answer)

wrong = 0
input("Press enter to start!!!")
print("-----------------------------")

start_time = time.time()        # Record the starting time

# display question and get user's answer
for i in range(TOTAL_QUESTIONS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            print("Correct! 🎉")
            break
        else:
            print("Incorrect answer. Try again.")

end_time = time.time()
total_time = round(end_time - start_time, 2)        # Calculate elapsed time
print("-----------------------------")
print("GREAT WORK! ⭐️ You finished in", total_time, "seconds!!")
