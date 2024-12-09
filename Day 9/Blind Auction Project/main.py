from art import logo

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

def find_highest_bidder(auction_dictionary):
    bidder = ""
    price = 0
    for name in auction_participants:
        if auction_participants[name] > price:
            price = auction_participants[name]
            bidder = name

    print(f"The winer is {bidder} with a bid of ${price}")

print(logo)

add_bidder = True
auction_participants = {}


while add_bidder:

    name = input("What is your name?: ")

    print("\n" * 100)

    price = int(input("What is your bid?: $"))

    print("\n" * 100)

    auction_participants[name] = price

    more_bidders = input("Are there any more bidders? Type 'yes' or 'no'").lower()

    if more_bidders == "no":
        add_bidder = False

    print("\n" * 100)

find_highest_bidder(auction_participants)
