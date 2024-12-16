import random
from art import logo

print(logo)

# print("Welcome to the number guessing game!")
# print("I'm thinking of a number between 1 and 100.")
# random_num = random.randint(1, 100)
# difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
#
# attempts = 0
#
# def guess_the_number(level):
#
#     global attempts
#     if level == "easy":
#         attempts = 10
#     else:
#         attempts = 5
#
#
#     while attempts != 0:
#         guess = int(input("Make a guess: "))
#
#         if guess == random_num:
#             print(f"You got it the answer was {random_num}!")
#         elif attempts == 0:
#             print("You've run out of guesses. Refresh page to play again.")
#         else:
#             if guess > random_num:
#                 print("Too high")
#                 print("Guess again.")
#                 attempts -= 1
#                 print(f"You have {attempts} attempts remaining to guess the number.")
#             else:
#                 print("Too low")
#                 print("Guess again.")
#                 attempts -= 1
#                 print(f"You have {attempts} attempts remaining to guess the number.")
#
# guess_the_number(difficulty)

# After seeing solutions video
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty():
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if level == "easy":
            return EASY_LEVEL_ATTEMPTS
        else:
            return HARD_LEVEL_ATTEMPTS

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")


def game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    random_num = random.randint(1, 100)
    attempts = set_difficulty()

    guess = 0
    while guess != random_num:

        print(f"You have {attempts} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, random_num, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != random_num:
            print("Guess again.")

game()

