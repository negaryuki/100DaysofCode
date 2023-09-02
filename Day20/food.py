from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):  # these are all inherited from the Turtle class
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fast")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        new_random_x = random.randint(-280, 280)
        new_random_y = random.randint(-280, 280)
        self.goto(new_random_x, new_random_y)
