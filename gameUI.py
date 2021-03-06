from ursina import *
from player import Player


class gameUI (Entity):
    def __init__(self):
        super().__init__()
        self.player = Player.getInstance()
        self.minimap = MiniMap(self.player)
        self.healthBar = HealthBar()
        self.text = Text(
            text="Score: 0 ", 
            color=color.rgb(0,0,0), 
            scale = 2.5, 
            position=(-0.8,0.5,0)
        )
    def update(self):
        self.minimap.playerRep.x = self.player.x/40
        self.minimap.playerRep.y = self.player.y/40
        self.healthBar.healthbar.scale_x = self.healthBar.healthbar_size.x*self.player.health/100
        self.text.text = "Score: " + str(self.player.score)
class HealthBar():
    def __init__(self):
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

        
        
    

class MiniMap(Entity):
    def __init__(self, player):
        super().__init__(
            scale=0.28,
            parent=camera.ui,
            model="quad",
            position=Vec2(0.74, 0.35),
            color=color.rgb(161, 234, 255)
        )
        
        black = color.rgb(0, 0, 0)
        red = color.rgb(255, 0, 0)
        green = color.rgb(0, 255, 0)
        bistre = color.rgb(205, 133, 63)
        goldenbrown = color.rgb(205, 133, 63)

        self.playerRep = Entity(
            parent=self,
            scale=.05,
            model='circle',
            position=(player.x/40,player.y/40),
            color=red
        )
        self.beach = Entity(
            parent=self,
            scale=1.2,
            model='quad',
            position=(0.03, 0.07, 0.0001),
            color=goldenbrown
        )
        self.quarter = Entity(
            parent=self,
            scale=(.05, 0.2),
            model='quad',
            position=(0,-0.38,0),
            color=bistre
        )
        self.quarter = Entity(
            parent=self,
            scale=(0.2, .05),
            model='quad',
            position=(-0.38,0,0),
            color=bistre
        )
        self.quarter = Entity(
            parent=self,
            scale=(.05, 0.2),
            model='quad',
            position=(0,0.38,0),
            color=bistre
        )
        self.quarter = Entity(
            parent=self,
            scale=(0.2, .05),
            model='quad',
            position=(0.38,0,0),
            color=bistre
        )

        self.smallIsland = Entity(
            parent=self,
            scale=(.095, .095),
            model='quad',
            position=(0.175,0.175,0),
            color=bistre
        )

        self.smallIsland = Entity(
            parent=self,
            scale=(.095, .095),
            model='quad',
            position=(-0.175,0.175,0),
            color=bistre
        )

        self.smallIsland = Entity(
            parent=self,
            scale=(.095, .095),
            model='quad',
            position=(0.175,-0.175,0),
            color=bistre
        )

        self.smallIsland = Entity(
            parent=self,
            scale=(.095, .095),
            model='quad',
            position=(-0.175,-0.175,0),
            color=bistre
        )

        self.bigIsland = Entity(
            parent=self,
            scale=(.14, .14),
            model='quad',
            position=(0,0,0),
            color=bistre
        )
        self.bigIsland = Entity(
            parent=self,
            scale=(.1, .1),
            model='quad',
            position=(0,0,-0.1),
            color=green
        )
    # def update(self):
    #     self.playerRep.x = self.player.x/40
    #     self.playerRep.y = self.player.y/40
