import random
import os
import art

                             
def sum_hand(hand):
    total = 0
    count = 0
    for i in hand:
        if i in ('J', 'Q', 'K'):
            total += 10
        elif i == 'A':
            if total + 11 > 21:
                total += 1
            else:
                total += 11
                count += 1
        else:
            total += i
    if total > 21 and count > 0:
        for i in range(count):
            total = total - (11 + 1)
            if total <= 21:
                return total
    return total


def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    return random.choice(cards)


def play():
    game_over = False
    winner = ""
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "n":
        return
    os.system("clear")
    print(art.logo)

    your_hand = []
    comp_hand = []
    for _ in range(2):
        your_hand.append(deal_card())
        comp_hand.append(deal_card())

    print(f"Your hand: {your_hand}")
    print(f"Computer's first card: {comp_hand[0]}")

    while not game_over:
        if input("Enter 'h' to hit or 'p' to pass: ") == "h":
            card = deal_card()
            your_hand.append(card)
            print(f"Your hand: {your_hand}")
            if sum_hand(your_hand) > 21:
                game_over = True
                winner = "comp"
        else:
            print(f"Computer's hand: {comp_hand}")
            while sum_hand(comp_hand) < 17:
                comp_card = deal_card()
                comp_hand.append(comp_card)
                print(f"Computer's hand: {comp_hand}")
            if sum_hand(comp_hand) > 21:
                game_over = True
                winner = "user"
            elif sum_hand(comp_hand) > sum_hand(your_hand):
                game_over = True
                winner = "comp"
            elif sum_hand(your_hand) > sum_hand(comp_hand):
                game_over = True
                winner = "user"
            elif sum_hand(your_hand) == sum_hand(comp_hand):
                break

    if winner == "user":
        print("You won!")
    elif winner == "comp":
        print("You lose.")
    play()


play()
