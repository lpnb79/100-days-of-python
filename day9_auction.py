import auction_art
print(auction_art.logo)

def highestbid(bidding_dictionary):
    highestbid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid = bidding_dictionary[bidder]
        if bid > highestbid:
            highestbid = bid
            winner = bidder
    print(f"The winner is {winner.capitalize()} with the bid ${highestbid}.\n")

auction = {}
bidding = True

while bidding:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: $"))
    auction[name] = price
    additionalBids = input("Any other bidders? Yes or No. ").lower()
    if additionalBids == "yes":
        bidding = True
        print("\n" * 20)
    elif additionalBids == "no":
        bidding = False
        print("\n")
        highestbid(auction)
    else:
        print("Only yes or no. Auction ended.\n")
        break
        

