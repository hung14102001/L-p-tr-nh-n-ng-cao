import os
from ursina import Entity, camera, collider, held_keys
import time

class Player(Entity):
    def __init__(self, position_x, position_y):

        super().__init__(
            model='quad',
            collider = 'box',
            texture=os.path.join("Ships", "ship (4).png"),
            x=position_x,
            y=position_y,
            rotation_z = 0,
            level = 1,
            team = 1,
            z=0,
            scale_x=1,
            scale_y=2,
        )
        self.speed = 0.1
        self.reload = time.time()
        
    def update(self):
        angle = self.rotation_z
        changeX = 0
        changeY = 0
        if held_keys['left arrow'] or held_keys['a'] :
            changeX = -self.speed
            angle = 90
        if held_keys['right arrow'] or held_keys['d'] :
            changeX = self.speed
            angle = -90
        if held_keys['up arrow'] or held_keys['w']:
            changeY = self.speed
            angle = 180
        if held_keys['down arrow'] or held_keys['s']:
            changeY = -self.speed
            angle = 0
        if (held_keys['left arrow'] or held_keys['a']) and (held_keys['up arrow'] or held_keys['w']):
            changeX = -self.speed /1.414
            changeY = self.speed /1.414
            angle = -45
        if (held_keys['right arrow'] or held_keys['d']) and (held_keys['up arrow'] or held_keys['w']):
            changeX = self.speed /1.414
            changeY = self.speed /1.414
            angle = 45
        if (held_keys['left arrow'] or held_keys['a']) and (held_keys['down arrow'] or held_keys['s']):
            changeX = -self.speed/1.414
            changeY = -self.speed /1.414
            angle = -135

        if (held_keys['right arrow'] or held_keys['d']) and (held_keys['down arrow'] or held_keys['s']):
            changeX = self.speed /1.414
            changeY = -self.speed /1.414
            angle = 135

        self.rotation_z = angle
        
        camera.x = self.x
        camera.y = self.y
        hitinfo = self.intersects()
        if hitinfo:
            changeX = 0
            changeY = 0
        self.x += changeX
        self.y += changeY
