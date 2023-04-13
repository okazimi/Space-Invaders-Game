# # IMPORTS
# TURTLE IMPORT
from turtle import *


# # LIVES CLASS
# PARENT CLASS: TURTLE
# CHILD CLASS: LIVES
class Lives(Turtle):

    # CREATE LIVES TRACKER
    def __init__(self):
        # INHERIT FROM TURTLE CLASS
        super().__init__()
        # BATTLESHIP IMAGE FILE PATH
        self.battleship_image = "./static/images/battleship.gif"
        # INCREMENTAL X-POSITION
        self.life_x = -50
        # LIVES ARRAY
        self.lives = []
        # GIVE USER THREE LIVES
        for i in range(3):
            # INITIALIZE LIFE INSTANCE
            self.life = Turtle()
            # HIDE LIFE
            self.life.hideturtle()
            # PENUP LIFE (MOVE LIFE WITHOUT LEAVING TRACKS)
            self.life.penup()
            # SET LIFE SHAPE
            self.life.shape(self.battleship_image)
            # MOVE LIFE
            self.life.goto(self.life_x, (window_height()*0.46))
            # INCREMENT LIFE X-POSITION
            self.life_x += 50
            # APPEND LIFE TO LIVES ARRAY
            self.lives.append(self.life)
            # SHOW LIFE
            self.life.showturtle()

    # REMOVE A LIFE
    def remove_life(self):
        # REMOVE A LIFE
        self.lives.pop().hideturtle()
