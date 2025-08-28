from turtle import Turtle

class Turtle_Char(Turtle):

    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.color("darkgreen")
        self.goto(0, -290)
        self.setheading(90)

    def move_turtle(self):
        self.forward(5)