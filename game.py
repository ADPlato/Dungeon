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
        self.collision = Collisions(self._display_surf)

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(pygame.mouse.get_pos())
                self.collision.set_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            if event.button == 3:
                self.collision.del_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])


    def on_loop(self):
        pygame.display.update()

    def on_render(self):
        self.map.background_image()
        self.map.background_grid()
        self.character.draw()
        self.collision.draw()




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

class Collisions():
    def __init__(self, surface):
        self._display_surf = surface
        self.collision_grid={}

    def draw(self):
        for x in self.collision_grid.values():
            pygame.draw.rect(self._display_surf, (0, 0, 0), x)



    def set_collision(self, x, y):
        self.collision_grid[f'{x//70},{y//70}'] =pygame.Rect((x//70)*70, (y//70)*70, 70, 70)

    def del_collision(self, x, y):
        try:
            del self.collision_grid[f'{x//70},{y//70}']
        except:
            pass

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
