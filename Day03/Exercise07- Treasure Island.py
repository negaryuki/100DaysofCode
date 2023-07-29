# find the tresure in tresure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')


print("Welcome to Treasure Island\n Your Mission is to find the treasure that is hidden in this Island")

left_right = (input("You reached a crossroad, which way will you go? left or right?")).lower()


swim_wait = "st"
door = "st"

# left_right_lower = left_right.lower()
# swim_wait_lower = swim_wait.lower()
# door_lower = door.lower()

if left_right == "left":
    swim_wait = (input("Good. you go further inside a forest and eventually reach a lake, will you wait or swim?")).lower()
    if swim_wait == "wait":
        door = (input("wonderful. After passing a huge oak tree, you will face three doors. which one will you choose? Yellow, Blue or Red?")).lower()
        if door == "yellow":
            print("You win")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game over")
