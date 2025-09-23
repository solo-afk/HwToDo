# IMPORTS -------------------------------------------------------------------------
import sys  
import random  
import time 
import os  

if os.name == 'nt':  
    clear_command = 'cls'  
else:
    clear_command = 'clear' 

# FUNCTION DEFS -------------------------------------------------------------------------
def clear():
    os.system(clear_command)

def typewriter_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)  
        sys.stdout.flush() 
        time.sleep(delay) 
    print()  

def play_game(user_move):
  
    global user_win_count, ai_win_count 

    while user_move != 'exit': 
        clear()  
        if user_move not in valid_moves:  
            typewriter_effect('Invalid move. Select again.')
            user_move = input("Please select 'rock', 'paper', or 'scissors': \n").lower()
            continue 

        ai_move = random.choice(valid_moves) 
        check_moves(user_move, ai_move) 
        display_moves(user_move, ai_move) 

        time.sleep(1) 

        typewriter_effect("\nPlease select 'rock', 'paper', or 'scissors'. Type 'exit' to quit.")
        user_move = input("").lower() 

    clear() 
    thanks_for_playing() 

def thanks_for_playing():
   
    typewriter_effect('Thanks so much for playing!')
    for i in range(4):  
        typewriter_effect('🤣😉')  
        time.sleep(.1) 

def display_moves(user_move, ai_move):
   
    global user_win_count, ai_win_count  

    print()
    print('----------------------')
    print(f'You: {moves[user_move]}') 
    print(f'AI: {moves[ai_move]}') 
    print(f'The score is currently: You: {user_win_count} vs. AI: {ai_win_count}')  
    print('----------------------')
    print()

def check_moves(user_move, ai_move):
    global user_win_count, ai_win_count  

    if user_move == ai_move: 
        typewriter_effect("It's a tie!")
    elif (user_move == 'rock' and ai_move == 'scissors') or (user_move == 'paper' and ai_move == 'rock') or (user_move == 'scissors' and ai_move == 'paper'):
        typewriter_effect("User wins!")  
        user_win_count += 1  
    else:
        typewriter_effect("AI wins") 
        ai_win_count += 1 

# MAIN -------------------------------------------------------------------------
user_win_count = 0
ai_win_count = 0  

moves = {'rock': '🪨', 'paper': '📜', 'scissors': '✂️'} 
valid_moves = list(moves.keys()) 

clear() 
typewriter_effect('~~~~~~~~~~~~~~~~~~~~~~~~')
typewriter_effect('Welcome to Rock, Paper, Scissors! Enter your move, or type \'exit\' to quit.')
user_move = input("").lower()  

play_game(user_move) 
