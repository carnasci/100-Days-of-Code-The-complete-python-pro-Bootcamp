from art import logo, vs
from game_data import data
import random


# Pick 2 random options from data and assign them to a and be and remove them from data.

def random_pick():
    pick = random.choice(data)
    data.remove(pick)
    return pick

# def compare_choices(choice_a, choice_b):
#     if choice_a["follower_count"] > choice_b["follower_count"]:
#         return choice_a
#     else:
#         return choice_b

def compare_choices(list_of_choices):
    """Takes a list of two options and returns the one with the most followers
        as winner"""
    followers = 0
    winner = {}
    for item in list_of_choices:
        if item["follower_count"] > followers:
            followers = item["follower_count"]
            winner = item
    return winner

def game():

    play_again = True
    game_score = 0
    option_a = random_pick()
    while play_again:
        options = []
        option_b = random_pick()
        options.append(option_a)
        options.append(option_b)
        print(logo)
        if game_score > 0:
            print(f"You're right! Curent score: {game_score}")
        print(f"Compare A: {option_a["name"]}, a {option_a["description"]}, from {option_a["country"]}.")
        print(vs)
        print(f"Compare B: {option_b["name"]}, a {option_b["description"]}, from {option_b["country"]}.")
        user_pick = input("Which has more followers? Type 'A' or 'B': ").lower()
        if user_pick == "a":
            user_pick = option_a
        else:
            user_pick = option_b

        winner = compare_choices(options)
        if user_pick == winner:
            option_a = user_pick
            game_score += 1
        else:
            play_again = False




game()