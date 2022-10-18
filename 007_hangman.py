import os
import random
from hangman_art import stages
from hangman_art import logo
from hangman_words_list import words_list
from colorama import Fore, Back, Style


# list of the words for the game import from the "hangman_words_list.py" module
words_list = words_list

# choose a word from the list
chosen_word = random.choice(words_list)

display = []

# creates empty spaces in the lenght of the chosen word
for _ in range(len(chosen_word)):
    display.append('_')

# prints the "Hangman" logo
os.system('cls')
print(f'{Fore.BLUE}{logo}{Style.RESET_ALL}\n\n')

# prints the empty spaces with the lenght of the chosen word
print(f'{Fore.GREEN}{display}{Style.RESET_ALL}\n\n')

# initializes some variables to keep track of the game state
lives = 6
position = 0
right_letters = 0
track = 0

while lives > 0:
# prints the number of lives left
    if lives > 1:
        print(f'You have {lives} lives left.')
    else:
        print(f'You have {lives} live left.')

# prints the ASCII art for the player's current lives
    print(f'{Fore.YELLOW}{stages[lives]}{Style.RESET_ALL}')

# asks the user to write a letter
    guess = input('Guess a letter:\n').lower()
    position = 0
    track = 0
    os.system('cls')

# checks if the letter is in the chosen word
    for letter in chosen_word:
        if letter == guess:
            display[position] = letter
            right_letters += 1
            track += 1
        position += 1

# displays the current state of the game with the letters filled in
    print(f'{Fore.GREEN}{display}{Style.RESET_ALL}\n\n')
    
# if the word does not contain that letter,
# it will give -1 to the life of the player
    if track == 0:
        print(f'{Fore.RED}You lost a live!{Style.RESET_ALL}\n')
        lives -= 1

# if all the letters are filled, the user wins the game
    if right_letters == len(display):
        print('You won!\n')
        print(f'{Fore.BLUE}The word was: {chosen_word}.{Style.RESET_ALL}')
        break
    
# if the user runs out of lives, game over
    if lives == 0:
        print(stages[0])
        print(f'{Fore.RED}You lose!{Style.RESET_ALL}\n')
        print(f'{Fore.BLUE}The word was: {chosen_word}.{Style.RESET_ALL}')
        break