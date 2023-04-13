# # IMPORTS
# TURTLE IMPORT
from turtle import *


# # BATTLESHIP ROCKET CLASS
# PARENT CLASS: TURTLE
# CHILD CLASS: BATTLESHIP ROCKET
class BattleshipRocket(Turtle):

    # CREATE BATTLESHIP ROCKET
    def __init__(self):
        # INHERIT FROM TURTLE CLASS
        super().__init__()
        # HIDE ROCKET
        self.hideturtle()
        # SET ROCKET COLOR
        self.color("green")
        # SET ROCKET SHAPE
        self.shape("rectangle")
        # SET ROCKET SPEED
        self.speed("fastest")
        # ROTATE ROCKET
        self.setheading(90)
        # SET ROCKET SIZE
        self.shapesize(0.5, 0.5)
        # ROCKET PENUP (MOVE ROCKET WITHOUT LEAVING TRACKS)
        self.penup()
