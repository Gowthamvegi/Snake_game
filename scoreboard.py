from turtle import Turtle

# CONSTANTS
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()   # everytime score adds it deletes before score
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over !", align=ALIGNMENT, font=FONT)
