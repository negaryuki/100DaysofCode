# create a virtual coin toss program. it will randomly tell the user "Heads or "Tails"

import random

random = random.randint(0, 1)

print(random)

if random == 1:
    print("Heads")
else:
    print("Tails")