import os
import art

print("Welcome to the secret auction program.")
print(art.logo)

go = "yes"

auction = {}
bids = {}

while go == "yes":
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))
    auction[name] = bid
    try:
        bids[bid] += 1
    except KeyError:
        bids[bid] = 1
    go = input("Are there any other bidders? Type 'yes' or 'no'.")
    if go == "yes":
        os.system("clear")

max_bid = 0
person = ""
for name in auction:
    if auction[name] > max_bid:
        max_bid = auction[name]
        person = name

same_bidders = []

if bids[max_bid] > 1:
    for name in auction:
        if auction[name] == max_bid:
            same_bidders.append(name)

if len(same_bidders) > 0:
    for name in same_bidders:
        print(f"Maximum bid of {max_bid} is made by {name}.")
else:
    print(f"The winner is {person} with a bid of ${max_bid}.")
