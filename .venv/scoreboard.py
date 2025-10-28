from turtle import Turtle
from snake import Snake



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 3
        self.hearts = "❤❤❤❤❤❤❤❤❤❤"
        # self.highscore = 0
        # with open("data.txt") as data:
        #     self.highscore = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def reset(self):
        # if self.score > self.highscore:
        #     self.highscore = self.score
        #     with open("data.txt", mode="w") as data:
        #         data.write(str(self.highscore))
        self.score = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Snake Length: {self.score} | Snake Hearts: {self.hearts}", move=False, align='center', font=('Courier', 13, 'normal'))


    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def loss_heart(self):
        self.hearts = self.hearts[:-1]
        self.update_scoreboard()
        self.reset()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game over!", align="center", font=("Courier", 36, "normal"))