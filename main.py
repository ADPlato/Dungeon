import pygame
import pygame_menu

import ctypes



class App:
    def __init__(self):
        self._running = True
        self._display_surf = None

        self.width=ctypes.windll.user32.GetSystemMetrics(0)
        self.height=ctypes.windll.user32.GetSystemMetrics(1)
        self.size = self.width, self.height

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        menu=App_Menu(self._display_surf)


    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._running = False
    def on_loop(self):
        pass
    def on_render(self):
        pass
    def on_cleanup(self):
        pygame.quit()


    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

class App_Menu(App):
    def __init__(self, _display_surf):
        self._display_surf=_display_surf

class App_Menu(App):
    def __init__(self, _display_surf):
        App.__init__(self)
        self._display_surf=_display_surf
        self.menu=pygame_menu.Menu('Welcome',
                              width=self.width/4,
                              height=self.height/4,
                              theme=pygame_menu.themes.THEME_DARK)
        self.menu.add.button('Play', self.start_game)
        self.menu.add.button('Create Map')
        self.menu.add.button('Settings', self.go_to_settings)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)
        self.menu.mainloop(_display_surf)

    def go_to_settings(self):
        menu=App_Menu_Settings(self._display_surf)

    def start_game(self):
        new_game=Game(self._display_surf)
        pygame.display.update()

class App_Menu_Settings(App_Menu):
    def __init__(self, _display_surf):
        App.__init__(self)
        self._display_surf = _display_surf
        self.menu=pygame_menu.Menu('Welcome',
                              width=self.width/4,
                              height=self.height/4,
                              theme=pygame_menu.themes.THEME_DARK)
        self.menu.add.button('Folder')
        self.menu.add.button('Cos innego')
        self.menu.add.button('Cofnij',self.menu_reset)
        self.menu.mainloop(_display_surf)

    def go_to_mainmenu(self):
        menu=App_Menu(self._display_surf)

class Character():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def move(self, move_x, move_y):
        self.x+=move_x
        self.y+=move_y

class Enemy():
    pass

class Game():
    def __init__(self, _display_surf):
        self._display_surf = _display_surf
        self._display_surf.fill((255,255,255))

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
