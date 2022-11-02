import os
import random
from time import sleep


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def deal_card(num):
    cards = []
    for _ in range(num):
        card = random.choice(deck)
        cards.append(card)
    return cards


def calculate_score(player_cards):
    sum_cards = sum(player_cards)
    if sum_cards == 21 and len(player_cards) == 2:
        return 0
    if 11 in player_cards and sum_cards > 21:
        player_cards.remove(11)
        player_cards.append(1)
    if player_cards == 21:
        return 0
    return sum_cards


def compare(user_score, dealer_score):
    if user_score == dealer_score:
        result = 'draw'
        return result
    elif user_score == 0:
        result = 'blackjack'
        return result
    elif dealer_score == 0:
        result = 'blackjack'
        return result
    elif user_score > 21:
        result = 'bust'
        return result
    elif dealer_score > 21:
        result = 'bust'
        return result
    elif user_score > dealer_score:
        result = 'win'
        return result
    else:
        result = 'lose'
        return result


deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_over = False
user_cards = deal_card(2)
dealer_cards = deal_card(2)

cls()
print(f'\nDealer cards: [{dealer_cards[0]}, ?]')
print(f'Your cards: {user_cards}')

while not game_over:
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    compare(user_score, dealer_score)

    if user_score == 0 or dealer_score == 0 or user_score > 21:
        game_over = True
    else:
        hit_or_stack = input('\nDo you want to hit one more card?\nType "y" or "n":\n')
        if hit_or_stack == 'y':
            user_cards += deal_card(1)
            cls()
            print(f'\nDealer cards: [{dealer_cards[0]}, ?]')
            print(f'Your cards: {user_cards}')
        elif hit_or_stack == 'n':
            game_over = True

if user_score < 21:
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards += deal_card(1)
        dealer_score = calculate_score(dealer_cards)
        for card in dealer_cards:
            cls()
            print(f'\nDealer cards: {dealer_cards}')
            print(f'Your cards: {user_cards}')
            sleep(2)

cls()
print(f'\nDealer cards: {dealer_cards}')
print(f'\nYour cards: {user_cards}')

final_result = compare(user_score, dealer_score)
if final_result == 'draw':
    print(f'\nIt\'s a {final_result}!')
elif final_result == 'bust':
    if user_score > 21:
        print(f'\nYou\'re busted! You lose!')
    else:
        print(f'\nThe computer is busted! You lose!')
elif final_result == 'blackjack':
    print(f'\nBLACKJACK! You win!')
else:
    print(f'\nYou {final_result}!')
print('\nGAME OVER!')