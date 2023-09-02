import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# setup Screen:

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turns off the animation, however, in order to see anything, we need to use the update method later

snake = Snake()
food = Food()
scoreboard = Scoreboard ()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()  # update screen in order to show snake
    time.sleep(0.1)
    snake.move()

    # Detect snake collision with food
    if snake.head.distance(food) < 15:
        food.refresh()         # reposition food
        snake.extend()  # add a new segment for each food
        scoreboard.increase_score()

    # Detect snake collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()





screen.exitonclick()
