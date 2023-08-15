# start by creating random_character() function. 

import random

from game_data import data


def random_character():
    character = random.choice(data)

    return(character)        
        
    
def compare_followers():
    
    a_character = random_character() 
    b_character = random_character()
    
    a_followers = a_character['follower_count']
    b_followers = b_character['follower_count']
    
    print(f" Character A : {a_character['name']} , {a_character['description']} from {a_character['country']}")

    print(f" Character B : {b_character['name']} , {b_character['description']} from {b_character['country']}")

    
    game_continue= True
    
    while game_continue:
        guess = input(" Who has more Followers? 'a' or 'b' ")
        
        if a_followers > b_followers and guess == "a":
            b_character = a_character
            return('You are right. Next:')
            
         
        elif a_followers > b_followers and guess == "b":
             return("wrong. You loose")
             game_continue = False
    
        elif a_followers < b_followers and guess == "b":
            b_character = a_character
            return('You are right. Next:')
         
        elif a_followers < b_followers and guess == "a":
             return("wrong. You loose")
             game_continue = False
    
    


print(compare_followers())
