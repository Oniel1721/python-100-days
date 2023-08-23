import os
bidders = {}

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

print("Welcome to the secret auction program.")
finish = False
while not finish:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    print("Are there any other bidders? Type 'yes' or 'no'")
    bidders[name] = bid
    finish = input().lower() != 'yes'
    clear()


bidder_with_highest_bid = None
highest_bid = 0

for name, bid in bidders.items():
    if bid > highest_bid:
        bidder_with_highest_bid = name
        highest_bid = bid

if bidder_with_highest_bid is None:
    print("No bidder found")
else:
    print(f"The winner is {bidder_with_highest_bid} with a bid of ${highest_bid}")

