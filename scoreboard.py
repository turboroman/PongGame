from turtle import Turtle
FONT = ('Arial', 30, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.write(f'{self.left_score} : {self.right_score}', align='center', font=FONT)
        self.hideturtle()

    def left_miss(self):
        self.clear()
        self.right_score += 1
        self.write(f'{self.left_score} : {self.right_score}', align='center', font=FONT)

    def right_miss(self):
        self.clear()
        self.left_score += 1
        self.write(f'{self.left_score} : {self.right_score}', align='center', font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        if self.left_score > self.right_score:
            result = 'Player left won'
        elif self.left_score < self.right_score:
            result = 'Player right won'
        else:
            result = 'DRAW'
        self.write(f'{result}'
                   f'\n'
                   f'FINAL SCORE'
                   f'\n'
                   f'{self.left_score} : {self.right_score}', align='center', font=FONT)
