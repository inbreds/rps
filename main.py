import random
import time
import os


base_choices = ['rock', 'paper', 'scissors']
# winners = {
#     'rock': 'paper',
#     'scissors': 'rock',
#     'paper': 'scissors'
# } # reference for what beats what

def play_game():
    ai_input = random.choice(base_choices) # randomly chooses input.
    print('rock'); print('paper'); print('scissors')
    user_input = input('> '); os.system('cls')
    if user_input == ai_input:
            print('tie!'); time.sleep(1.5); os.system('cls')

    
    elif ai_input == 'rock':
        if user_input == 'paper':
            print('you have won!'); time.sleep(1.5); os.system('cls')
        else:
            print('you lost try again!'); time.sleep(1.5); os.system('cls')

    elif ai_input == 'scissors':
        if user_input == 'rock':
            print('you have won!'); time.sleep(1.5); os.system('cls')
        else:
            print('you lost try again!'); time.sleep(1.5); os.system('cls')
    
    elif ai_input == 'paper':
        if user_input == 'scissors':
            print('you have won!'); time.sleep(1.5); os.system('cls')
        else:
            print('you lost try again!'); time.sleep(1.5); os.system('cls')


while True:
 play_game()
