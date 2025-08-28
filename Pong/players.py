from turtle import Turtle

UP = 90
DOWN = 270

class Player():

    def __init__(self):
        self.player_1 = self.create_player((-530, 0))
        self.player_2 = self.create_player((530, 0))

    def create_player(self, position):
        player_segment = Turtle("square")
        player_segment.color("white")
        player_segment.penup()
        player_segment.shapesize(stretch_len = 0.8, stretch_wid = 5)
        player_segment.goto(position)
        return player_segment
    
    def up_1(self):
        if self.player_1.ycor() <= 290:
            new_y = self.player_1.ycor() + 10
            self.player_1.sety(new_y)

    def down_1(self):
        if self.player_1.ycor() >= -290:
            new_y = self.player_1.ycor() - 10
            self.player_1.sety(new_y)

    def up_2(self):
        if self.player_2.ycor() <= 290:
            new_y = self.player_2.ycor() + 10
            self.player_2.sety(new_y)

    def down_2(self):
        if self.player_2.ycor() >= -290:
            new_y = self.player_2.ycor() - 10
            self.player_2.sety(new_y)