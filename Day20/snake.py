from turtle import Turtle

# Step 1: Create a snake:

# These are constants and are reachable throughout the class
SEGMENT_DISTANCE = [(0, 0), (-20, 0), (-40, 0)]  # create a tuple to define snake segments location
MOVE_DISTANCE = 20  # we create constants so that in case we want to make changes in the games option
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# we merely access it through the start of the code rather than the whole code body

class Snake:

    def __init__(self):
        self.snake = []  # create an empty list to hold the segments later on
        self.create_snake()  # method to create a snake
        self.head = self.snake[0]

    def create_snake(self):
        for position in SEGMENT_DISTANCE:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)  # in the for loop before
        self.snake.append(segment)

    def extend(self):
        self.add_segment(self.snake[-1].position())  # position is a method of the Turtle class

    def move(self):
        for seg in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg - 1].xcor()
            new_y = self.snake[seg - 1].ycor()
            self.snake[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Define methods to control the snake with arrow keys
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)  # Set the snake's heading to 90 degrees (upward)
            self.move()

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)  # Set the snake's heading to 270 degrees (downward)
            self.move()

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)  # Set the snake's heading to 180 degrees (leftward)
            self.move()

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)  # Set the snake's heading to 0 degrees (rightward)
            self.move()
