from turtle import Turtle

class Lanes():

    def __init__(self):
        self.paint_lanes()

    
    def paint_lanes(self):
        for i in range(0, 16):
            for j in range(0, 30):
                marker = Turtle("square")
                marker.penup()              
                marker.color("white")
                marker.shapesize(stretch_len=0.5, stretch_wid=0.05)
                if i % 2 == 0:
                    marker.goto(440 - (40 * j), -225 + (30 * i))
                else:
                    marker.goto(420 - (40 * j), -225 + (30 * i))