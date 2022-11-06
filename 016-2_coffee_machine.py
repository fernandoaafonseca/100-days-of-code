from collections import OrderedDict
from itertools import islice
import os


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

list_of_tuples = [(key, MENU[key]) for key in MENU]
ORDERED_MENU = OrderedDict(list_of_tuples)

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f'Sorry! The is not enough {item}.')
            return False
    return True


def process_payment():
    print('\nPlease insert a coin.')
    quarter = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

    total_money = 0

    quarters_ammount = int(input('How many quarters ($0.25)? '))
    total_money += quarters_ammount * quarter
    dimes_ammount = int(input('How many dimes ($0.10)? '))
    total_money += dimes_ammount * dimes
    nickles_ammount = int(input('How many nickles ($0.05)? '))
    total_money += nickles_ammount * nickles
    pennies_ammount = int(input('How many pennies ($0.01)? '))
    total_money += pennies_ammount * pennies

    return total_money


def check_money(total_money, drink_cost):
    global profit
    os.system('cls' if os.name=='nt' else 'clear')
    print(f'Total money: ${total_money:.2f}.')
    if total_money > drink_cost:
        change = total_money - drink_cost
        print(f'\nHere is your change: ${change:.2f}.')
        profit += drink_cost
        return True
    elif total_money == drink_cost:
        profit += drink_cost
        return True
    else:
        return False


def make_coffee(drink_choice, drink_name):
    for item in drink_choice['ingredients']:
        resources[item] -= drink_choice['ingredients'][item]
    print(f'\nHere is your {drink_name}! Enjoy!')


valid_inputs = ['x', 'y']
for i in range(len(ORDERED_MENU)):
    valid_inputs.append(i)
is_on = True
os.system('cls' if os.name=='nt' else 'clear')

while is_on:
    user_input = 'z'

    while user_input not in valid_inputs:

        print(f'What would you like?\n')
        for i in range(len(ORDERED_MENU)):
            print(f'{i} - {next(islice(ORDERED_MENU.keys(), i, None))}')
        print(f'x - report')
        print(f'y - turn off\n')
        user_input = input()
        
        if user_input != int:
            try:
                user_input = int(user_input)

                if type(user_input) == int:
                    drink_name = next(islice(ORDERED_MENU.keys(), user_input, None))
                    drink_choice = MENU[drink_name]
                    
                    if check_resources(drink_choice['ingredients']):
                        drink_cost = drink_choice['cost']
                        total_money = process_payment()
                        if check_money(total_money, drink_cost):
                            make_coffee(drink_choice, drink_name)
                        else:
                            print(f'\nSorry, that\'s not enough money. Money refunded.\n')

            except:
                if user_input == 'x':
                    os.system('cls' if os.name=='nt' else 'clear')
                    print(f'Water: {resources["water"]}ml')
                    print(f'Milk: {resources["milk"]}ml')
                    print(f'Coffee: {resources["coffee"]}g')
                    print(f'Money: ${profit}')

                elif user_input == 'y':
                    print(f'Powering off...')
                    is_on = False
                else:
                    os.system('cls' if os.name=='nt' else 'clear')
                    continue