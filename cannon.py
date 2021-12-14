import math
from ursina import Entity
class Canon(Entity):
    def __init__(self, position_x, position_y):

        super().__init__()
        self.model = 'quad'
        self.texture = "Cannon/cannonBall.png"
        self.x = position_x + 0.1
        self.y = position_y + 0.8
        self.scale_x = 0.18
        self.scale_y = 0.18
        self.speed = 0.3
        self.quater = 0
        self.cannonBallchangeX = 0
        self.cannonBallchangeY = 0
    