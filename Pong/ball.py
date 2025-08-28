from turtle import Turtle
import random

class Pongball():

    def __init__(self):
        self.ball = self.create_pongball()

    def create_pongball(self):
        pongball = Turtle("circle")
        pongball.color("white")
        pongball.penup()
        pongball.goto(0, 0)

        self.dx = 5
        self.dy = 5

        return pongball
    
    def ball_movement(self):

        new_x = self.ball.xcor() + self.dx
        new_y = self.ball.ycor() + self.dy
        self.ball.goto(new_x, new_y)

        if self.ball.ycor() >= 340:
            self.dy *= -1        
            
        if self.ball.ycor() <= -340:
            self.dy *= -1

    def reset_position(self):

        self.ball.goto(0, 0)
        self.dy = 5
        self.dx *= -1
