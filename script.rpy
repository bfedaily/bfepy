# The script of the game goes in this file.
#style.default.font = "7_Emulogic.ttf"
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define fps = 30
define config.nearest_neighbor = True
style default:
    antialias False
    line_spacing 2
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
            if not ext.lower() in [ ".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp"]:
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

    play music "audio/dream.ogg"

    image bg green = Animation("images/anim/bg/green")
    scene bg green
    with Fade(0.5, 0.5, 0.5, color="#000")

    screen dont_skip():
        key "mouseup_1" action NullAction()
        key "K_RETURN" action NullAction()
        key "K_SPACE" action NullAction()
        key "K_KP_ENTER" action NullAction()
        key "joy_dismiss" action NullAction()

    image trix welcome1 = Animation("images/anim/trix/welcome1/", (28/0.93))
    show trix welcome1 at zoom_dissolve, center
    $renpy.pause(2.4, hard = True)
    "HEY, HEY!!! ARE YOU ASLEEP?\n C'MON! ANSWER THE GREAT TRIXIE!."

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
        pause 1.9
        "images/anim/overlay/cast2/60.png"
        pause 99999
    show overlay cast2

    "AFTER THAT, YOU'LL TURN BACK\nTO HUMAN. HAVE A GOOD TIME."

    image bg intro = "images/bg/ponyday.png"
    scene bg intro:
    play music "audio/89_main_theme_start.ogg" noloop

    $renpy.music.queue("audio/90_main_theme.ogg", channel=u'music', loop=True, clear_queue=True, fadein=0, tight=True)

    image intro:
        Animation("images/anim/red/transform/start/", (189/6.3))
        pause (160/(189/6.3))
        Animation("images/anim/red/transform/loop/", (189/6.3))
    show intro:
        xalign 0.0

    $renpy.pause(((160-26)/(189/6.3)), hard = True)

    "CUTE. NOW GO. i will STAY\nAROUND HERE FOR A BIT."
    "THE GREAT AND POWERFUL TRIXIE\nSHALL SPEAK TO YOU LATER."


label pony1:

    scene bg intro:
        xalign 1
    image trixbook1:
        Animation("images/anim/trix/bookread/loop/", (30))

    image arrow_r:
        Animation("images/anim/UI/arrow_r/", (30))
    image arrow_l:
        Animation("images/anim/UI/arrow_l/", (30))
    image arrow_u:
        Animation("images/anim/UI/arrow_u/", (30))
    image arrow_d:
        Animation("images/anim/UI/arrow_d/", (30))

    screen MapUI:
        imagebutton:
            xpos 442
            ypos 314
            idle "arrow_r"
            hover "images/UI/arrow_r.webp"
            action NullAction()
 #           action Jump("house1_pressed")

        imagebutton:
            xpos 16
            ypos 314
            idle "arrow_l"
            hover "images/UI/arrow_l.webp"
#            action NullAction()
            action Jump("apple1")

        imagebutton:
            xpos 224
            ypos 218
            idle "arrow_u"
            hover "images/UI/arrow_u.webp"
            action NullAction()
#            action Jump("house1_pressed")

        imagebutton:
            xpos 312
            ypos 221
            idle "trixbook1"
#            action Jump("house1_pressed")
    call screen MapUI
    ""

label apple1:
    image bg apple1 = "images/bg/apple1.png"
    scene bg apple1:
        xalign 1


    screen MapUI2:
        imagebutton:
            xpos 442
            ypos 314
            idle "arrow_r"
            hover "images/UI/arrow_r.webp"
#            action NullAction()
            action Jump("pony1")

        imagebutton:
            xpos 16
            ypos 314
            idle "arrow_l"
            hover "images/UI/arrow_l.webp"
#            action NullAction()
            action Jump("apple1")

        imagebutton:
            xpos 224
            ypos 218
            idle "arrow_u"
            hover "images/UI/arrow_u.webp"
#            action NullAction()
            action Jump("apple2")

    call screen MapUI2

label apple2:
    image bg apple2 = "images/bg/apple2.png"
    scene bg apple2:
        xalign 1

    screen apple2:
        imagebutton:
            xpos 224
            ypos 218
            idle "arrow_u"
            hover "images/UI/arrow_u.webp"
#            action NullAction()
            action Jump("apple3")

        imagebutton:
            xpos 224
            ypos 314
            idle "arrow_d"
            hover "images/UI/arrow_d.webp"
#            action NullAction()
            action Jump("apple1")


    call screen apple2

label apple3:
    image bg apple3 = "images/bg/apple3.png"
    scene bg apple3:
        xalign 1

    screen apple3:
        imagebutton:
            xpos 224
            ypos 218
            idle "arrow_u"
            hover "images/UI/arrow_u.webp"
            action NullAction()
#            action Jump("house1_pressed")

        imagebutton:
            xpos 224
            ypos 314
            idle "arrow_d"
            hover "images/UI/arrow_d.webp"
#            action NullAction()
            action Jump("apple2")

    call screen apple3
    # This ends the game.

    return
