
#?Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, 
#?print out a message of congratulations to the winner, and ask if the players want to start a new game)

#?Remember the rules:
#?Rock beats scissors
#?Scissors beats paper
#?Paper beats rock

import random

print('''
----------Rock-Paper-Scissors game----------
Please select one of the selection below by entering them in the text field.

1. Rock
2. Paper
3. Scissors  
''')

stop = False

while(not stop):
    
    answerP1 = input('Player 1: Please type your choice: Rock, Paper or Scissors:')
    
    answerP2 = input('Player 2: Please type your choice: Rock, Paper or Scissors:')

    #comparing the responses according to the Rock-Paper-Scissors game rule
    if answerP1 == answerP2:
        print('DRAW GAME')
    elif answerP1 == 'Rock' and answerP2 == 'Paper':
        print('PLAYER 2 WINS')
    elif answerP1 == 'Rock' and answerP2 == 'Scissors':
        print('PLAYER 1 WINS')
    elif answerP1 == 'Paper' and answerP2 == 'Rock':
        print('PLAYER 1 WINS')
    elif answerP1 == 'Paper' and answerP2 == 'Scissors':
        print('PLAYER 2 WINS')
    elif answerP1 == 'Scissors' and answerP2 == 'Rock':
        print('PLAYER 2 WINS')
    elif answerP1 == 'Scissors' and answerP2 == 'Paper':
        print('PLAYER 1 WINS')
    else:
        print('Wrong answer, please type Rock, Paper or Scissors in your next attempt!')    
    
    #asking to the user if he wants to start a new game or cancel
    answer = input('Do you want to start a new game? (Yes or No)')
    
    #asking to the user if he wants to start a new game or cancel
    if answer == 'Yes':
        print('New game will start')
    elif answer == 'No':
        stop = True
        print('GAME OVER')
    else:
        print('Wrong answer, please type Yes or No in your next attempt!')    