from art import logo, vs
from game_data import data
import random

# option_a = {}
# option_b = {}
game_score = 0

# Pick 2 random options from data and assign them to a and be and remove them from data.

def random_pick():
    pick = random.choice(data)
    data.remove(pick)
    return pick


def game():
    option_a = random_pick()
    option_b = random_pick()
    print(logo)
    print(f"Compare A: {option_a["name"]}, a {option_a["description"]}, from {option_a["country"]}.")
    print(vs)
    print(f"Compare B: {option_b["name"]}, a {option_b["description"]}, from {option_b["country"]}.")

game()