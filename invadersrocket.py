# # IMPORTS
# TURTLE IMPORT
from turtle import *


# # INVADERS ROCKET CLASS
# PARENT CLASS: TURTLE
# CHILD CLASS: INVADERS ROCKET
class InvadersRocket(Turtle):

    # CREATE INVADERS ROCKET
    def __init__(self):
        # INHERIT FROM TURTLE CLASS
        super().__init__()
        # HIDE ROCKET
        self.hideturtle()
        # SET ROCKET COLOR
        self.color("red")
        # SET ROCKET SHAPE
        self.shape("rectangle")
        # SET ROCKET SPEED
        self.speed("fastest")
        # ROTATE ROCKET
        self.setheading(270)
        # SET ROCKET SIZE
        self.shapesize(0.5, 0.5)
        # ROCKET PENUP (MOVE ROCKET WITHOUT LEAVING TRACKS)
        self.penup()
