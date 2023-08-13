# Global scope

player_health= 10


#----------------------------------------------------------------------
#local scope

def drink_portion():
  portion-strength = 2
  print(player_health)


drink_portion()

#----------------------------------------------------------------------
#there is no block scope in python:


game_level = 3
enemies = ["sceleton","zombie", "alien"]

if game_level < 5:
    new_enemy = enemies[0]
    print(new_enemy)


#----------------------------------------------------------------------
# modifiying Global scope

# we have to use the "global" function in order to modify a global scope BUT,
# It's better to not use it frequently, as it may cause Bugs if not used right.
# instead, we could simply "return" a value to save it and then change it.

def change_enemy():
  global enemies
  enemies.append("hulk")

change_enemy()
print(enemies) 


#---------------------------------------------------------------------

#Global constants:
# Are variables which you define and plan to never change again. such as Pi

PI = 3.14159

# in order to differentiate these constants with variables, we write them all in UpperCase letters 

