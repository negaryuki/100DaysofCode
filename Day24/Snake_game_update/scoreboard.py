from turtle import Turtle

ALIGNMENTS = "center"
FONT = ("Courier ", 22, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENTS, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.highscore:
            with open("data.txt", "w") as data:
                data.write(f"{self.score}")
        self.highscore = self.score  # Update the highscore
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
