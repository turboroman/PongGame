from turtle import Turtle

FIRST_BALL_ANGLE = 100
INITIAL_BALL_SPEED = 0.05


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue violet')
        self.x_move = 10
        self.y_move = 10
        self.speed_level = INITIAL_BALL_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def jump_from_wall(self):
        self.y_move *= -1

    def jump_from_rocket(self):
        self.x_move *= -1

    def reset_position(self):
        self.hideturtle()
        self.speed(10)
        self.goto(0, 0)
        self.showturtle()
        self.speed(1)
        self.jump_from_rocket()
