from turtle import Screen
from turtle_char import Turtle_Char
from game_ui import GameUI
from cars import Cars
from lanes import Lanes
import random
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("grey")
screen.title("Cross the Road")
screen.tracer(0)

turtle_char = Turtle_Char()
game_ui = GameUI()
lanes = Lanes()
cars = Cars()

forward = False

def press_w():
    global forward
    forward = True

def release_w():
    global forward
    forward = False

screen.listen()
screen.onkeypress(press_w, "w")
screen.onkeyrelease(release_w, "w")

screen.update()
screen.listen()

def ask_replay():
    replay_game = screen.textinput("Heyho", "Do you want to keep playing? 'Yes' or 'No' ").lower()
    if replay_game == "yes":
        restart_game()
    else:
        screen.bye()

def restart_game():
    game_ui.current_level = 0
    game_ui.level.clear()
    game_ui.level.write(arg = f"Level: {game_ui.current_level}", align = "center", font = ("Corious", 16, "normal"))
    for car in cars.cars:
        car.hideturtle()
    cars.cars = []
    cars.speed = 8
    game_ui.lost.clear()
    turtle_char.goto(0, -290)
    global running
    running = True

    screen.listen()
    screen.onkeypress(press_w, "w")
    screen.onkeyrelease(release_w, "w")

    game_loop()
    


running = True

def game_loop():
    global forward
    global running
    if not running:
        return

    if random.random() < 0.1:
        cars.spawn_car()
    if forward:
        turtle_char.move_turtle()

    for car in cars.cars:
        if (abs(turtle_char.xcor() - car.xcor()) < 30):
            if (abs(turtle_char.ycor() - car.ycor()) < 22):
                running = False
                game_ui.game_over()
                screen.ontimer(ask_replay, t = 2000)


    if turtle_char.ycor() >= 290:
        game_ui.passed()
        cars.increase_speed()
        turtle_char.goto(0, -290)


    cars.move_car()

    screen.update()
    screen.ontimer(game_loop, 20)

game_loop()
screen.mainloop()