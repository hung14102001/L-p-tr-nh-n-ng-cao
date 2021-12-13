from re import A, escape
from ursina import *
from random import randint

from ursina.camera import Camera

# from ursina import texture

Cannons = []
# input
def input(key):
    global Cannons
    if key == 'esc':
        app.running = False
    # move left if hold arrow left
    if held_keys['left arrow'] or held_keys['a'] :
        player.x -= 0.1
    if held_keys['right arrow'] or held_keys['d'] :
        player.x += 0.1
    if held_keys['up arrow'] or held_keys['w']:
        player.y += 0.1
    if held_keys['down arrow'] or held_keys['s']:
        player.y -= 0.1
    if key == 'space':
        Audio('audios/shot.wav').play()
        cannon = Canon()
        Cannons.append(cannon)
# create cannon class
class Canon(Entity):
    def __init__(self):

        super().__init__()
        self.model = 'cube'
        self.texture = "Cannon/cannonBall.png"
        self.x = player.x
        self.y = player.y + 0.8
        self.scale_x = 0.18
        self.scale_y = 0.18
        self.speed = 3

# function update
def update():
    # add bounderies
    if player.x < -6.8:
        player.x = -6.8
    if player.x > 6.8:
        player.x = 6.8
    if player.y < -3.2:
        player.y = -3.2
    if player.y > 3.2:
        player.y = 3.2
# display the background
app = Ursina()
player = Entity(model='cube',texture = 'ship (24).png', scale=(1.1,1.5,1), z=0)
background = Entity(model='cube', scale_x=15, scale_y=10, texture='Sample.png', z = 0.01)



app.run()