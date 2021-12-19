from ursina import camera, Entity, Vec2, Vec3, color, texture, EditorCamera, BoxCollider
from ursina.prefabs.first_person_controller import FirstPersonController
class MiniMap(Entity):
    def __init__(self, player, sea):
        super().__init__(
            scale=0.4,
            parent = camera.ui,
            model="quad"
            # parent = camera.ui,
            # collider="box"
        )
        
        self.minimap_size = Vec2(1, 1)
        self.position = Vec2(0.7, 0.3)
        self.player_X = player.x
        self.player_Y = player.y
    def update(self):
        # ec = EditorCamera(rotation_smoothing=2, enabled=1, position=Vec3(self.player_X, self.player_Y, -10))
        camera.minimapX = self.player_X
        camera.minimapY = self.player_Y
        camera.minimapZ = -50
        # put camera in minimap
        # self.texture = ec
        # self.texture = texture.Texture(ec)
        