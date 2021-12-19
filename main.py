import os

from re import A, escape
from ursina import *
from random import randint
from cannonball import CannonBall
from player import Player
from sea import Sea
from ursina.camera import Camera

app = Ursina(boderless=False)

# Custom window
window.exit_button.enabled = True
window.cog_button.enabled = False
window.fps_counter.enabled = False
window.fullscreen = False

# Title and background
window.title = "Demo"
window.color = color.rgb(167, 162, 193)


# Introduction_Screen
# create text
txt = Text(text='WELCOME TO OUR WORLD !',
           origin=(0, -5),
           color=color.yellow,
           scale=3)
txt.appear(speed=.05, delay=0)

# create play-button
play_btn = Button(parent='player.py',
                  text='', icon='Icon/play_icon.png',
                  color=color.rgba(255, 255, 255, 0),
                  scale=.2, position=(0, -.1))

# Show/hide item on screen
def pressed(item, is_enable):
    if is_enable:
        item.enable()
    else:
        item.disable()


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
                pressed(canno, True)
            else:
                pressed(canno, False)


# play_btn clicked
def btn_Clicked():
    pressed(play_btn, False)
    pressed(player, True)
    background = Sea(1)
    txt.text = ''


# display the background
player = Player(0, 0)
background = Sea(0)
# camera add in player

pressed(player, False)
play_btn.on_click = btn_Clicked

app.run()
