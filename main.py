from turtle import Turtle, Screen
import time

from ball import Ball, INITIAL_BALL_SPEED
from rocket import Rocket
from scoreboard import ScoreBoard

TABLE_WIDTH = 800
TABLE_HEIGHT = 600

table = Screen()
table.setup(TABLE_WIDTH, TABLE_HEIGHT)
table.bgcolor('black')
table.title('Pong')

middle_line = Turtle()
middle_line.hideturtle()
middle_line.goto(0, TABLE_HEIGHT/2 - 60)
middle_line.setheading(270)
middle_line.pencolor('grey')
middle_line.pensize(5)
middle_line.speed('fastest')
while middle_line.ycor() > -(TABLE_HEIGHT/2):
    middle_line.forward(20)
    middle_line.penup()
    middle_line.forward(20)
    middle_line.pendown()

rocket_left = Rocket('left')
rocket_right = Rocket('right')
ball = Ball()

table.listen()
table.onkeypress(rocket_left.move_up, 'w')
table.onkeypress(rocket_right.move_up, 'Up')
table.onkeypress(rocket_left.move_down, 's')
table.onkeypress(rocket_right.move_down, 'Down')

game_is_on = True
scoreboard = ScoreBoard()
while game_is_on:
    table.update()
    ball.move()
    time.sleep(ball.speed_level)

    if -270 >= ball.ycor() or ball.ycor() >= 290:
        ball.jump_from_wall()

    if ball.xcor() > 310 and rocket_right.ycor() - 50 < ball.ycor() < rocket_right.ycor() + 50 or ball.xcor() < -325 \
            and rocket_left.ycor() - 50 < ball.ycor() < rocket_left.ycor() + 50:
        ball.jump_from_rocket()
        ball.speed_level /= 2

    if ball.xcor() > 350:
        scoreboard.right_miss()
        ball.reset_position()
        ball.speed_level = INITIAL_BALL_SPEED

    if ball.xcor() < -350:
        scoreboard.left_miss()
        ball.reset_position()
        ball.speed_level = INITIAL_BALL_SPEED

    if scoreboard.left_score == 3 or scoreboard.right_score == 3:
        game_is_on = False
        middle_line.reset()
        middle_line.hideturtle()
        ball.hideturtle()
        scoreboard.game_over()


table.exitonclick()
