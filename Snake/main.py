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

keys = {"Up": False, "Right": False, "Down": False, "Left": False}

def press(key): 
    keys[key] = True

def release(key): 
    keys[key] = False

def bind_keys():
    screen.onkeypress(lambda: press("Up"), "Up")
    screen.onkeyrelease(lambda: release("Up"), "Up")

    screen.onkeypress(lambda: press("Down"), "Down")
    screen.onkeyrelease(lambda: release("Down"), "Down")

    screen.onkeypress(lambda: press("Left"), "Left")
    screen.onkeyrelease(lambda: release("Left"), "Left")

    screen.onkeypress(lambda: press("Right"), "Right")
    screen.onkeyrelease(lambda: release("Right"), "Right")
    screen.listen()


bind_keys()

def reset_snake():
    for seg in snake.segments:
        seg.hideturtle()
    snake.segments.clear()
    snake.create_snake()
    snake.head = snake.segments[0]

def ask_replay():
    replay_game = screen.textinput("Heyho", "Do you want to keep playing? 'Yes' or 'No' ").lower()
    if replay_game == "yes":
        restart_game()
    else:
        screen.bye()

def restart_game():
    global running
    running = True
    food.clear()
    food.refresh()

    scoreboard.score = 0
    scoreboard.update_score()

    bind_keys()

    game_on()

running = True

def game_on():
    global running

    if not running:
        return
    
    if keys["Down"]: snake.down()
    if keys["Left"]:snake.left()
    if keys["Right"]: snake.right()
    if keys["Up"]: snake.up()

    screen.update()
    time.sleep(0.05)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.scored()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        running = False
        reset_snake()
        ask_replay()
        

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.game_over()
            running = False
            reset_snake()
            ask_replay()

    screen.update()
    screen.ontimer(game_on, 10)

game_on()
screen.exitonclick()