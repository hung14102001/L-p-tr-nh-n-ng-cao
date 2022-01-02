import os

from re import A, escape
from ursina import *
from random import randint
from cannonball import CannonBall
from player import Player
from sea import Sea
from ursina.camera import Camera
from direct.stdpy import thread
from ursina.prefabs.health_bar import HealthBar

class Title(Text):
    def __init__(self):
        super().__init__(
            text='WELCOME TO OUR WORLD !',
            origin=(0, -4),
            color=color.black,
            size=Text.size,
            font='Font/aAbstractGroovy.ttf',
        )
        self.appear(speed=.05, delay=0)


class InputName(InputField):
    def __init__(self):
        super().__init__(x=.5, y=0,)
        self.tooltip = Tooltip('Nhap ten cua ban')


class LoadingWheel(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.parent = camera.ui
        self.point = Entity(parent=self, 
                            model=Circle(24, mode='point', thickness=.03), 
                            color=color.light_gray, 
                            y=.75, 
                            scale=2, 
                            texture='circle')
        self.point2 = Entity(parent=self, 
                             model=Circle(12, mode='point', thickness=.03), 
                             color=color.light_gray, 
                             y=.75, 
                             scale=1, 
                             texture='circle')

        self.scale = .025
        self.text_entity = Text(world_parent=self, 
                                text='Loading...', 
                                origin=(0, 0), 
                                color=color.light_gray)
        self.y = -.25

        self.bg = Entity(parent=self, 
                         model='quad',
                         scale_x=camera.aspect_ratio, 
                         color=color.black, 
                         z=1)
        self.bg.scale *= 400

        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        self.point.rotation_y += 5
        self.point2.rotation_y += 3


class MainMenu(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            parent=camera.ui, 
            ignore_paused=True
        )

        # Create empty entities that will be parents of our menus content
        self.main_menu = Entity(parent=self, visible=True)
        self.options_menu = Entity(parent=self, visible=False)

        self.title = Title()
        self.player_name = InputName()
        self.loading_screen = LoadingWheel(visible=False)
        self.player = Player(0, 0)
        self.background = Sea(False)

        # Add a background
        self.bg = Sprite('Image/background.png')

        # [MAIN MENU] WINDOWN START
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

        def loadTextures():
            textures_to_load = ['brick', 'shore', 'grass', 'heightmap'] * 25
            bar = HealthBar(max_value=len(textures_to_load), value=0, position=(-.5,-.35,-2), scale_x=1, animation_duration=0, world_parent=self.loading_screen, bar_color=color.gray)
            for i, t in enumerate(textures_to_load):
                load_texture(t)
                print(i)
                bar.value = i+1

            print('loaded textures')
            hide(self.loading_screen)
            show(self.player)
            self.background = Sea(True)

        # Reference of our action function for play button
        def play_btn():
            hide(self.title, self.player_name, self.bg, self.main_menu)
            show(self.loading_screen)
            t = time.time()

            try:
                thread.start_new_thread(function=loadTextures, args='')
            except Exception as e:
                print('error starting thread', e)

            print('---', time.time()-t)

        # Reference of our action function for options button
        def options_menu_btn():
            hide(self.title, self.player_name, self.main_menu)
            show(self.options_menu)

        # Reference of our action function for quit button
        def quit_game():
            application.quit()

        # Button list
        ButtonList(button_dict={
            "Play": Func(play_btn),
            "Options": Func(options_menu_btn),
            "Exit": Func(quit_game)
        }, y=0, parent=self.main_menu)
        # [MAIN MENU] WINDOW END


        # [OPTIONS MENU] WINDOW START
        # Title of our menu
        Text("OPTIONS MENU", parent=self.options_menu, y=0.4, x=0, origin=(0, 0))

        # Reference of our action function for back button
        def options_back_btn_action():
            show(self.main_menu)
            hide(self.options_menu)

        # Button
        Button("Back", parent=self.options_menu, y=-0.3, scale=(0.1, 0.05), color=rgb(50, 50, 50),
               on_click=options_back_btn_action)

        # [OPTIONS MENU] WINDOW END

        # Here we can change attributes of this class when call this class
        for key, value in kwargs.items():
            setattr(self, key, value)


    # from ursina import texture
    def input(self,key):                                 # input
        if key == 'esc':
            app.running = False

        # move left if hold arrow left
        if mouse.left:
            # Audio('audios/shot.wav').play()
            if time.time() - self.player.reload > 1:
                self.player.reload = time.time()
                #CannonBall(player.x, player.y, mouse.x, mouse.y)
                self.canno = CannonBall(self.player.x, self.player.y, mouse.x, mouse.y)
                
                # Show/hide cannon by player
                if self.player.enabled:
                    self.canno.enable()
                else:
                    self.canno.disable()
