import os
import ursina
from random import randint


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


class IslandPart(ursina.Entity):
    def __init__(self, position):
        super().__init__(
            position=position,
            scale=2,
            model="quad",
            texture=os.path.join("Tiles", "tile_17.png"),
            collider="box"
        )
        self.texture.filtering = None


class Sea():
    def __init__(self, k):
        for x in range(-20, 20, 2):
            for y in range(-20, 20, 2):
                part = SeaPart(ursina.Vec3(x, y, 0.1))
                self.pressed(part,k)
        for x in range(-30, 30, 2):
            for y in range(-30, 30, 2):
                if x >= 20 or x <= -20 or y <= -20 or y >= 20:
                    part = SoilPart(ursina.Vec3(x, y, 0.1))
                    self.pressed(part,k)
                


        for x in range(0, 20):
            px = randint(-18, 18)
            py = randint(-18, 18)
            part = IslandPart(ursina.Vec3(px, py, 0))
            self.pressed(part,k)

    # Show/hide background when button clicked   
    def pressed(self, item, index):
        if index==1:
            item.enable()
        else:
            item.disable()

