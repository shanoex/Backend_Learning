import random
import sys
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
playagain = True
while playagain:
    print('')
    print('Welcome to the rock paper scissors game!')
    print(' Enter 1 for choosing rock,\n 2 for choosing paper, \n 3 for choosing scissors\n')
    playerschoice=int(input('Enter you choice:\n'))
    if playerschoice not in [1,2,3]:
        print('Choose from 1,2,3 only')
        sys.exit()
    computerchoice=random.randint(1,3)
    print("")
    print('computer choice is:', RPS(computerchoice).name)
    print('your choice is:', RPS(playerschoice).name)
    print("")
    if playerschoice == computerchoice:
        print('It is a tie')
    elif (playerschoice == 1 and computerchoice == 3) or (playerschoice == 2 and computerchoice == 1) or (playerschoice == 3 and computerchoice == 2):
        print('yess you win')
    else:
        print('python wins')
    playagain =input('\n Do you want to play again? \n y for yes and n for no\n')
    if playagain.lower() == 'y':
        continue
    else:
        print('\n Thanks for playing!')
        break