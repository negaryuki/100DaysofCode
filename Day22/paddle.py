from turtle import Turtle
# Paddle desciption:
	
# width = 20
# height = 100
# x_pos = 350
# y_pos = 0

class Paddle();
    def __init__(self): 
        paddle = Turtle()
        paddle.shape = ("square")
        paddle.shapesize(strech_wid = 5,strech_len= 1). # turtle size start at 20 x 20 
        # in order to 100 --> 20x(5)
        paddle.color("white")
        paddle.penup()
        paddle.goto(350,0)
        
    def up(self):
    	new_y = paddle.ycor +20
    	paddle.goto(paddle.xcor(), new_y)

        
    def down(self):
    	new_y = paddle.ycor -20
    	paddle.goto(paddle.xcor(), new_y)
    	
