import random
from art import logo

def deal_card(player_cards):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards.append(random.choice(cards))
    return player_cards

def blackjack():
    play_again = True

    while play_again:

        user_cards = []
        dealer_cards = []
        final_score = f"You're final hand: {user_cards}, final score: {sum(user_cards)}"
        dealer_final_score = f"Computer's final score: {dealer_cards}, final score: {sum(dealer_cards)}"

        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if play == "y":
            print("\n" * 20)
            print(logo)
            deal_card(user_cards)
            deal_card(user_cards)
            print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
            deal_card(dealer_cards)
            deal_card(dealer_cards)

            print(f"Computer's first card: {dealer_cards[0]}")

            deal = True
            while deal:
                deal_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if deal_another_card == "y":
                    deal_card(user_cards)
                    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
                    print(f"Computer's first card: {dealer_cards[0]}")
                    if sum(user_cards) > 21:
                        print(f"You're final hand: {user_cards}, final score: {sum(user_cards)}")
                        print(f"Computer's final score: {dealer_cards}, final score: {sum(dealer_cards)}")
                        print("You went over you lose")
                        play_again = False
                        blackjack()
                else:
                    deal = False
                    print(f"You're final hand: {user_cards}, final score: {sum(user_cards)}")
                    while sum(dealer_cards) < 17:
                        deal_card(dealer_cards)
                    print(f"Computer's final score: {dealer_cards}, final score: {sum(dealer_cards)}")
                    if sum(dealer_cards) > 21:
                        print("Dealer went over. You win")
                    elif sum(user_cards) == sum(dealer_cards):
                        print("Draw")
                    elif sum(user_cards) > sum(dealer_cards):
                        print("You win")
                    elif sum(user_cards) < sum(dealer_cards):
                        print("You lose")
                    play_again = False
                    blackjack()


        else:
            play_again = False
            blackjack()

blackjack()

