# Create a collection of questions
# Each question needs an answer
# Randomly select questions
# Ask the user each question
# Check their answer
# Keep track of correct answers
# Show the final score

# The big thing you're about to learn is how to represent related information in Python.

import random

# trivia questions and the correct answer   QUESTION → ANSWER
questions = {
    "What is the largest planet in our solar system?": "jupiter",
    "What animal is known as the 'King of the Jungle'?": "lion",
    "What is the only mammal capable of true flight instead of gliding?": "bat",
    "How many hearts does an octopus have?": "3",
    "What is the fastest land animal?": "cheetah",
    "What planet is known as the Red Planet?": "mars",
    "What is the name of Harry Potter's owl?": "hedwig",
    "What is the smallest prime number?": "2",
    "Which animal can sleep while standing up?": "horse",
    "What is the name of the cowboy in Toy Story?": "woody",
    "How many sides does a hexagon have?": "6",
    "What is the main ingredient in hummus?": "chickpeas",
    "What is the largest ocean on Earth?": "pacific",
    "What color is a giraffe's tongue typically?": "purple",
    "What is the hardest natural substance on Earth?": "diamond",
    "Which bird is famous for being unable to fly but being an excellent swimmer?": "penguin",
    "What is the name of the princess in The Princess and the Frog?": "tiana",
    "How many bones are in the adult human body?": "206",
    "What gas do plants absorb from the atmosphere?": "carbon dioxide",
    "Which video game character is famous for saying 'It's-a me!'?": "mario",
    "What is the world's largest species of shark?": "whale shark",
    "What fruit is known for having its seeds on the outside?": "strawberry",
    "What is the name of the fictional city where Batman lives?": "gotham",
    "Which planet has the most prominent ring system?": "saturn",
}

# Randomly select questions
def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = len(questions_list)
    score = 0

    # random.sample() to create a randomized ordering without repeating questions
    while True:

        number_of_questions = int(input("How many questions would you like? "))

        if number_of_questions <= total_questions:
            print(f"Great lets play {number_of_questions} questions :)")
            break
        else:
            print(f"Oops! You only have {total_questions} question(s) to pick.")

    selected_questions = random.sample(questions_list, number_of_questions)

    # loop and give index of each question and its question value
    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")     # numbers the list of questions starting at 1. -> max
        user_answer = input("Your answer to the question?: ").lower().strip()   #.lower bc answers are lowercase
        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print(f"Correct! You got it!\n")
            score += 1
        else:
            print(f"Whoops, the correct answer is {correct_answer}. You got it wrong!\n")

    print(f"GAME OVER! Your final score is {score}/{number_of_questions} question(s).")

python_trivia_game()
