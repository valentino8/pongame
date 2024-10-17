from turtle import Screen
from turtle import Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time
screen = Screen()
screen.setup(width=800,height = 600)
screen.bgcolor("black")
screen.title("The Ping Pong Game")
screen.tracer(0)

score = Scoreboard()

ball = Ball((0,0))
paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))


screen.listen()
screen.onkeypress(paddle1.down,"Down")
screen.onkeypress(paddle1.up,"Up")
screen.onkeypress(paddle2.down,"s")
screen.onkeypress(paddle2.up,"w")
game_on = True

while game_on:


    screen.update()
    time.sleep(ball.move_speed)

    ball.move()
    score.updateScore()


    if ball.ycor() < -290 or ball.ycor() > 290:
        ball.bounce_y()
    if ball.distance(paddle1) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    if ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 480:

        ball.ball_reset()
        score.lscorecount()


    if ball.xcor() < -480:
        ball.ball_reset()
        score.rscorecount()






screen.exitonclick()