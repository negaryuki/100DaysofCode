#creating. number guessing game

import random

def randomize_number():
  number = random.randint(1,100)
  return number 


def game_fundamental():
    number = randomize_number()
    continue_guess = True 
    
    while continue_guess == True:
        guess = int(input("Enter a number\n"))
        if guess > number:
            print(" You're too high")
            attempt -= 1
        elif guess < number:
            print("You're too low")
            attempt -= 1
        elif guess == number:
            print("You guessed right! You win!")
        elif attempt == 0:
            continue_guess = False
            print("you are out of tries. Game over")
    
            

def game_start():
  game_continue = True
  level = print(input("Welcome to the number guessing game ^o^/ ! your goal is to guess what random number the computer chose between 1 and 100.\n first choose your level. 'hard' or 'easy'?"))

  
  while game_continue == True:
        
      if level == "hard":
        attempt = 5
        game_fundamental()

      elif level == "easy":
        attempt = 10
        game_fundamental()
        
      else:
        print("you entered an invalid input. the game will now restart")
        game_continue = False
        game_start()

      
    
  
game_start()    
