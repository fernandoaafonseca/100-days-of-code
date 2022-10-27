'''
Jokenpo (Rock, Paper and Scissors) in the terminal:

I played around with the code a bit, adding colors, ASCII art, animations for the strings, sounds etc.

I know it could be better, but I don't want to be stuck in it for too long, so I can try other things.

PS: you need to install the "playsound" module to hear the sounds.
'''

import random
import sys
from time import sleep
from colorama import Fore, Back, Style

def animate(text, time=0.01):
  for letter in text:
    print(letter, end="")
    sys.stdout.flush()
    sleep(time)

def jokenpo():
    sleep(0.1)
    animate(f'\n\n{Fore.YELLOW}==================================================\n')
    sleep(0.5)
    print('JO!')
    sleep(0.5)
    print('KEN!')
    sleep(0.5)
    print('PO!')
    sleep(0.5)
    animate(f'{Fore.YELLOW}==================================================\n\n')
    sleep(0.1)

print(f'''{Fore.YELLOW}
⠀⠀⠀⠀⠀⣠⡴⠖⠒⠲⠶⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠖⠒⢶⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡾⠁⠀⣀⠔⠁⠀⠀⠈⠙⠷⣤⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⠀⠀⠀⢀⡿⠀⠀⠀⠀⠀⠀⠀
⣠⠞⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⠈⢿⡀⢠⡶⠒⠳⠶⣄⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⣰⠏⠀⢀⣤⣤⣄⡀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠛⠛⠃⠸⡇⠈⣇⠸⡇⠀⠀⠀⠘⣇⠀⠀⣠⡾⠁⠀⠀⠀⢀⣾⣣⡴⠚⠉⠀⠀⠈⠹⡆⠀
⣹⡷⠤⠤⠤⠄⠀⠀⠀⠀⢠⣤⡤⠶⠖⠛⠀⣿⠀⣿⠀⢻⡄⠀⠀⠀⢻⣠⡾⠋⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠀⠀⢀⣠⡾⠃⠀
⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡤⠖⠋⢀⣿⣠⠏⠀⠀⣿⠀⠀⠀⠘⠉⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀⠀⣠⠶⠋⠁⠀⠀⠀
⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠀⠀⠀⢀⣴⡿⠥⠶⠖⠛⠛⢶⡄
⠀⠉⢿⡋⠉⠉⠁⠀⠀⠀⠀⠀⢀⣠⠾⠋⠀⠀⠀⠀⢀⣰⡇⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⢀⣠⠼⠃
⠀⠀⠈⠛⠶⠦⠤⠤⠤⠶⠶⠛⠋⠁⠀⠀⠀⠀⠀⠀⣿⠉⣇⠀⡴⠟⠁⣠⡾⠃⠀⠀⠀⠀⠀⠈⠀⠀⠀⣀⣤⠶⠛⠉⠀⠀⠀
⠀⠀⠀⠀⢀⣠⣤⣀⣠⣤⠶⠶⠒⠶⠶⣤⣀⠀⠀⠀⢻⡄⠹⣦⠀⠶⠛⢁⣠⡴⠀⠀⠀⠀⠀⠀⣠⡶⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⡴⠋⣠⠞⠋⠁⠀⠀⠀⠀⠙⣄⠀⠙⢷⡀⠀⠀⠻⣄⠈⢷⣄⠈⠉⠁⠀⠀⠀⢀⣠⡴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡾⠁⣴⠋⠰⣤⣄⡀⠀⠀⠀⠀⠈⠳⢤⣼⣇⣀⣀⠀⠉⠳⢤⣭⡿⠒⠶⠶⠒⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⠃⢰⠇⠰⢦⣄⡈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠛⠓⠲⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠸⣧⣿⠀⠻⣤⡈⠛⠳⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠹⣆⠀⠈⠛⠂⠀⠀⠀⠀⠀⠀⠈⠐⠒⠒⠶⣶⣶⠶⠤⠤⣤⣠⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⣦⣀⠀⠀⠀⠀⠐⠲⠤⣤⣀⡀⠀⠀⠀⠀⠀⠉⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⠤⠤⠤⠶⠞⠋⠉⠙⠳⢦⣄⡀⠀⠀⠀⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⠦⠾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
''')

animate(f'{Fore.YELLOW}==================================================\n')

cpu_choice = random.randint(0,2)

user_choice = input('What do you choose?\n\
    0 - Rock\n\
    1 - Paper\n\
    2 - Scissors\n')

try:
    user_choice = int(user_choice)
except:
    animate(f'{Fore.RED}YOU LOSE! Choose "0", "1" or "2"!{Style.RESET_ALL}')
    exit()

animate(f'{Fore.YELLOW}==================================================\n')

if user_choice not in (0, 1, 2):
    animate(f'{Fore.RED}YOU LOSE! Choose "0", "1" or "2"!{Style.RESET_ALL}')
    exit()

if user_choice == 0:
    animate(f'\n{Fore.GREEN}You chose ROCK')
    animate(f'''{Fore.GREEN}
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')
elif user_choice == 1:
    animate(f'\n{Fore.GREEN}You chose PAPER')
    animate(f'''{Fore.GREEN}
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''')
else:
    animate(f'\n{Fore.GREEN}You chose SCISSORS')
    animate(f'''{Fore.GREEN}
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')

jokenpo()

if cpu_choice == 0:
    animate(f'{Fore.RED}Computer chose ROCK')
    animate(f'''{Fore.RED}
    _______
---'   ____)
    (_____)
    (_____)
    (____)
---.__(___)''')
elif cpu_choice == 1:
    animate(f'{Fore.RED}Computer chose PAPER')
    animate(f'''{Fore.RED}
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''')
else:
    animate(f'{Fore.RED}Computer chose SCISSORS')
    animate(f'''{Fore.RED}
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')

if user_choice == cpu_choice:
    animate(f'\n{Fore.BLUE}\nIT\'S A TIE!\n')
elif user_choice == 0 and cpu_choice == 1:
    animate(f'\n{Fore.RED}\nPaper covers rock.')
    animate(f'\n{Fore.RED}\nYOU LOSE!\n')
elif user_choice == 0 and cpu_choice == 2:
    animate(f'\n{Fore.GREEN}\nRock smashes scissors.')
    animate(f'\n{Fore.GREEN}\nYOU WIN!\n')
elif user_choice == 1 and cpu_choice == 0:
    animate(f'\n{Fore.GREEN}\nPaper covers rock')
    animate(f'\n{Fore.GREEN}\nYOU WIN!\n')
elif user_choice == 1 and cpu_choice == 2:
    animate(f'\n{Fore.RED}\nScissors cuts paper!')
    animate(f'\n{Fore.RED}\nYOU LOSE!\n')
elif user_choice == 2 and cpu_choice == 1:
    animate(f'\n{Fore.GREEN}\nScissors cuts paper!')
    animate(f'\n{Fore.GREEN}\nYOU WIN!\n')
else:
    animate(f'\n{Fore.RED}\nRock smashes scissors!')
    animate(f'\n{Fore.RED}\nYOU LOSE!\n')

animate(f'\n{Fore.YELLOW}==================================================\n{Style.RESET_ALL}')