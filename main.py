from turtle import Screen
import time
from paddle import Paddle
from pongball import PongBall
from scoreboard import Scoreboard

screen = Screen()
screen.title("Pong Game")
screen.screensize(canvwidth=600, canvheight=600, bg="midnight blue")
screen.tracer(0)

right_paddle = Paddle()
right_paddle.color("red")
right_paddle.setpos(350, 0)

left_paddle = Paddle()
left_paddle.color("green")
left_paddle.setpos(-350, 0)

dashed_line = Paddle()
dashed_line.setpos(0, -380)
dashed_line.draw_dashed_line()

pongball = PongBall()

scoreboard = Scoreboard()

screen.listen()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

should_move = True

while should_move:

    screen.update()
    time.sleep(pongball.move_speed)
    # print(pongball.move_speed)
    screen.tracer(1)
    pongball.move_ball()

    # Detect Collisions with Top and Bottom Walls
    if pongball.ycor() > 300 or pongball.ycor() < -300:
        # Needs to Bounce in Vertical Direction
        pongball.bounce_ball_y()

    # Detect Collisions with Right Paddle
    if pongball.distance(right_paddle) < 50 and pongball.xcor() > 320:
        # Needs to bounce in Horizontal Direction
        pongball.bounce_ball_x()

    # Detect Collisions with Left Paddle
    if pongball.distance(left_paddle) < 50 and pongball.xcor() < -320:
        # Needs to bounce in Horizontal Direction
        pongball.bounce_ball_x()

    # Detect if the ball has reached the right edge of the screen
    if pongball.xcor() > 350:
        screen.tracer(0)
        pongball.restart_round()
        scoreboard.left_point()
        screen.update()

    # Detect if the ball has reached the left edge of the screen
    if pongball.xcor() < -350:
        screen.tracer(0)
        pongball.restart_round()
        scoreboard.right_point()
        screen.update()

    # Display Game Over Screen if either of the players reach a score of 10
    if scoreboard.left_score > 9 or scoreboard.right_score > 9:
        scoreboard.setpos(0, 0)
        scoreboard.write("Game Over.", align="center", font=("courier", 60, "bold"))
        should_move = False

screen.exitonclick()
