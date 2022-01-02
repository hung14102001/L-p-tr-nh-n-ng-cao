from ursina import *


class Text(Text):
    def __init__(self):
        super().__init__(
            text='WELCOME TO OUR WORLD !',
            origin=(0, -4),
            color=color.black,
            size=Text.size,
            font=Text.default_font

        )
        self.appear(speed=.05, delay=0)
    

class Input(InputField):
    def __init__(self):
        super().__init__(y=0)
        self.tooltip = Tooltip('Nhap ten cua ban')


class Button(Button):
    def __init__(self):
        super().__init__(
            position=(0, -.2),
            scale=.1,
            icon='Image/play_icon.png',
            color=color.rgba(255, 255, 255, 0),
        )
        