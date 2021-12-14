from re import A, escape
from ursina import *
from random import randint
from cannon import Canon
from player import Player
from ursina.camera import Camera

# from ursina import texture
playerchangeX = 0
playerchangeY = 0
Cannons = []
numOfPlayers = 6
player = Player(0,0)
camera = Camera()
# input
def input(key):
    global Cannons
    global player
    if key == 'esc':
        app.running = False
    # move left if hold arrow left
    if held_keys['left arrow'] or held_keys['a'] :
        player.changeX = - 0.1
    if held_keys['right arrow'] or held_keys['d'] :
        player.changeX = 0.1
    if held_keys['up arrow'] or held_keys['w']:
        player.changeY = 0.1
    if held_keys['down arrow'] or held_keys['s']:
        player.changeY = -0.1
    if not (held_keys['left arrow'] or held_keys['a'] or held_keys['right arrow'] or held_keys['d'] ):
        player.changeX = 0
    if not (held_keys['up arrow'] or held_keys['w'] or held_keys['down arrow'] or held_keys['s']):
        player.changeY = 0

    if mouse.left:
        # Audio('audios/shot.wav').play()
        cannon = Canon(player.x, player.y)
        Cannons.append(cannon)
        mouse.x = round((mouse.x),2)
        mouse.y = round((mouse.y),2)
        player.x = round((player.x),2)
        player.y = round((player.y),2)
        rediffX = (mouse.x - player.x)
        rediffY = (mouse.y - player.y)
        podiffX = math.fabs(mouse.x - player.x)
        podiffY = math.fabs(mouse.y- player.y)
        rad = math.atan2(podiffY/podiffX, 1)
        cannon.cannonBallchangeX = math.cos(rad) * cannon.speed
        cannon.cannonBallchangeY = math.sin(rad) * cannon.speed
        print(player.x, player.y)
        print(rad*180)
        if rediffX < 0 and rediffY < 0:
            cannon.quarter = 1
            cannon.cannonBallchangeX *= -1
            cannon.cannonBallchangeY *= -1
        elif rediffX > 0 and rediffY < 0:
            cannon.quater = 2
            # cannon.cannonBallchangeX = cannon.cannonBallchangeX
            cannon.cannonBallchangeY *= -1
        elif rediffX > 0 and rediffY > 0:
            cannon.quater = 3
            # cannon.cannonBallchangeX = cannon.cannonBallchangeX
            # cannon.cannonBallchangeY = cannon.cannonBallchangeY
        elif rediffX < 0 and rediffY > 0:
            cannon.quaterquarter = 4
            cannon.cannonBallchangeX *= -1
            # cannon.cannonBallchangeY = cannon.cannonBallchangeY

# function update
def update():
    # move player
    player.x += player.changeX
    player.y += player.changeY
    # if player.x < -6.8:
    #     player.x = -6.8
    # if player.x > 6.8:
    #     player.x = 6.8
    # if player.y < -3.2:
    #     player.y = -3.2
    # if player.y > 3.2:
    #     player.y = 3.2
    # update cannons
    for cannon in Cannons:
        cannon.x += cannon.cannonBallchangeX
        cannon.y += cannon.cannonBallchangeY

    camera.position = (player.x, player.y, -20)
# display the background
app = Ursina()
# player = Entity(model='quad',texture = 'ship (24).png', rotation = (0, 0 ,0), scale=(1,2), z=0)
background = Entity(model='quad', scale_x=10, scale_y=10, texture='Sample.png', z = 0.01)
# camera add in player
camera = Camera()
camera.orthographic = True
camera.orthographic_scale = 10
camera.x = player.x
camera.y = player.y
camera.z = 0.01


app.run()