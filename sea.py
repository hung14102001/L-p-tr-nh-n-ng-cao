import os
import ursina


class SeaPart(ursina.Entity):
    def __init__(self, position):
        super().__init__(
            position=position,
            scale=2,
            model="quad",
            texture=os.path.join("Tiles", "tile_73.png"),
            collider="box"
        )
        self.texture.filtering = None
class SoilPart(ursina.Entity):
    def __init__(self, position):
        super().__init__(
            position=position,
            scale=2,
            model="quad",
            texture=os.path.join("Tiles", "tile_18.png"),
            collider="box"
        )
        self.texture.filtering = None

class Sea:
    def __init__(self):
        for x in range(-20, 20, 2):
            for y in range(-20, 20, 2):
                part = SeaPart(ursina.Vec3(x, y, 0.1))
        for x in range(-30, 30, 2):
            for y in range(-30, 30, 2):
                if x >= 20 or x <=-20 or y <= -20 or y >= 20:
                    part = SoilPart(ursina.Vec3(x, y, 0.1))