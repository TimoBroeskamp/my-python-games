from turtle import Turtle

class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.draw_line()

    def draw_line(self):
        for i in range(21):
            line_segment = Turtle("square")
            line_segment.color("white")
            line_segment.penup()
            line_segment.goto(0, -350 + i * 35)
            line_segment.shapesize(stretch_len = 0.1, stretch_wid = 1)