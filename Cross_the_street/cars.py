from turtle import Turtle
import random

class Cars():

    def __init__(self):
        self.cars = []
        self.speed = 8

    def spawn_car(self):
        car = Turtle("square")
        car.shapesize(stretch_len=1.7, stretch_wid=1)
        car.penup()
        car.color(random.choice(["red", "green", "blue", "pink", "orange"]))
        car.setheading(180)
        car.goto(400, random.randint(-7, 7) * 30)
        self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.forward(self.speed)

        for car in self.cars[:]:
            if car.xcor() < -400:
                car.hideturtle()
                self.cars.remove(car)

    def increase_speed(self):
        self.speed += 2