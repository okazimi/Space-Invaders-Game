# # IMPORTS
# TURTLE IMPORT
from turtle import *


# # SCORE CLASS
# PARENT CLASS: TURTLE
# CHILD CLASS: SCORE
class Score(Turtle):

    # CREATE SCOREBOARD
    def __init__(self):
        # INHERIT FROM TURTLE CLASS
        super().__init__()
        # PENUP SCOREBOARD (MOVE SCOREBOARD WITHOUT LEAVING TRACKS)
        self.penup()
        # HIDE SCOREBOARD
        self.hideturtle()
        # MOVE SCOREBOARD
        self.goto(0, (window_height()*0.35))
        # SET SCOREBOARD COLOR
        self.color("green")
        # INITIALIZE SCORE VARIABLE
        self.score = 0
        # UPDATE SCOREBOARD
        self.update_scoreboard()

    # UPDATE SCOREBOARD
    def update_scoreboard(self):
        # CLEAR SCOREBOARD
        self.clear()
        # UPDATE SCORE
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "bold"))

    # INCREASE SCORE
    def increase_score(self):
        # INCREASE SCORE BY 100
        self.score += 100
        # UPDATE SCOREBOARD
        self.update_scoreboard()
