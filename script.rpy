# The script of the game goes in this file.
#style.default.font = "7_Emulogic.ttf"
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define fps = 30
define config.nearest_neighbor = True

init python:
    def Animation(prefix, fps=30, trans=None):
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
    ""
    window hide
    image bg noisea =Animation("images/anim/bg/noise")
#    image bg noiseb = im.Scale(bg noisea, 496, 368)
    scene bg noisea:
        zoom 1.8
        xalign 0.5
    image test bedroom = "images/bg/bedroom.png"
    show test bedroom:
        alpha 0.0
        ease 0.1 alpha 1.0
        zoom 1.0
        yalign 0.2
        xalign 0.5
        ease 0.8 zoom .72
    pause .9
    image bggg = "images/white.png"
    scene bggg
    with dissolve
    pause .5
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music dream fadeout 2

    image bg green = Animation("images/anim/bg/green")
    scene bg green
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    image trix welcome1 = Animation("images/anim/trix/welcome1/", (28/0.93))
    show trix welcome1
    "HEY, HEY!!! ARE YOU ASLEEP?\nC\'MON! ANSWER THE GREAT TRIXIE!."
    image trix welcome2:
        Animation("images/anim/trix/welcome2/start/", (39/1.3))
        pause (11/(39/1.3))
        Animation("images/anim/trix/welcome2/loop/", (39/1.3))
    show trix welcome2
    "THAT'S BETTER. TRIXIE SHALL\nSTART EXPLAINING THE RULES."

    image trix welcome3 = Animation("images/anim/trix/welcome3/")
    show trix welcome3

    image overlay cast:
        Animation("images/anim/overlay/cast1/start/", (66/2.2))
        pause (49/(66/2.2))
        Animation("images/anim/overlay/cast1/loop/", (66/2.2))
    show overlay cast

    "THE SPELL THAT TURNS YOU INTO\nA PONY LASTS THREE DAYS."


    "AFTER THAT, YOU'LL TURN BACK\nTO HUMAN. HAVE A GOOD TIME."





    # This ends the game.

    return
