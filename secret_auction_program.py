import arts
print(arts.logo)

bids={}
def find_highest_bidder(dictionary):
    winner=""
    highest_bid=0
    for bidder in dictionary:
        bid_amount=dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"the winner is {winner} and the highest bid is ${highest_bid}")

should_continue=True

while should_continue:
    name = input("What is your name?\n")
    price =int(input("What is your bid?\n$"))
    bids[name]=price
    decision=input("Are there any other bidders? yes or no\n").lower()
    print("\n" * 100)
    if decision == "no":
        should_continue=False
        find_highest_bidder(bids)