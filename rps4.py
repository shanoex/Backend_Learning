import random
import sys
from enum import Enum

game_counter=0

def finc_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    print('')
    print('Welcome to the rock paper scissors game!')
    print(' Enter 1 for choosing rock,\n 2 for choosing paper, \n 3 for choosing scissors\n')
    playerschoice=int(input('Enter you choice:\n'))
    if playerschoice not in [1,2,3]:
        print('Choose from 1,2,3 only')
        return finc_rps()
    computerchoice=random.randint(1,3)
    print("")
    print('computer choice is:', RPS(computerchoice).name)
    print('your choice is:', RPS(playerschoice).name)
    print("")
    def decide_winner(playerschoice, computerchoice):
        if playerschoice == computerchoice:
            return 'It is a tie'
        elif (playerschoice == 1 and computerchoice == 3) or (playerschoice == 2 and computerchoice == 1) or (playerschoice == 3 and computerchoice == 2):
            return 'yess you win'
        else:
            return 'python wins'
    game_result = decide_winner(playerschoice, computerchoice)
    print(game_result)
        
    global game_counter
    game_counter+=1
    print(f'you have played {game_counter} games')

    print("\n Do you want to play again?")

    
    while True:
        playagain =input(' \n y for yes and n for no\n')
        if playagain.lower() not in ['y','n']:
            continue
        else:
            break
    if playagain.lower() == 'y':
        return finc_rps()    
    else:
        print('\n Thanks for playing!')
        sys.exit("Bye have a great day!")

finc_rps()