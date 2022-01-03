from re import A, escape
from ursina import *
from cannonball import CannonBall
from player import Player
from sea import Sea, Plant, Coin
from minimap import MiniMap
from enemy import Enemy

class OpenMap():
    def __init__(self):
        self.player = Player(-15, -15)
        self.background = Sea()
        self.minimap = MiniMap(self.player, self.background)
        self.plant = Plant()
        self.coin = Coin()
        self.enemy = Enemy(Vec2(5,5), '1111', '234', './Ships/ship_4.png')

    # from ursina import texture
    def input(self,key):                                 # input
        if key == 'esc':
            app.running = False

        # move left if hold arrow left
        if mouse.left:
            # Audio('audios/shot.wav').play()
            if time.time() - self.player.reload > 1:
                self.player.reload = time.time()
                CannonBall(self.player, self.player.x, self.player.y, mouse.x, mouse.y)
                