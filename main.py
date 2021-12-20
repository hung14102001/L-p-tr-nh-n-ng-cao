import os

from re import A, escape
from ursina import *
from random import randint
from cannonball import CannonBall
from player import Player
from sea import Sea
from minimap import MiniMap
# from network import Network
from ursina.camera import Camera


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
            CannonBall(player, mouse.x, mouse.y)
    

# display the background
app = Ursina()
player = Player(0,0)
background = Sea()  
minimap = MiniMap(player, background)


app.run()