import os, math
from ursina import Entity, destroy, HotReloader
class CannonBall(Entity):
    def __init__(self, player_x, player_y, mouse_x, mouse_y):

        super().__init__(
            model='quad',
            texture=os.path.join("Cannon", "cannonBall.png"),
            x=player_x,
            y=player_y,
            z=0,
            scale_x=0.18,
            scale_y=0.18,
        )
        self.speed = 0.03
        self.quater = 0
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y

        self.rediffX = self.mouse_x
        self.rediffY = self.mouse_y

        self.rad = math.atan(self.rediffY/ self.rediffX)
        destroy(self,delay= 10)
    def update(self):
        if self.rediffX < 0:
            self.x -= math.cos(self.rad)*self.speed
            self.y -= math.sin(self.rad)*self.speed
        else:
            self.x += math.cos(self.rad)*self.speed
            self.y += math.sin(self.rad)*self.speed
    