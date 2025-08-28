from turtle import Turtle, Screen
from players import Player
from line import Line
from ball import Pongball
from score import Score

MAX_ANGLE = 10

screen = Screen()
screen.setup(width = 1100, height = 700)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
screen.listen()

line = Line()
player = Player()
pongball = Pongball()
score = Score()
screen.update()

keys = {"Up": False, "Down": False, "w": False, "s": False}

def press(key): 
    keys[key] = True

def release(key): 
    keys[key] = False

for key in keys:
    screen.onkeypress(lambda k = key: press(k), key)
    screen.onkeyrelease(lambda k = key: release(k), key)

def game_loop():
    if keys["Up"]: player.up_2()
    if keys["Down"]: player.down_2()
    if keys["w"]: player.up_1()
    if keys["s"]: player.down_1()

    if (pongball.ball.xcor() >= 520) and (player.player_2.ycor() - 55 < pongball.ball.ycor() < player.player_2.ycor() + 55):
        offset = pongball.ball.ycor() - player.player_2.ycor()
        pongball.dy = (offset/50)*MAX_ANGLE
        pongball.dx *= -1

    if (pongball.ball.xcor() <= -520) and (player.player_1.ycor() - 55 < pongball.ball.ycor() < player.player_1.ycor() + 55):
        offset = pongball.ball.ycor() - player.player_1.ycor()
        pongball.dy = (offset/50)*MAX_ANGLE
        pongball.dx *= -1

    if pongball.ball.xcor() >= 550:
        score.scored_1()
        pongball.reset_position()

    if pongball.ball.xcor() <= -550:
        score.scored_2()
        pongball.reset_position()

    
    pongball.ball_movement()

    screen.update()
    screen.ontimer(game_loop, 10)

game_loop()
screen.mainloop()
