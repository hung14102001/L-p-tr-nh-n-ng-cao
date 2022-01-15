import os
from ursina import *
import time
import random
from sea import Restrictor, CoinPart


class Player(Entity):
    __instance = None
    @staticmethod 
    def getInstance():
      """ Static access method. """
      if Player.__instance == None:
         Player(random.randint(10, 19), random.randint(10, 19))
      return Player.__instance

    def __init__(self, position_x, position_y):
        """ Virtually private constructor. """
        if Player.__instance != None:
            self.x = position_x
            self.y = position_y
            return self
        else:
            Player.__instance = self

        super().__init__(
            model='cube',
            collider = 'box',
            x=position_x,
            y=position_y,
            score = 0,
            rotation_z = 0,
            z=0,
            scale_x=1,
            scale_y=2,
            enabled = False,
        )
        self.speed = 0.15
        self.reload = time.time()
        self.level = 1
        self.network = network
        self.coins = coins
        self.healthbar_pos = Vec2(0, -0.1)
        self.healthbar_size = Vec2(0.2, 0.02)
        self.healthbar_bg = Entity(
            parent=camera.ui,
            model="quad",
            color= color.rgb(255, 0, 0),
            position=self.healthbar_pos,
            scale=self.healthbar_size
        )
        self.healthbar = Entity(
            parent=camera.ui,
            model="quad",
            color=color.rgb(0, 255, 0),
            position=self.healthbar_pos,
            scale=self.healthbar_size
        )
        
        self.health = 20
        self.game_ended = False
        text = Text(text="Score: " +str(self.score), color=color.rgb(0,0,0), scale = 2.5, position=(-0.8,0.5,0))
        self.team = 1
        # self.healthbar_pos = Vec2(0, -0.1)
        # self.healthbar_size = Vec2(0.2, 0.02)
        # self.healthbar_bg = Entity(
        #     parent=camera.ui,
        #     model="quad",
        #     color= color.rgb(255, 0, 0),
        #     position=self.healthbar_pos,
        #     scale=self.healthbar_size
        # )
        # self.healthbar = Entity(
        #     parent=camera.ui,
        #     model="quad",
        #     color=color.rgb(0, 255, 0),
        #     position=self.healthbar_pos,
        #     scale=self.healthbar_size
        # )
        
        self.health = 100
        # self.text = Text(
        #     text="Score: " + str(self.score), 
        #     color=color.rgb(0,0,0), 
        #     scale = 2.5, 
        #     position=(-0.8,0.5,0)
        # )

        fire = Animation(
            'kenney_piratePack/PNG/Default size/Effects/fire',
            fps=4,
            loop=True,
            autoplay=True,
            visible=False,
            z=-1
        )
        fire2 = Animation(
            'kenney_piratePack/PNG/Default size/Effects/fire',
            scale=(.2,.4),
            # rotation_y=180,
            fps=4,
            loop=True,
            autoplay=True,
            visible=False,
            z=-1
        )
        fire3 = Animation(
            'kenney_piratePack/PNG/Default size/Effects/fire',
            scale=(.4,.6),
            fps=4,
            loop=True,
            autoplay=True,
            visible=False,
            z=-1
        )
        self.anim = [fire, fire2, fire3]
        self.animPos = [[.5, 0], [-.1, .2], [.2, 0]]
        
    def update(self):
        self.healthbar.scale_x = self.healthbar_size[0]*self.health/20
        if self.health > 0:
            angle = self.rotation_z
            increaseX = 0
            increaseY = 0
            decreaseX = 0
            decreaseY = 0
            if held_keys['up arrow'] or held_keys['w']:
                increaseY = self.speed
                angle = 180
        
            if held_keys['down arrow'] or held_keys['s']:
                decreaseY = self.speed
                angle = 0
            if held_keys['left arrow'] or held_keys['a'] :
                decreaseX = self.speed
                angle = 90
                if held_keys['up arrow'] or held_keys['w']:
                    angle = 135
                    decreaseX = self.speed /1.414
                    increaseY = self.speed /1.414
                elif held_keys['down arrow'] or held_keys['s']:
                    angle = 45
                    decreaseX = self.speed /1.414
                    decreaseY = self.speed /1.414

            if held_keys['right arrow'] or held_keys['d'] :
                increaseX = self.speed
                angle = -90
                if held_keys['up arrow'] or held_keys['w']:
                    angle = -135
                    increaseX = self.speed /1.414
                    increaseY = self.speed /1.414

                elif held_keys['down arrow'] or held_keys['s']:
                    angle = -45
                    increaseX = self.speed /1.414
                    decreaseY = self.speed /1.414
            if held_keys['g']:
                camera.x = self.x
                camera.y = self.y
                camera.z = -50
            self.rotation_z = angle
            
            camera.x = self.x
            camera.y = self.y
            camera.z = -30


            hitinfo = self.intersects()
            if hitinfo.hit:
                if isinstance(hitinfo.entity, CoinPart):
                    if not self.game_ended:
                        self.score += 1
                    index = hitinfo.entity.index
                    self.coins.destroy_coin(index)

                    self.network.send_coin(index)

                x = hitinfo.point.x
                y = hitinfo.point.y
                if x == .5:
                    decreaseX = 0
                if x == -.5:
                    increaseX = 0
                if y == .5:
                    decreaseY = 0
                if y == -.5:
                    increaseY = 0
                
            self.x = self.x + increaseX - decreaseX
            self.y = self.y + increaseY - decreaseY
            
