import time
from turtle import Turtle

class Scoreboard(Turtle):
    WINNING_SCORE = 5  

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.draw_center_line()
        self.update_scoreboard()

    def draw_center_line(self):
        self.pencolor("green")  
        self.goto(0, 300)
        self.setheading(270)
        for _ in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        self.pencolor("white")  

    def update_scoreboard(self):
        self.clear()
        self.draw_center_line()
        self.color("red")
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 40, "bold"))
        self.color("blue")
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 40, "bold"))

    def l_point(self):
        self.left_score += 1
        self.update_scoreboard()
        if self.left_score >= self.WINNING_SCORE:
            self.game_over("Left Player Wins!")

    def r_point(self):
        self.right_score += 1
        self.update_scoreboard()
        if self.right_score >= self.WINNING_SCORE:
            self.game_over("Right Player Wins!")

    def game_over(self, winner):
        self.goto(0, 0)
        self.color("green")
        self.write(winner, align="center", font=("Courier", 30, "bold"))

        from turtle import Screen  
        screen = Screen()
        screen.update()  

        time.sleep(2)  
        self.reset_game() 

    def reset_game(self):
        self.clear()  
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()
