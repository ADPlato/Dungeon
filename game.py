import pygame
import ctypes


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None

        self.width = ctypes.windll.user32.GetSystemMetrics(0)
        self.height = ctypes.windll.user32.GetSystemMetrics(1)
        self.size = self.width, self.height

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self.map=Map(self._display_surf)
        self.character = Character(self._display_surf, 70, 70)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._running = False
            if event.key == pygame.K_DOWN:
                self.character.move(0, 70)
            if event.key == pygame.K_UP:
                self.character.move(0, -70)
            if event.key ==pygame.K_RIGHT:
                self.character.move(70,0)
            if event.key == pygame.K_LEFT:
                self.character.move(-70,0)

    def on_loop(self):
        pygame.display.update()

    def on_render(self):
        self.map.background_image()
        self.map.background_grid()
        self.character.draw()



    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


class Character():
    def __init__(self, surface, x, y):
        self._display_surf = surface
        self.x = x
        self.y = y
        self.draw()

    def draw(self):
        rect = pygame.Rect(self.x, self.y, 70, 70)
        pygame.draw.rect(self._display_surf, (0, 0, 0), rect)



    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y

class Map():
    def __init__(self, surface):
        self._display_surf = surface

    def background_grid(self):
        block_size = 70
        for x in range(0, ctypes.windll.user32.GetSystemMetrics(0), block_size):
            for y in range(0, ctypes.windll.user32.GetSystemMetrics(1), block_size):
                rect = pygame.Rect(x, y, block_size, block_size)
                pygame.draw.rect(self._display_surf, (0,0,0), rect, 1)

    def background_image(self):
        bg_img = pygame.image.load('test.png')
        #bg_img = pygame.transform.scale(bg_img,(ctypes.windll.user32.GetSystemMetrics(0),ctypes.windll.user32.GetSystemMetrics(1)))
        self._display_surf.blit(bg_img,(0,0))

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
