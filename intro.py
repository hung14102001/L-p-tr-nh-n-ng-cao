from ursina import *

class Title(Text):
    def __init__(self):
        super().__init__(
            text = 'WELCOME TO OUR WORLD !',
            origin = (0, -4),
            color = color.black,
            size = Text.size,
            font = 'Font/aAbstractGroovy.ttf'
        )
        self.appear(speed=.05, delay=0)
    

class inputName(InputField):
    def __init__(self):
        super().__init__(
            y=0,
            font=Text.default_font)
        self.tooltip = Tooltip('Nhap ten cua ban')


class optionButton(Button):
    def __init__(self):
        super().__init__(
            position=(0, -.2),
            scale=.1,
            icon='Image/play_icon.png',
            color=color.rgba(255, 255, 255, 0),
        )
        
class LoadingWheel(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.parent = camera.ui
        self.point = Entity(parent=self, model=Circle(24, mode='point', thickness=.03), color=color.light_gray, y=.75, scale=2, texture='circle')
        self.point2 = Entity(parent=self, model=Circle(12, mode='point', thickness=.03), color=color.light_gray, y=.75, scale=1, texture='circle')

        self.scale = .025
        self.text_entity = Text(world_parent=self, text='Loading...', origin=(0,0), color=color.light_gray)
        self.y = -.25

        #self.bg = Entity(parent=self, model='quad', scale_x=camera.aspect_ratio, color=color.black, z=1)
        #self.bg.scale *= 400

        for key, value in kwargs.items():
            setattr(self, key ,value)


    def update(self):
        self.point.rotation_y += 5
        self.point2.rotation_y += 3    
