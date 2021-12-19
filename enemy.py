from ursina import Entity, Vec3, Vec2, color, collider, destroy

class enemy(Entity):
    def __init__(self, position: Vec3, identifier: str, username: str, img_path: str):
        super().__init__(
            position=position,
            model="cube",
            collider="box",
            texture=img_path,
            scale=Vec3(1, 2, 0)
        )


        self.name_tag = Entity(
            parent=self,
            text=username,
            position=Vec3(0, 1.3, 0),
            scale=Vec2(5, 3),
            billboard=True,
            origin=Vec2(0, 0)
        )

        self.health = 100
        self.id = identifier
        self.username = username
    def update(self):
        try:
            color_saturation = 1 - self.health / 100
        except AttributeError:
            self.health = 100
            color_saturation = 1 - self.health / 100

        self.color = color.color(0, color_saturation, 1)

        if self.health <= 0:
            destroy(self)
