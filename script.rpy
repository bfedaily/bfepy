# The script of the game goes in this file.
#style.default.font = "7_Emulogic.ttf"
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define fps = 30
define config.nearest_neighbor = True
$renpy.maximum_framerate(30)
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


transform zoom_dissolve:
    alpha 0.0 zoom 1.2
    linear 2 zoom 1.0 alpha 1.0
# The game starts here.

label start:
    window hide
    ""
    window hide
    pause 1
    image bg noisea =Animation("images/anim/bg/noise")
#    image bg noiseb = im.Scale(bg noisea, 496, 368)
    scene bg noisea:
        zoom 1.8
        xalign 0.5
    image test bedroom = "images/bg/bedroom.png"
    show test bedroom:
        alpha 0.0
        yalign 0.2
        xalign 0.5
        ease 0.2 alpha 1.0
        zoom 1.0
        ease 0.8 zoom .72
    pause .1
    image bgwhite = "images/white.png"
    show bgwhite:
        alpha 1.0
        ease 0.2 alpha 0.0

    pause 1
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music dream fadeout 2

    image bg green = Animation("images/anim/bg/green")
    scene bg green
    with Fade(0.5, 0.5, 0.5, color="#000")

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    image trix welcome1 = Animation("images/anim/trix/welcome1/", (28/0.93))
    show trix welcome1 at zoom_dissolve, center
    "HEY, HEY!!! ARE YOU ASLEEP?\nC\'MON! ANSWER THE GREAT TRIXIE!."
    $renpy.pause(2.0, hard = True)
    image trix welcome2:
        Animation("images/anim/trix/welcome2/start/", (39/1.3))
        pause (11/(39/1.3))
        Animation("images/anim/trix/welcome2/loop/", (39/1.3))
    show trix welcome2
    "THAT'S BETTER. TRIXIE SHALL\nSTART EXPLAINING THE RULES."

    image trix welcome3 = Animation("images/anim/trix/welcome3/")
    show trix welcome3

    image overlay cast1:
        Animation("images/anim/overlay/cast1/start/", (66/2.2))
        pause (49/(66/2.2))
        Animation("images/anim/overlay/cast1/loop/", (66/2.2))
    show overlay cast1

    "THE SPELL THAT TURNS YOU INTO\nA PONY LASTS THREE DAYS."

    image overlay cast2:
        Animation("images/anim/overlay/cast2/", (46/2))
        pause 2.0
        "images/anim/overlay/cast2/60.png"
        pause 99999
    show overlay cast2
    "AFTER THAT, YOU'LL TURN BACK\nTO HUMAN. HAVE A GOOD TIME."

    $renpy.pause(2.0, hard = True)
    image bg ponyday = "images/bg/ponyday.png"
    scene bg ponyday:


    image intro:
        Animation("images/anim/red/transform/start/", (189/6.3))
        pause (160/(189/6.3))
        Animation("images/anim/red/transform/loop/", (189/6.3))
    show intro:
        xalign 0.0

    $renpy.pause(6.1, hard = True)

    "CUTE. NOW GO. i will STAY\nAROUND HERE FOR A BIT."

    $renpy.pause(0.3, hard = True)

    "THE GREAT AND POWERFUL TRIXIE\nSHALL SPEAK TO YOU LATER."




    # This ends the game.

    return
