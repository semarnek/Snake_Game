import fileinput
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-20, 280)
        self.score = 0

        with open("highscore.txt") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()


    def update_scoreboard(self):
        with open("highscore.txt", mode="w") as data:
            data.write(str(self.high_score))

        self.clear()
        self.write(f"Score: {self.score}\tHigh Score: {self.high_score}", align="center", font=("Courier", 12, "bold"))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.update_scoreboard()



    #def game_over(self):
        #self.goto(0,0)
        #self.write(f"GAME OVER!", align="center",font=("Arial", 24, "bold"))

    def add_Score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_scoreboard()