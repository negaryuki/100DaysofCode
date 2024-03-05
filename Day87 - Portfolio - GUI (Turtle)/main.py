import turtle
import random


# ----------- Setup Screen ----------------
screen= turtle.screen()
screen.title("Breakout Game")
screen.bgcolor("Black")
screen.setup(width=600, height=600)

# ----------- Create Paddle ---------------

paddle= turtle.Turtle()
paddle.shape("square")
paddle.color("pink")
paddle.shapesize(strech_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0,-250)

# ----------- Create Ball ----------------

ball = turtle.Turtle()
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.yx = -2

# ----------- Create Bricks ----------------

bricks = []
colors = ["#FFDE59","#EF1515","#00CCE5","#CB6CE6","#8ABF94"]

for i in range(5):
  brick = turtle.Turtle()
  brick.shape("Square")
  brick.color(colors[i])
  brick.penup()
  brick.goto(-200,250 - i * 25)
  bricks.append(brick)
  
# ----------- Create Score ----------------

score = 0
score_display = turtle.Turtle()
score_display.speed(0).  # the turtle will update without any animation 
score_display.color("white")
score.display.penup()
score_display.hideturtle(). # hide turtle cursor
score_display.goto(0,260)
score_display.write("Score: {}".format(score).align="center", font=("Courier",24,"normal"))

# ----------- Functions ----------------
