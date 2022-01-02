from ursina import *
from direct.stdpy import thread
from ursina.prefabs.health_bar import HealthBar

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

class intro():
    def display(item, state):               # Show/hide item on screen
        if state:
            item.visible = True
        else:
            item.visible = False

    def show(*argv):
        for arg in argv:
            display(arg, True)

    def hide(*argv):
        for arg in argv:
            display(arg, False)

    def submit():                                   # Play-button clicked
        hide(title, playButton, inpName, bg)
        show(info_text)
    

    def load_textures():
        textures_to_load = ['brick', 'shore', 'grass', 'heightmap'] * 25
        bar = HealthBar(max_value=len(textures_to_load), value=0, position=(-.5,-.35,-2), scale_x=1, animation_duration=0, world_parent=loading_screen, bar_color=color.gray)
        for i, t in enumerate(textures_to_load):
            load_texture(t)
            print(i)
            bar.value = i+1

        print('loaded textures')
        hide(loading_screen, info_text)
        #show(player)
        #background = Sea(True)
    
    def input(key):
        if key == 'space':
            info_text.visible = False
            loading_screen.enabled = True
            t = time.time()

            try:
                thread.start_new_thread(function=load_textures, args='')
            except Exception as e:
                print('error starting thread', e)

            print('---', time.time()-t)

    title = Title()
    inpName = inputName()
    playButton = optionButton()
    loading_screen = LoadingWheel(enabled=False)
    info_text = Text('''Press space to start loading textures''', origin=(0,0), color=color.black, visible = False)

    #player = Player(0, 0)
    #background = Sea(False)


    playButton.on_click = submit
