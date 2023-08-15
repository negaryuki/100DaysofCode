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
    


    return(a_followers , b_followers)
    
        
    
print(random_character())
print(compare_followers())
