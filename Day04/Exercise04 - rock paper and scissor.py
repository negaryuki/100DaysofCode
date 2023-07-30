# Rock Paper Scissors ASCII Art

Rock = (
    '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

''')

Paper = ('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')

Scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

import random

selection = input("What Do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor")
computer = random.randint(0, 2)

selection = int(selection)

print(computer)

if selection == 0 and computer == 0:
    print(Rock)
    print(f'Computer Chooses {Rock}')
    print(" It's a Draw")
elif selection == 0 and computer == 1:
    print(Rock)
    print(f'Computer Chooses {Scissors}')
    print("You win!")
elif selection == 0 and computer == 2:
    print(Rock)
    print(f'Computer Chooses {Paper}')
    print("You loose!")
elif selection == 1 and computer == 0:
        print(Scissors)
        print(f'Computer Chooses {Rock}')
        print("You loose!")
elif selection == 1 and computer == 1:
        print(Scissors)
        print(f'Computer Chooses {Scissors}')
        print("It's a Draw!")
elif selection == 1 and computer == 2:
        print(Scissors)
        print(f'Computer Chooses {Paper}')
        print("You Win!")
elif selection == 2 and computer == 0:
        print(Paper)
        print(f'Computer Chooses {Rock}')
        print("You Win!")
elif selection == 2 and computer == 1:
        print(Paper)
        print(f'Computer Chooses {Scissors}')
        print("You loose!")
elif selection == 2 and computer == 2:
        print(Paper)
        print(f'Computer Chooses {Paper}')
        print("It's a Draw!")
else:
    print("you added a wrong number")
