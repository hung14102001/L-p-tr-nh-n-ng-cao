from ursina import *
from random import randint
from menu import MainMenu
from sea import Plant, Coin
from minimap import MiniMap
# from network import Network
from ursina.camera import Camera
from enemy import Enemy


# display the background
app = Ursina()

window.title = 'My game'                # The window title

# Custom window
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen

# Do not show the in-game red X that loses the window
window.exit_button.visible = False
window.fps_counter.enabled = False

main_menu = MainMenu()

#plant = Plant()
#coin = Coin()
#minimap = MiniMap(player, background)
# camera.z = -100
#Enemy(Vec2(5,5), '1111', '234', './Ships/ship_4.png')

app.run()