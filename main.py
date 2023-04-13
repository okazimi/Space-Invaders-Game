# # IMPORTS
# RANDOM IMPORT
import random
# SOUND IMPORT
import winsound
# GUI IMPORT
from gui import Gui
# BATTLESHIP IMPORT
from battleship import Battleship
# BATTLESHIP ROCKET IMPORT
from battleshiprocket import BattleshipRocket
# INVADERS IMPORT
from invaders import Invaders
# INVADERS ROCKET IMPORT
from invadersrocket import InvadersRocket
# SCORE IMPORT
from score import Score
# LIVES IMPORT
from lives import Lives
# RESTART IMPORT
from restart import Restart


# # METHODS
# CREATE GAME ELEMENTS
def create_game_elements():
    # INITIALIZE GUI INSTANCE
    gui = Gui()
    # GET CREATED GUI
    gui = gui.get_gui()
    # INITIALIZE BATTLESHIP INSTANCE
    bs = Battleship()
    # INITIALIZE BATTLESHIP ROCKET INSTANCE
    bs_r = BattleshipRocket()
    # INITIALIZE INVADERS INSTANCE
    inv = Invaders()
    # GET CREATED INVADERS
    inv = inv.get_invaders()
    # INITIALIZE INVADERS ROCKET INSTANCE
    inv_r = InvadersRocket()
    # INITIALIZE SCOREBOARD INSTANCE
    sb = Score()
    # INITIALIZE LIVES INSTANCE
    heart = Lives()
    # INITIALIZE RESTART INSTANCE
    re = Restart()
    # RETURN CREATIONS
    return gui, bs, bs_r, inv, inv_r, sb, heart, re


# FIRE BATTLESHIP ROCKET
def fire_battleship_rocket():
    # REFERENCE GLOBAL VARIABLE
    global BATTLESHIP_ROCKET
    # IF BATTLESHIP ROCKET STATE IS PREPARING
    if BATTLESHIP_ROCKET == "PREPARING":
        # PLAY ROCKET SOUND
        winsound.PlaySound("static/sounds/battleship_laser.wav", winsound.SND_ASYNC)
        # UPDATE ROCKET STATE
        BATTLESHIP_ROCKET = "FIRING"
        # MOVE ROCKET TO BATTLESHIP
        battleship_rocket.setposition(battleship.xcor(), battleship.ycor()+25)
        # SHOW ROCKET
        battleship_rocket.showturtle()


# FIRE INVADER ROCKET
def fire_invader_rocket():
    # REFERENCE GLOBAL VARIABLE
    global INVADER_ROCKET
    # IF INVADER ROCKET STATE IS PREPARING
    if INVADER_ROCKET == "PREPARING":
        # PLAY ROCKET SOUND
        winsound.PlaySound("static/sounds/invader_laser.wav", winsound.SND_ASYNC)
        # UPDATE INVADER ROCKET STATE
        INVADER_ROCKET = "FIRING"
        # SELECT RANDOM INVADER
        selected_invader = random.choice(invaders)
        # MOVE ROCKET TO INVADER
        invaders_rocket.setposition(selected_invader.xcor(), selected_invader.ycor()-25)
        # SHOW INVADERS ROCKET
        invaders_rocket.showturtle()


