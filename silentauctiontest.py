"""
Title: silentauctiontest
Version: 1
Author: Jamie U
Created: 4/2/18
Description: This program allows someone to run a silent auction.
"""

def get_float(message):
    choice = -1
    while choice == -1:
        try:
            choice = float(input(message))
        except:
            print("Please enter numbers only")
    return choice

highestBid = 0
bidCount = 0
name = ""
bids = []
names = []

reservePrice = get_float("What do you want the reserve price to be?")

while name.upper() != "F":
    print ("Highest bid so far is:", highestBid)
    name = ""
    while len(name) < 1:
        name = input("What is your name?")
    if name.upper() != "F":
        bid = get_float("What do you want to bid?")
        if bid > highestBid:
            highestBid = bid
            bids.append(bid)
            names.append(name)
            bidCount += 1
        else:
            print("Sorry " + name + ", you'll need to make another higher bid.")

if highestBid >= reservePrice:
    print("Auction won by ", names[bidCount - 1], "with", bids[bidCount - 1])
else:
    print("Auction did not meet reserve price")

for i in range(bidCount):
    print(names[i], bids[i])
