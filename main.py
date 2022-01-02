import os

from re import A, escape
from ursina import *
from random import randint
from cannonball import CannonBall
from player import Player
from sea import Sea
from ursina.camera import Camera
from intro import Title, inputName, optionButton, LoadingWheel
from direct.stdpy import thread
from ursina.prefabs.health_bar import HealthBar



app = Ursina()

window.title = 'My game'                # The window title
bg = Sprite('Image/background.png')

# Custom window
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
# Do not show the in-game red X that loses the window
window.exit_button.visible = False
window.fps_counter.enabled = False

def display(item, state):               # Show/hide item on screen
        if state:
            item.visible = True
        else:
            item.visible = False

def show(*argv):
    for arg in argv:
        display(arg, True)

def hide(*argv):
    for arg in argv:
        display(arg, False)

def submit():                                   # Play-button clicked
    hide(title, playButton, inpName, bg)
    show(info_text)

def load_textures():
    textures_to_load = ['brick', 'shore', 'grass', 'heightmap'] * 25
    bar = HealthBar(max_value=len(textures_to_load), value=0, position=(-.5,-.35,-2), scale_x=1, animation_duration=0, world_parent=loading_screen, bar_color=color.gray)
    for i, t in enumerate(textures_to_load):
        load_texture(t)
        print(i)
        bar.value = i+1

    print('loaded textures')
    hide(loading_screen, info_text)
    show(player)
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
            if player.visible:
                display(canno, True)
            else:
                display(canno, False)
    
    if key == 'space':
        hide(info_text)
        show(loading_screen)
        t = time.time()

        try:
            thread.start_new_thread(function=load_textures, args='')
        except Exception as e:
            print('error starting thread', e)

        print('---', time.time()-t)

title = Title()
inpName = inputName()
playButton = optionButton()
loading_screen = LoadingWheel(visible=False)
info_text = Text('''Press space to start loading textures''', origin=(0,0), color=color.black, visible = False)

player = Player(0, 0)
background = Sea(False)


playButton.on_click = submit


app.run()
