# The script of the game goes in this file.
#style.default.font = "7_Emulogic.ttf"
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define config.nearest_neighbor = True
init python:
    def Animation(prefix, fps=24, trans=None):
        import os
        pause = 1.0 / fps
        chain = []
        for fn in renpy.list_files():
            if not fn.startswith(prefix):
                continue
            basename = os.path.basename(fn)
            base, ext = os.path.splitext(basename)
            if not ext.lower() in [ ".jpg", ".jpeg", ".png", ".webp" ]:
                continue
            chain.extend([fn, pause, trans])
        return renpy.display.anim.TransitionAnimation(*chain)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music dream fadeout 1

    image greenbg = Animation("images/anim/bg/")
    scene greenbg

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    image trix welcome1 = Animation("images/anim/trix/welcome1/")
    show trix welcome1
    "HEY, HEY!!! ARE YOU ASLEEP?\nC\'MON! ANSWER THE GREAT TRIXIE!."

    image trix welcome2l = Animation("images/anim/trix/welcome2/loop/")

    image trix welcome2:
        "images/anim/trix/welcome2/start/01.png"
        pause (1/20)
        "images/anim/trix/welcome2/start/05.png"
        pause (1/20)
        "images/anim/trix/welcome2/start/08.png"
        pause (1/20)
        "images/anim/trix/welcome2/start/11.png"
        pause (1/20)
        "trix welcome2l"

    #image trix welcome2s = Animation("images/anim/trix/welcome2/start/")
    show trix welcome2
    "THAT'S BETTER. TRIXIE SHALL\nSTART EXPLAINING THE RULES."

    image trix welcome3 = Animation("images/anim/trix/welcome3/")
    show trix welcome3
    "THE SPELL THAT TURNS YOU INTO\nA PONY LASTS THREE DAYS."
    "AFTER THAT, YOU'LL TURN BACK\nTO HUMAN. HAVE A GOOD TIME."





    # This ends the game.

    return
