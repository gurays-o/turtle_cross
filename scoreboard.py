from turtle import Turtle

ALIGN = "left"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-285, 265)
        self.level = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=("Courier", 20, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 14, "bold"))
