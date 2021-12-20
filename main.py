import os

from re import A, escape
from ursina import *
from random import randint
from cannonball import CannonBall
from player import Player
from sea import Sea
from ursina.camera import Camera
from intro import Text, Input, Button


app = Ursina(boderless=False)

# Custom window
window.exit_button.enabled = True
window.cog_button.enabled = False
window.fps_counter.enabled = False
window.fullscreen = False

# Title and background
window.title = "Demo"
window.color = color.rgb(167, 162, 193)


# Show/hide item on screen
def display(item, state):
    if state:
        item.enable()
    else:
        item.disable()


def enable(*argv):
    for arg in argv:
        display(arg, True)


def disable(*argv):
    for arg in argv:
        display(arg, False)


# Loading animations
anim = Animation('loadAnim/load', loop=True, autoplay=True, duration=12)
a = Animator(animations={'ready': Entity(),
                         'load': anim}
             )

# play-button clicked


def submit():
    disable(btn, inp)
    txt.text = ''
    a.state = 'load'
    invoke(start, delay=1.5)


# start play game
def start():
    a.state = 'ready'
    enable(player)
    background = Sea(True)


# from ursina import texture
# input
def input(key):
    if key == 'esc':
        app.running = False
    # move left if hold arrow left

    if mouse.left:
        # Audio('audios/shot.wav').play()
        if time.time() - player.reload > 1:
            player.reload = time.time()
            #CannonBall(player.x, player.y, mouse.x, mouse.y)
            canno = CannonBall(player.x, player.y, mouse.x, mouse.y)

            # Show/hide cannon by player
            if player.enabled:
                display(canno, True)
            else:
                display(canno, False)


# Introduction
txt = Text()
inp = Input()
btn = Button()

player = Player(0, 0)
background = Sea(False)

disable(player)
a.state = 'ready'
btn.on_click = submit


app.run()