if __name__ == "__main__":

    # CREATE GAME ELEMENTS
    screen, battleship, battleship_rocket, invaders, invaders_rocket, scoreboard, lives, restart = create_game_elements()

    # # GLOBAL VARIABLES
    # BATTLESHIP ROCKET STATE
    BATTLESHIP_ROCKET = "PREPARING"
    # INVADER ROCKET STATE
    INVADER_ROCKET = "PREPARING"
    # BATTLESHIP ROCKET SPEED
    BATTLESHIP_ROCKET_SPEED = 70
    # INVADER ROCKET SPEED
    INVADER_ROCKET_SPEED = -70
    # INVADER X SPEED
    INVADER_X_SPEED = 15
    # INVADER Y SPEED
    INVADER_Y_SPEED = 0.25

    # LISTEN FOR USER INPUTS
    screen.listen()
    # MOVE BATTLESHIP TO THE RIGHT WITH RIGHT ARROW KEY
    screen.onkey(fun=battleship.move_right, key="Right")
    # MOVE BATTLESHIP TO THE LEFT WITH LEFT ARROW KEY
    screen.onkey(fun=battleship.move_left, key="Left")
    # FIRE BATTLESHIP ROCKETS WITH SPACE BAR
    screen.onkey(fun=fire_battleship_rocket, key="space")

    # WHILE TRUE
    while True:

        # IF USER HAS NO LIVES LEFT
        if len(lives.lives) == 0:
            # FOR EACH INVADER
            for invader in invaders:
                # HIDE THE INVADER
                invader.hideturtle()
            # HIDE THE BATTLESHIP
            battleship.hideturtle()
            # HIDE BATTLESHIP ROCKET
            battleship_rocket.hideturtle()
            # HIDE INVADER ROCKET
            invaders_rocket.hideturtle()
            # RESET SCOREBOARD
            scoreboard.reset()
            # HIDE LIVES
            lives.hideturtle()
            # DISPLAY RESTART PROMPT
            restart.update_restart_prompt(scoreboard.score)
            # DISPLAY TEXT BOX TO CAPTURE USER INPUT
            user_input = screen.textinput("Restart?", "Y/N?")
            # IF USER WANTS TO PLAY AGAIN
            if user_input.lower() == "y":
                # RESET RESTART PROMPT
                restart.reset()
                # CREATE GAME ELEMENTS
                screen, battleship, battleship_rocket, invaders, invaders_rocket, scoreboard, lives, restart = create_game_elements()
                # LISTEN FOR USER INPUTS
                screen.listen()
                # MOVE BATTLESHIP TO THE RIGHT WITH RIGHT ARROW KEY
                screen.onkey(fun=battleship.move_right, key="Right")
                # MOVE BATTLESHIP TO THE LEFT WITH LEFT ARROW KEY
                screen.onkey(fun=battleship.move_left, key="Left")
                # FIRE BATTLESHIP ROCKETS WITH SPACE BAR
                screen.onkey(fun=fire_battleship_rocket, key="space")
            # IF USER DOES NOT WANT TO PLAY AGAIN
            elif user_input.lower() == "n":
                # END GAME
                break
            # INVALID INPUT
            else:
                # ASK USER TO TRY AGAIN
                user_input = screen.textinput("Invalid Input", "Please enter any key to return to previous prompt")

        # FOR EACH INVADER
        for invader in invaders:
            # MOVE THE INVADER
            invader.setposition(invader.xcor() + INVADER_X_SPEED, invader.ycor() - INVADER_Y_SPEED)
            # IF INVADER HAS REACHED RIGHT SIDE OF THE SCREEN
            if invader.xcor() >= (screen.window_width()*0.4):
                # UPDATE INVADER SPEED
                INVADER_X_SPEED *= -1
            # IF INVADER HAS REACHED LEFT SIDE OF THE SCREEN
            elif invader.xcor() <= (screen.window_width() * -0.4):
                # UPDATE INVADER SPEED
                INVADER_X_SPEED *= -1
            # IF BATTLESHIP ROCKET HAS COLLIDED WITH INVADER
            if invader.distance(battleship_rocket) < 40:
                # PLAY SOUND
                winsound.PlaySound("static/sounds/explosion.wav", winsound.SND_ASYNC)
                # HIDE ROCKET
                battleship_rocket.hideturtle()
                # MOVE ROCKET OFF SCREEN
                battleship_rocket.goto(-500, -500)
                # UPDATE BATTLESHIP ROCKET STATE
                BATTLESHIP_ROCKET = "PREPARING"
                # HIDE INVADER
                invader.hideturtle()
                # REMOVE INVADER FROM LIST
                invaders.remove(invader)
                # UPDATE SCORE
                scoreboard.increase_score()
            # IF INVADER HAS REACHED THE BATTLESHIP
            if invader.distance(battleship) < 60:
                # FOR EACH INVADER
                for remaining_invader in invaders:
                    # HIDE THE INVADER
                    remaining_invader.hideturtle()
                # HIDE THE BATTLESHIP
                battleship.hideturtle()
                # HIDE BATTLESHIP ROCKET
                battleship_rocket.hideturtle()
                # HIDE INVADER ROCKET
                invaders_rocket.hideturtle()
                # RESET SCOREBOARD
                scoreboard.reset()
                # HIDE LIVES
                lives.hideturtle()
                # DISPLAY RESTART PROMPT
                restart.update_restart_prompt(scoreboard.score)
                # DISPLAY TEXT BOX TO CAPTURE USER INPUT
                user_input = screen.textinput("Restart?", "Y/N?")
                # IF USER WANTS TO PLAY AGAIN
                if user_input.lower() == "y":
                    # RESET RESTART PROMPT
                    restart.reset()
                    # CREATE GAME ELEMENTS
                    screen, battleship, battleship_rocket, invaders, invaders_rocket, scoreboard, lives, restart = create_game_elements()
                    # LISTEN FOR USER INPUTS
                    screen.listen()
                    # MOVE BATTLESHIP TO THE RIGHT WITH RIGHT ARROW KEY
                    screen.onkey(fun=battleship.move_right, key="Right")
                    # MOVE BATTLESHIP TO THE LEFT WITH LEFT ARROW KEY
                    screen.onkey(fun=battleship.move_left, key="Left")
                    # FIRE BATTLESHIP ROCKETS WITH SPACE BAR
                    screen.onkey(fun=fire_battleship_rocket, key="space")
                # IF USER DOES NOT WANT TO PLAY AGAIN
                elif user_input.lower() == "n":
                    # END GAME
                    break
                # INVALID INPUT
                else:
                    # ASK USER TO TRY AGAIN
                    user_input = screen.textinput("Invalid Input", "Please enter any key to return to previous prompt")

        # FIRE INVADER ROCKET
        fire_invader_rocket()

        # IF ROCKET IS FIRING
        if INVADER_ROCKET == "FIRING":
            # MOVE INVADERS ROCKET
            invaders_rocket.sety(invaders_rocket.ycor() + INVADER_ROCKET_SPEED)
        # IF FIRED INVADER ROCKET HAS REACHED BOTTOM OF THE SCREEN
        if invaders_rocket.ycor() <= (screen.window_height() * -.45):
            # HIDE INVADER ROCKET
            invaders_rocket.hideturtle()
            # UPDATE INVADER ROCKET STATE
            INVADER_ROCKET = "PREPARING"
        # IF INVADERS ROCKET HAS COLLIDED WITH BATTLESHIP
        if invaders_rocket.distance(battleship) < 50:
            # PLAY SOUND
            winsound.PlaySound("static/sounds/explosion.wav", winsound.SND_ASYNC)
            # HIDE INVADER ROCKET
            invaders_rocket.hideturtle()
            # UPDATE INVADER ROCKET STATE
            INVADER_ROCKET = "PREPARING"
            # REMOVE A LIFE
            lives.remove_life()
            # RESET BATTLESHIP
            battleship.reset_battleship()

        # IF ROCKET IS FIRING
        if BATTLESHIP_ROCKET == "FIRING":
            # MOVE BATTLESHIP ROCKET
            battleship_rocket.sety(battleship_rocket.ycor() + BATTLESHIP_ROCKET_SPEED)
        # IF ROCKET HAS REACHED TOP OF THE SCREEN
        if battleship_rocket.ycor() >= (screen.window_height() * .35):
            # HIDE ROCKET
            battleship_rocket.hideturtle()
            # UPDATE ROCKET STATE
            BATTLESHIP_ROCKET = "PREPARING"

        # UPDATE SCREEN
        screen.update()
