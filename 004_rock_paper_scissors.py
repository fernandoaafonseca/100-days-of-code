import random
import sys
from time import sleep
from playsound import playsound

def animate(text, time=0.001):
  for letter in text:
    print(letter, end="")
    sys.stdout.flush()
    sleep(time)

def jokenpo():
    sleep(0.1)
    animate('\033[1;33m==================================================\n')
    sleep(0.5)
    print('JO!')
    sleep(0.5)
    print('KEN!')
    sleep(0.5)
    print('PO!')
    sleep(0.5)
    animate('\033[1;33m==================================================\n')
    sleep(0.1)

print('''\n\033[1;33m
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

animate('\033[1;33m==================================================\n')

cpu_choice = random.randint(0,2)

user_choice = input('What do you choose?\n\
    0 - Rock\n\
    1 - Paper\n\
    2 - Scissors\n')

try:
    user_choice = int(user_choice)
except:
    playsound(r'C:\Windows\Media\ringout.wav')
    animate('\033[1;31mYOU LOSE! Choose "0", "1" or "2"!\033[m')
    exit()

animate('\033[1;33m==================================================\n')

if user_choice not in (0, 1, 2):
    playsound(r'C:\Windows\Media\ringout.wav')
    animate('\033[1;31mYOU LOSE! Choose "0", "1" or "2"!\033[m')
    exit()

if user_choice == 0:
    print('\nYou chose ROCK')
    print('''\033[1;34m
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)\n\033[m''')
elif user_choice == 1:
    print('\nYou chose PAPER')
    print('''\033[1;34m
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)\n\033[m''')
else:
    print('\nYou chose SCISSORS')
    print(''''\033[1;34m
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)\n\033[m''')

jokenpo()

if cpu_choice == 0:
    print('\033[1;33mComputer chose ROCK')
    print('''\033[1;31m
    _______
---'   ____)
    (_____)
    (_____)
    (____)
---.__(___)\033[m''')
elif cpu_choice == 1:
    print('Computer chose PAPER')
    print('''\033[1;31m
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)\033[m''')
else:
    print('Computer chose SCISSORS')
    print(''''\033[1;31m
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)\033[m''')

if user_choice == cpu_choice:
    animate('\033[1;32m\nIT\'S A TIE!\n\033[m')
    playsound(r'C:\Windows\Media\ringout.wav')
elif user_choice == 0 and cpu_choice == 1:
    print('\n\033[1;33mPaper covers rock.\033[m')
    playsound(r'C:\Windows\Media\ringout.wav')
    animate('\033[1;31m\nYOU LOSE!\n\033[m')
elif user_choice == 0 and cpu_choice == 2:
    print('\n\033[1;33mRock smashes scissors.\033[m')
    animate('\033[1;32m\nYOU WIN!\n\033[m')
    playsound(r'C:\Windows\Media\tada.wav')
elif user_choice == 1 and cpu_choice == 0:
    print('\n\033[1;33mPaper covers rock\033[m')
    playsound(r'C:\Windows\Media\tada.wav')
    animate('\033[1;32m\nYOU WIN!\n\033[m')
elif user_choice == 1 and cpu_choice == 2:
    print('\n\033[1;33mScissors cuts paper!\033[m')
    playsound(r'C:\Windows\Media\ringout.wav')
    animate('\033[1;31m\nYOU LOSE!\n\033[m')
elif user_choice == 2 and cpu_choice == 1:
    print('\n\033[1;33mScissors cuts paper!\033[m')
    animate('\033[1;32m\nYOU WIN!\n\033[m')
    playsound(r'C:\Windows\Media\tada.wav')
else:
    print('\n\033[1;33mRock smashes scissors!\033[m')
    playsound(r'C:\Windows\Media\ringout.wav')
    animate('\033[1;31m\nYOU LOSE!\n\033[m')

animate('\033[1;33m==================================================\n\033[m')