from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_1 = 0
        self.score_2 = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 290)
        self.write(self.score_1, align = "center", font = ("Courier", 36, "normal"))
        self.goto(100, 290)
        self.write(self.score_2, align = "center", font = ("Courier", 36, "normal"))

    def scored_1(self):
        self.score_1 += 1
        self.update_score()

    def scored_2(self):
        self.score_2 += 1
        self.update_score()