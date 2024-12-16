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

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
random_num = random.randint(1, 100)