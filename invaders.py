# # IMPORTS
# TURTLE IMPORT
from turtle import *


# # INVADERS CLASS
# PARENT CLASS: TURTLE
# CHILD CLASS: INVADERS
class Invaders(Turtle):

    # CREATE INVADERS
    def __init__(self):
        # INHERIT FROM TURTLE CLASS
        super().__init__()
        # INVADERS IMAGE FILEPATH
        self.INVADERS_IMAGE = "./static/images/invaders.gif"
        # SET INITIAL INVADER X-POSITION TO -0.11 OF THE WINDOW WIDTH
        self.invader_x = window_width() * (-0.11)
        # SET INITIAL INVADER Y-POSITION TO 0.15 OF THE WINDOW HEIGHT
        self.invader_y = window_height() * 0.15
        # CREATE EMPTY INVADER LIST
        self.invaders = []
        # CREATE 21 INVADERS
        for i in range(21):
            # INITIALIZE INVADER INSTANCE
            self.invader = Turtle()
            # SET PEN UP FOR INVADER (NO TRACE MARKS)
            self.invader.penup()
            # SET INVADER SPEED
            self.invader.speed("fastest")
            # HIDE INVADER
            self.invader.hideturtle()
            # SET INVADER SHAPE
            self.invader.shape(self.INVADERS_IMAGE)
            # MOVE INVADER
            self.invader.goto(self.invader_x, self.invader_y)
            # SHOW INVADER
            self.invader.showturtle()
            # FIRST ROW INCREMENTS
            if i < 6:
                # INCREMENT X-POSITION
                self.invader_x += 50
            # SECOND ROW INCREMENTS
            elif i == 6:
                # INCREMENT Y-POSITION
                self.invader_y += 50
            # SECOND ROW DECREMENTS
            elif 7 <= i < 13:
                # DECREMENT X-POSITION
                self.invader_x -= 50
            # THIRD ROW INCREMENTS
            elif i == 13:
                # INCREMENT Y-POSITION
                self.invader_y += 50
            # THIRD ROW INCREMENTS
            elif 21 > i:
                # INCREMENT X-POSITION
                self.invader_x += 50
            # APPEND INVADER TO INVADERS LIST
            self.invaders.append(self.invader)

    # INVADERS GETTER
    def get_invaders(self):
        # RETURN INVADERS
        return self.invaders
