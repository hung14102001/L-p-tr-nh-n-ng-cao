import os
from ursina import Entity, camera, held_keys

class Player(Entity):
    def __init__(self, position_x, position_y):

        super().__init__(
            model='quad',
            texture=os.path.join("Ships", "ship (4).png"),
            x=position_x,
            y=position_y,
            z=0,
            scale_x=1,
            scale_y=2,
        )
        self.speed = 0.09
        
    def update(self):
        # move left if hold arrow left
        if held_keys['left arrow'] or held_keys['a'] :
            self.x -= self.speed
        if held_keys['right arrow'] or held_keys['d'] :
            self.x += self.speed
        if held_keys['up arrow'] or held_keys['w']:
            self.y += self.speed
        if held_keys['down arrow'] or held_keys['s']:
            self.y -= self.speed
        camera.x = self.x
        camera.y = self.y
        if self.x > 14:
            self.x = 14
        if self.y >14:
            self.y = 14
        if self.x < -20:
            self.x = -20
        if self.y < -20:
            self.y = -20

