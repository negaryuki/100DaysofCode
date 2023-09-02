# Inheritance in Classes:

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhale")


# In order to inherit a class and its methods whe have to use the super() function

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("under water")

    def swim(self):
        print("swimming")


nemo = Fish()
nemo.breathe()
nemo.swim()