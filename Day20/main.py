import time
from turtle import Turtle, Screen
from snake import Snake

# setup Screen:

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turns off the animation, however, in order to see anything, we need to use the update method later


snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()  # update screen in order to show snake
    time.sleep(0.1)

    snake.move()






screen.exitonclick()
