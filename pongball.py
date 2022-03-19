from turtle import Turtle
import random

MOVE_SPEED = 0.1

class PongBall(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("orange")
        self.speed("normal")
        self.x_move = random.randint(1, 10)
        self.y_move = 10
        self.move_speed = MOVE_SPEED

    def move_ball(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.setpos(x_pos, y_pos)

    def bounce_ball_y(self):
        self.y_move *= -1
        self.move_speed *= 0.5

    def bounce_ball_x(self):
        self.x_move *= -1
        self.move_speed *= 0.5

    def restart_round(self):
        self.setpos(0, 0)
        self.bounce_ball_x()
        # self.move_speed = MOVE_SPEED
