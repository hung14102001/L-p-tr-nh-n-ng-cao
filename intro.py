from ursina import *


class Text(Text):
    def __init__(self):
        super().__init__(
            text='WELCOME TO OUR WORLD !',
            origin=(0, -5),
            color=color.yellow,
            scale=3

        )
        self.appear(speed=.05, delay=0)


class Input(InputField):
    def __init__(self):
        super().__init__(y=.1)
        self.tooltip = Tooltip('Nhap ten cua ban')


class Button(Button):
    def __init__(self):
        super().__init__(
            position=(0, -.1),
            scale=.2,
            icon='Icon/play_icon.png',
            color=color.rgba(255, 255, 255, 0),
        )
        