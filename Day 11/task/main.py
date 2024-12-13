import random
from art import logo

# def deal_card(player_cards):
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     player_cards.append(random.choice(cards))
#     return player_cards
#
# def blackjack():
#     play_again = True
#
#     while play_again:
#
#         user_cards = []
#         dealer_cards = []
#         final_score = f"You're final hand: {user_cards}, final score: {sum(user_cards)}"
#         dealer_final_score = f"Computer's final score: {dealer_cards}, final score: {sum(dealer_cards)}"
#
#         play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
#         if play == "y":
#             print("\n" * 20)
#             print(logo)
#             deal_card(user_cards)
#             deal_card(user_cards)
#             print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
#             deal_card(dealer_cards)
#             deal_card(dealer_cards)
#
#             print(f"Computer's first card: {dealer_cards[0]}")
#
#             deal = True
#             while deal:
#                 deal_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
#                 if deal_another_card == "y":
#                     deal_card(user_cards)
#                     print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
#                     print(f"Computer's first card: {dealer_cards[0]}")
#                     if sum(user_cards) > 21:
#                         print(f"You're final hand: {user_cards}, final score: {sum(user_cards)}")
#                         print(f"Computer's final score: {dealer_cards}, final score: {sum(dealer_cards)}")
#                         print("You went over you lose")
#                         play_again = False
#                         blackjack()
#                 else:
#                     deal = False
#                     print(f"You're final hand: {user_cards}, final score: {sum(user_cards)}")
#                     while sum(dealer_cards) < 17:
#                         deal_card(dealer_cards)
#                     print(f"Computer's final score: {dealer_cards}, final score: {sum(dealer_cards)}")
#                     if sum(dealer_cards) > 21:
#                         print("Dealer went over. You win")
#                     elif sum(user_cards) == sum(dealer_cards):
#                         print("Draw")
#                     elif sum(user_cards) > sum(dealer_cards):
#                         print("You win")
#                     elif sum(user_cards) < sum(dealer_cards):
#                         print("You lose")
#                     play_again = False
#                     blackjack()
#
#
#         else:
#             play_again = False
#             blackjack()
#
# blackjack()

#With hints

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 or computer_score < 21:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    blackjack()
