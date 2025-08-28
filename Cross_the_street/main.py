from turtle import Screen
from turtle_char import Turtle_Char
from game_ui import GameUI
from cars import Cars
from lanes import Lanes
import random

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("grey")
screen.title("Cross the Road")
screen.tracer(0)

turtle_char = Turtle_Char()
game_ui = GameUI()
lanes = Lanes()
cars = Cars()

forward = {"w": False}

def press_w():
    forward["w"] = True

def release_w():
    forward["w"] = False
screen.listen()
screen.onkeypress(press_w, "w")
screen.onkeyrelease(release_w, "w")

screen.update()
screen.listen()

running = True

def game_loop():
    global running
    if not running:
        return

    if random.randint(0,10) == 10:
        cars.spawn_car()
    if forward["w"]:
        turtle_char.move_turtle()

    for car in cars.cars:
        if (abs(turtle_char.xcor() - car.xcor()) < 30):
            if (abs(turtle_char.ycor() - car.ycor()) < 22):
                running = False
                screen.textinput("Heyho", "Do you want to keep playing? 'Yes' or 'No' ")
                game_ui.game_over()

    if turtle_char.ycor() >= 290:
        game_ui.passed()
        cars.increase_speed()
        turtle_char.goto(0, -290)


    cars.move_car()

    screen.update()
    screen.ontimer(game_loop, 20)

game_loop()
screen.mainloop()
