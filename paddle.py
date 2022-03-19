from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        new_y = self.ycor() + 20
        self.setpos(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.setpos(self.xcor(), new_y)

    def draw_dashed_line(self):
        self.pensize(3)
        for i in range(100):
            self.pendown()
            self.seth(90)
            self.forward(20)
            self.penup()
            self.forward(20)
