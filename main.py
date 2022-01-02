import os

from re import A, escape
from ursina import *
from random import randint
from cannonball import CannonBall
from player import Player
from sea import Sea
from ursina.camera import Camera
from intro import intro


app = Ursina()

window.title = 'My game'                # The window title
bg = Sprite('Image/background.png')

# Custom window
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
# Do not show the in-game red X that loses the window
window.exit_button.visible = False
window.fps_counter.enabled = False


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
            if player.visible:
                display(canno, True)
            else:
                display(canno, False)


player = Player(0, 0)
background = Sea(False)


app.run()
