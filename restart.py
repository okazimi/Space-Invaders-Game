# # IMPORTS
# TURTLE IMPORT
from turtle import *


# # RESTART CLASS
# PARENT CLASS: TURTLE
# CHILD CLASS: RESTART
class Restart(Turtle):

    # RESTART
    def __init__(self):
        # INHERIT FROM TURTLE CLASS
        super().__init__()
        # PENUP (MOVE WITHOUT LEAVING TRACKS)
        self.penup()
        # HIDE RESTART PROMPT
        self.hideturtle()
        # MOVE RESTART PROMPT
        self.goto(0, 0)
        # SET PROMPT TEXT COLOR
        self.color("green")

    # UPDATE RESTART PROMPT
    def update_restart_prompt(self, score):
        # CLEAR RESTART PROMPT
        self.clear()
        # UPDATE RESTART PROMPT
        self.write(f"  Game Over ☹️\n   Score: {score}\n Restart? Y/N", align="center", font=("Courier", 20, "bold"))
