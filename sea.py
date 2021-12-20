import os
import ursina
from random import randint

from ursina import collider    

# self.collider = BoxCollider(self, size=Vec3(1, 2, 1))

class SeaPart(ursina.Entity):
    def __init__(self, position):
        super().__init__(
            position=position,
            scale=2,
            model="quad",
            texture=os.path.join("Tiles", "tile_73.png")
        )
        self.texture.filtering = None

class SoilPart(ursina.Entity):
    def __init__(self, position):
        super().__init__(
            position=position,
            scale=1,
            model="quad",
            texture=os.path.join("Tiles", "tile_18.png"),
            collider="box"
        )
        self.texture.filtering = None
class IslandPart(ursina.Entity):
    def __init__(self, position,img):
        super().__init__(
            position=position,
            scale=1,
            model="quad",
            texture=img,
            collider="box"
        )
        # self.texture.filtering = None
class PlantPart(ursina.Entity):
    def __init__(self, position,img):
        super().__init__(
            position=position,
            scale=1,
            model="quad",
            texture=img,
            # collider="box"
        )     
class Sea:
    tiles = [os.path.join("Tiles",f"tile_{x}") for x in range(0,96)]    
    def __init__(self):
        for x in range(-20, 20, 2):
            for y in range(-20, 20, 2):
                part = SeaPart(ursina.Vec3(x, y, 0.1))
        for x in range(-30, 30, 2):
            for y in range(-30, 30, 2):
                if x >= 20 or x <=-20 or y <= -20 or y >= 20:
                    part = SoilPart(ursina.Vec3(x, y, 0))
        for x in range(0, 5):
            px = randint(-18, 18)
            py = randint(-18, 18)
            part = IslandPart(ursina.Vec3(px, py, 0), self.tiles[1])
            part = IslandPart(ursina.Vec3(px+1, py, 0), self.tiles[2])
            part = IslandPart(ursina.Vec3(px+2, py, 0), self.tiles[3])
            part = IslandPart(ursina.Vec3(px, py-1, 0), self.tiles[17])
            part = IslandPart(ursina.Vec3(px+1, py-1, 0), self.tiles[18])
            part = IslandPart(ursina.Vec3(px+2, py-1, 0), self.tiles[19])
            part = IslandPart(ursina.Vec3(px, py-2, 0), self.tiles[33])
            part = IslandPart(ursina.Vec3(px+1, py-2, 0), self.tiles[34])
            part = IslandPart(ursina.Vec3(px+2, py-2, 0), self.tiles[35])
        for x in range(0, 5):
            px = randint(-18, 18)
            py = randint(-18, 18)
            part = IslandPart(ursina.Vec3(px, py, 0), self.tiles[4])
            part = IslandPart(ursina.Vec3(px+1, py, 0), self.tiles[5])
            part = IslandPart(ursina.Vec3(px, py-1, 0), self.tiles[20])
            part = IslandPart(ursina.Vec3(px+1, py-1, 0), self.tiles[21])
        for x in range(0, 5):
            px = randint(-16, 16)
            py = randint(-16, 16)
            for i in range(0, 5):
                part = IslandPart(ursina.Vec3(px+i, py, 0), self.tiles[6+i])
            for i in range(0, 5):
                part = IslandPart(ursina.Vec3(px+i, py-1, 0), self.tiles[22+i])
            for i in range(0, 5):
                part = IslandPart(ursina.Vec3(px+i, py-2, 0), self.tiles[38+i])
            for i in range(0, 5):
                part = IslandPart(ursina.Vec3(px+i, py-3, 0), self.tiles[54+i])
        for x in range(0, 5):
            px = randint(-18, 18)
            py = randint(-18, 18)
            part = IslandPart(ursina.Vec3(px, py, 0), self.tiles[36])
            part = IslandPart(ursina.Vec3(px+1, py, 0), self.tiles[37])
            part = IslandPart(ursina.Vec3(px, py-1, 0), self.tiles[52])
            part = IslandPart(ursina.Vec3(px+1, py-1, 0), self.tiles[53])
        for x in range(0, 5):
            for i in range(0, 3):
                px = randint(-17, 17)
                py = randint(-17, 17)
                part = IslandPart(ursina.Vec3(px+i, py, 0), self.tiles[70+i])
            # for i in range(0, 5):
            #     part = IslandPart(ursina.Vec3(px+i, py-1, 0), self.tiles[55+i])