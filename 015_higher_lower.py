import random
import os
from modules.higher_lower import data


def get_account():
    return random.choice(data)


def format(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f'{name}, a {description} from {country}'


def check_answer(guess, account_1, account_2):
    if account_1['follower_count'] > account_2['follower_count']:
        answer = 'a'
    else:
        answer = 'b'

    if guess == answer:
        return True
    else:
        return False
    

def game():
    game_over = False
    score = 0
    account_1 = get_account()
    account_2 = get_account()

    while not game_over:
        account_1 = account_2
        account_2 = get_account()

        while account_1 == account_2:
            account_2 = get_account()
        
        print()
        print(f'Compare A: {format(account_1)}.')
        print('vs')
        print(f'Against B: {format(account_2)}.')
        print()

        guess = input('Who has more followers? Type "A" or "B": \n').lower()
        is_correct = check_answer(guess, account_1, account_2)

        os.system('cls' if os.name=='nt' else 'clear')
        
        if is_correct:
            score += 1
            print(f'You got it! Current score: {score}.')
        else:
            print(f'You\'re wrong. Final score: {score}.')
            game_over = True

if __name__ == '__main__':
    game()