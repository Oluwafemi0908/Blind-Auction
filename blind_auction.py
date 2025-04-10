# Bidders bid for an item without knowing others bid and the highest bidder wins.
bids = {}
should_continue = True


def auction():
    """
    Takes bidders name and bid and stores them in the bids dictionary
    """
    global should_continue
    bidder = input("What's your name?: ")
    bid = int(input("How much are you bidding?: $"))

    bids[bidder] = bid

    another_bidder = input("Any other bidder? (y or n): ").lower()

    if another_bidder == "n":
        should_continue = False


while should_continue:
    auction()

highest_bid = 0
highest_bidder = ""


# Comparing bids in the dictionary step by step and storing the highest
for key in bids:
    if bids[key] > highest_bid:
        highest_bid = bids[key]
        highest_bidder = key

print(f"The highest bid is ${highest_bid} from {highest_bidder}.")
