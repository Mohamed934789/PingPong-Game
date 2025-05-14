from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic("background.gif")
screen.title("Ping Pong Game")


r__paddle = Paddle((350, 0), "blue")  
l__paddle = Paddle((-350, 0), "red") 

ball = Ball()
scoreboard = Scoreboard()
screen.tracer(0)



screen.listen()
screen.onkey(r__paddle.go_up, "Up")
screen.onkey(r__paddle.go_down, "Down")
screen.onkey(l__paddle.go_up, "w")
screen.onkey(l__paddle.go_down, "s")

default_sleep = 0.1
game_on = True
while game_on:
    screen.update()
    time.sleep(default_sleep)
    ball.goto(ball.xcor() + ball.x_move, ball.ycor() + ball.y_move)

    if (ball.ycor() >= 280) or (ball.ycor() <= -280):
        ball.y_move *= -1

    if (ball.xcor() >= 330 and ball.distance(r__paddle) <= 50) or (ball.xcor() <= -330 and ball.distance(l__paddle) <= 50):
        ball.x_move *= -1
        default_sleep *= 0.9

    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.x_move *= -1
        default_sleep = 0.1
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.x_move *= -1
        default_sleep = 0.1    
        scoreboard.r_point() 

screen.mainloop()