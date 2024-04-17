import turtle
import random

# ----------- Setup Screen ----------------
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("Black")
screen.setup(width=600, height=600)
screen.tracer(0)  # Disable automatic screen updates

# ----------- Create Paddle ---------------

paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("pink")
paddle.shapesize(1, 5)
paddle.penup()
paddle.goto(0, -250)

# ----------- Create Ball ----------------

ball = turtle.Turtle()
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 2  # the ball will move 2 units to the right in each frame of the game loop
ball.dy = -2  # he ball will move 2 units downward in each frame of the game loop

# ----------- Create Bricks ----------------

bricks = []
colors = ["#FFDE59", "#EF1515", "#00CCE5", "#CB6CE6", "#8ABF94"]

# Define the number of rows and columns of bricks:
rows = 8      # as you desire
columns = 10  # as you desire

# Define the starting position of the first brick
start_x = -200
start_y = 250

# Define the spacing between bricks
brick_spacing_x = 50
brick_spacing_y = 25

for r in range(rows):
    for c in range (columns):
        brick = turtle.Turtle()
        brick.shape("square")
        #brick.color(colors[r % len(colors)])  Cycle through colors repeatedly
        brick_color = random.choice(colors)  # random colors
        brick.color(brick_color)
        brick.penup()
        brick.goto(start_x + c * brick_spacing_x, start_y - r * brick_spacing_y)
        bricks.append(brick)
        bricks.append(brick)

# ----------- Create Score ----------------

score = 0
score_display = turtle.Turtle()
score_display.speed(0)  # the turtle will update without any animation
score_display.color("white")
score_display.hideturtle()  # hide turtle cursor
score_display.penup()
score_display.goto(0, 260)
score_display.write("Score: {}".format(score), font=("Courier", 24, "normal"))


# ----------- Functions ----------------

# Function to move Paddle Left

def move_left():
    x = paddle.xcor()  # retrieve current x coordinate of paddle

    if x > -240:
        x -= 20
        paddle.setx(x)


# Function to move Paddle Right

def move_right():
    x = paddle.xcor()

    if x < 240:
        x += 20
        paddle.setx(x)


# ----------- Keyboard Binding ----------------

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")


# ----------- Main Game Loop ----------------

def game_loop():
    global score
    screen.update()  # Manually update screen

    # Move Ball:
    # ball.xcor() ----> Current x position of ball
    # ball.dx()   ----> Velocity along x of ball per frame

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check Boarders:
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1  # Reverse xcor direction

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1  # Reverse ycor direction

    # Paddle and Ball Collision:

    # check if ball is near paddle in ycor between -240 and -250:
    # check if ball is near paddle in xcor considering the paddle's length:
    if (-240 > ball.ycor() > -250) and ((ball.xcor() < paddle.xcor() + 50) and (ball.xcor() > paddle.xcor() - 50)):
        ball.dy *= -1  # the ball collided with the paddle --> reverse ball direction (upward)

    # Ball and Brick Collision:

    for brick in bricks:
        if brick.distance(ball) < 20:
            # brick.goto(5000,5000)  we could move the brick out of sight
            # or the more efficient way is to delete it as follows:
            brick.hideturtle()  # First hide it
            bricks.remove(brick)  # Remove the brick from the list
            ball.dy *= -1
            score += 1
            score_display.clear()  # Clear Previous score
            score_display.write(f"Score: {score}", font=("Courier", 24, "normal"))

    # GAME OVER CONDITION:

    # if player loses (ball didn't hit the paddle)
    if ball.ycor() < -290:
        ball.dx = 0   # Stop the ball
        ball.dy = 0
        score_display.goto(0, 0)
        score_display.write("Game Over!", align="center", font=("Courier", 30, "normal"))
        screen.update()

    # if Player wins (all bricks are removed)
    elif len(bricks) == 0:
        ball.dx = 0   # Stop the ball
        ball.dy = 0
        score_display.goto(0, 0)
        score_display.write("You Won!", align="center", font=("Courier", 30, "normal"))
        screen.update()

    # Call game_loop() again after a certain delay
    delay_in_milliseconds = 10
    screen.ontimer(game_loop, delay_in_milliseconds)


# Start the game loop
game_loop()

turtle.done()  # keep window open after the game ends
