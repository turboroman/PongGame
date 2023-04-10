from turtle import Turtle

INITIAL_COR_LEFT = -350
INITIAL_COR_RIGHT = 340


class Rocket(Turtle):
    def __init__(self, side):
        self.side = side
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.shape('square')
        self.shapesize(1, 5)
        self.setheading(90)
        self.penup()
        if self.side == 'left':
            self.goto(INITIAL_COR_LEFT, 0)
            self.color('red')

        elif self.side == 'right':
            self.goto(INITIAL_COR_RIGHT, 0)
            self.color('blue')
        self.showturtle()

    def move_up(self):
        if self.ycor() < 240:
            self.forward(20)

    def move_down(self):
        if self.ycor() > -240:
            self.backward(20)
