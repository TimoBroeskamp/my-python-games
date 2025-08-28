from turtle import Turtle

FONT = ("Corious", 36, "bold")

class GameUI():

    def __init__(self):
        self.current_level = 0
        self.level = Turtle()
        self.level.penup()
        self.level.hideturtle()
        self.level.goto(0, 250)
        self.level.write(arg = f"Level: {self.current_level}", align = "center", font = ("Corious", 16, "normal"))

        self.lost = Turtle()
        self.lost.hideturtle()
        self.lost.penup()

    def passed(self):
        self.current_level += 1
        self.level.clear()
        self.level.write(arg = f"Level: {self.current_level}", align = "center", font = ("Corious", 16, "normal"))

    def game_over(self):

        self.lost.goto(0, 50)
        self.lost.color("black")
        self.lost.write(arg = "GAME OVER", align = "center", font = FONT)

