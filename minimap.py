from ursina import camera, Entity, Vec2, color
class MiniMap(Entity):
    def __init__(self, player, sea):
        super().__init__(
            scale=0.3,
            parent=camera.ui,
            model="quad",
            position=Vec2(0.74, 0.35),
            color=color.rgb(161, 234, 255)
        )

        self.player = player
        
        self.playerRep = Entity(
            parent=self,
            scale=.05,
            model='circle',
            position=(player.x/40,player.y/40),
            color=color.rgb(0,0,0)
        )
    def update(self):
        self.playerRep.x = self.player.x/40
        self.playerRep.y = self.player.y/40