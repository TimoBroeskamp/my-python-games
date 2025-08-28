from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(height = 600, width = 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.05)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.scored()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_on = False
            scoreboard.game_over()

        

screen.exitonclick()