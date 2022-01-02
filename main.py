import os

from re import A, escape
from ursina import *
from random import randint
from cannonball import CannonBall
from player import Player
from sea import Sea
from ursina.camera import Camera
from intro import Text, Input, Button


app = Ursina()

# Custom window
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window 
window.fps_counter.enabled = False

window.title = 'My Game'                # The window title
bg = Sprite('Image/background.png')

Text.default_font = 'Font/aAbstractGroovy.ttf'
Text.size = 0.1

def display(item, state):               # Show/hide item on screen
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


anim = Animation('loadAnim/load', loop=True)    # Loading animations
a = Animator(animations={'ready': Entity(),
                         'load': anim}
             )

def submit():                                   # Play-button clicked
    disable(btn, inp, bg)
    txt.visible = False
    a.state = 'load'
    invoke(start, delay=1.2)
    

def start():                                    # Start play game
    a.state = 'ready'
    enable(player)
    background = Sea(True)


# from ursina import texture
def input(key):                                 # input
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
btn.on_click = submit


app.run()
