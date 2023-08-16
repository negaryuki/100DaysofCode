import random
import os
from game_data import data
from art import logo


def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')


def random_character():
    character = random.choice(data)

    return(character)        
        
        
        
def return_celebrity_info(data_dic):
    
    return f"{data_dic['name']}, a {data_dic ['description']} from {data_dic['country']}"




def decide_winner(A_followers , B_followers):
    
    A_followers = A_followers['follower_count']
    B_followers = B_followers['follower_count']
    
    if A_followers > B_followers:
        return 'a'
    else:
        return 'b'
        
        
def game_setup(A_character , B_character):

    print(logo)
    print(f'A Character is : {return_celebrity_info(A_character)}')
    print("vs")
    print(f'B character is : {return_celebrity_info(B_character)}')
    
    
    
game_over = False
game_score = 0


A_character = random_character()
B_character = random_character()

if A_character == B_character:
    B_character = random_character()
    
      
while not game_over:

    clear_console()
    game_setup(A_character,B_character)
    guess = input(" Who has more Followers? 'a' or 'b' ").lower()
    correct_answer = decide_winner(A_character, B_character)
        
    if guess == correct_answer:
        game_score += 1
        print (f"You are right. Your score: {game_score} Next is:")
        
        if correct_answer == 'b':
            
            A_character = B_character
            B_character =random_character()
        
        else:
            B_character = random_character()
                    
    else:
        game_over = True
        print (f"You are wrong. Your final score: {game_score}")
