import math
from ursina import Entity
class Player(Entity):
    def __init__(self, position_x, position_y):

        super().__init__()
        self.model = 'quad'
        self.texture = "Ships/ship (24).png"
        self.x = position_x
        self.y = position_y
        self.scale_x = 1
        self.scale_y = 2
        self.Speed = 0.3
        self.changeX = 0
        self.changeY = 0