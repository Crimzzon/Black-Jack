import math
import random

card_list = []
player_cards = []
number_of_decks = 1
deck_pop = 1

for i in range((4*number_of_decks)):
    deck_pop = 1
    for x in range(13):
        deck_pop = deck_pop + 1
        card_list.append(deck_pop)

def card_conversion(card):
    if card == 11 or card == 12 or card == 13: 
        card = 10
    elif card == 14: 
        card = 11
    return card

def new_card():
    card = card_list[random.randint(0,len(card_list))-1]
    card = card_conversion(card)
    card_list.pop(card)
    return card

def check_aces(list):
    for i in range(len(list)):
        if sum(list) > 21 and list[i] == 11:
            list[i] = 2
    return list

def print_cards(list):
    for i in range(len(list)):
        if len(list)-i > 1:
            print(list[i],"+",end=" ")
        else:
            print(list[i],"=",sum(list))
    return

player_cards = [new_card() for i in range(2)]
dealer_cards = [new_card() for i in range(2)]

check_aces(player_cards)
check_aces(dealer_cards)

print("Players cards:",end=" ")
print_cards(player_cards)
print("Dealers up card: ", dealer_cards[0],dealer_cards[1])

hit = input("Hit? Y/N ")

while(sum(player_cards) < 20):
    if hit == 'Y' or 'y':
        player_cards.append(new_card())
        check_aces(player_cards)
        print_cards(player_cards)
        if sum(player_cards) > 20:
            break
        else:
            hit = input("Hit? Y/N")
    if hit == 'N' or 'n':
        break

while sum(dealer_cards) < 17:
    dealer_cards.append(new_card())
    check_aces(dealer_cards)

print("Players cards:",end=" ")
print_cards(player_cards)
print("Dealers cards:",end=" ")
print_cards(dealer_cards)

if ((sum(player_cards) > 21) or (sum(dealer_cards) > sum(player_cards))) and sum(dealer_cards) <= 21:
    print("Dealer wins!",sum(player_cards),sum(dealer_cards))
elif (sum(dealer_cards) > 21) or (sum(dealer_cards) < sum(player_cards)) and sum(player_cards) <= 21:
    print("Player wins!",sum(player_cards),sum(dealer_cards))
else:
    print("Draw!",sum(player_cards),sum(dealer_cards))


