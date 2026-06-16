import random
import sys
from enum import Enum

def rps(name='PlayerOne'):

    game_counter=0
    player_wins=0
    computer_wins=0

    def finc_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        print('')
        print('Welcome to the rock paper scissors game!')
        print(f' {name}, Enter 1 for choosing rock,\n 2 for choosing paper, \n 3 for choosing scissors\n')
        playerschoice=int(input(f' {name}, Enter your choice:\n'))
        if playerschoice not in [1,2,3]:
            print('Choose from 1,2,3 only')
            return finc_rps()
        computerchoice=random.randint(1,3)
        print("")
        print('computer choice is:', RPS(computerchoice).name)
        print('your choice is:', RPS(playerschoice).name)
        print("")
        def decide_winner(playerschoice, computerchoice):
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins
            if playerschoice == computerchoice:
                return 'It is a tie'
            elif (playerschoice == 1 and computerchoice == 3) or (playerschoice == 2 and computerchoice == 1) or (playerschoice == 3 and computerchoice == 2):
                player_wins += 1
                return f'{name} you win'
            
            else:
                computer_wins += 1
                return f'{name} you lose'
        game_result = decide_winner(playerschoice, computerchoice)
        print(game_result)
        print(f'{name} wins: {player_wins}, Computer wins: {computer_wins}')
            
        nonlocal game_counter
        game_counter+=1
        print(f'{name} have played {game_counter} games')

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
            print(f'\n Thanks for playing {name}!')
            sys.exit("Bye have a great day!")
    return finc_rps


if __name__ == "__main__"   :
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )
    parser.add_argument(
        "-n","--name",metavar="name",required=True,help="The name of the person that is playing."

    )
    
    args=  parser.parse_args()

    rock_paper_scissor=rps(args.name)
    rock_paper_scissor()
