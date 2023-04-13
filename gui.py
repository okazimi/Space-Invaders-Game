# # IMPORTS
# TURTLE IMPORT
from turtle import *


# # GUI CLASS
# PARENT CLASS: TURTLE
# CHILD CLASS: GUI
class Gui(Turtle):

    # CREATE GUI
    def __init__(self):
        # INHERIT FROM TURTLE CLASS
        super().__init__()
        # BATTLESHIP IMAGE FILEPATH
        self.battleship_image = "./static/images/battleship.gif"
        # INVADERS IMAGE FILEPATH
        self.invader_image = "./static/images/invaders.gif"
        # INITIALIZE SCREEN INSTANCE
        self.gui = Screen()
        # ADD BATTLESHIP IMAGE TO GUI
        self.gui.addshape(self.battleship_image)
        # ADD INVADER IMAGE TO GUI
        self.gui.addshape(self.invader_image)
        # ADD MISSILE SHAPE TO GUI
        self.gui.addshape("rectangle", ((-5, 15), (5, 15), (5, -15), (-5, -15)))
        # SET GUI SIZE (FULL SCREEN)
        self.gui.setup(width=1.0, height=1.0)
        # SET GUI BACKGROUND COLOR
        self.gui.bgcolor("black")
        # SET GUI TITLE
        self.gui.title("Space Invaders")

    # GUI GETTER
    def get_gui(self):
        # RETURN CREATED GUI INSTANCE
        return self.gui
