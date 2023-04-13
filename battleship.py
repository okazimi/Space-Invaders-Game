# # IMPORTS
# TURTLE IMPORT
from turtle import *


# # BATTLESHIP CLASS
# PARENT CLASS: TURTLE
# CHILD CLASS: BATTLESHIP
class Battleship(Turtle):

    # CREATE BATTLESHIP
    def __init__(self):
        # INHERIT FROM TURTLE CLASS
        super().__init__()
        # BATTLESHIP IMAGE FILEPATH
        self.battleship_image = "./static/images/battleship.gif"
        # SET MODE TO PENUP
        self.penup()
        # SET SHAPE
        self.shape(self.battleship_image)
        # SET BATTLESHIP SIZE
        self.shapesize(10, 10, 1)
        # MOVE BATTLESHIP TO START LOCATION
        self.goto(0, -(window_height() - (window_height()*0.65)))
        # SHOW BATTLESHIP
        self.showturtle()

    # MOVE BATTLESHIP TO THE LEFT
    def move_left(self):
        # GET NEW X COORDINATE
        new_x = self.xcor() - 25
        # IF BATTLESHIP HAS NOT REACHED THE LEFT SIDE OF THE SCREEN
        if not self.xcor() <= -window_width()*.45:
            # MOVE BATTLESHIP TO THE LEFT (Y-COORDINATE DOES NOT CHANGE)
            self.goto(new_x, self.ycor())

    # MOVE THE BATTLESHIP TO THE RIGHT
    def move_right(self):
        # GET NEW X COORDINATE
        new_x = self.xcor() + 25
        # IF BATTLESHIP HAS NOT REACHED THE RIGHT SIDE OF THE SCREEN
        if not self.xcor() >= window_width()*.45:
            # MOVE BATTLESHIP TO THE RIGHT (Y-COORDINATE DOES NOT CHANGE)
            self.goto(new_x, self.ycor())

    # RESET BATTLESHIP
    def reset_battleship(self):
        # HIDE BATTLESHIP
        self.hideturtle()
        # MOVE BATTLESHIP TO START LOCATION
        self.goto(0, -(window_height() - (window_height()*0.65)))
        # SHOW BATTLESHIP
        self.showturtle()
