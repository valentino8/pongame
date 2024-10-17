from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.updateScore()

    def updateScore(self):
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("Courier", 50, "italic"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("Courier", 50, "italic"))

    def lscorecount(self):
        self.lscore +=1
        self.clear()
        self.updateScore()

    def rscorecount(self):
        self.rscore +=1
        self.clear()
        self.updateScore()
