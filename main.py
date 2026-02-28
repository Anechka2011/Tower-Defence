import pygame


class Sprite:
    def __init__(self, center, image):
        self.image = image
        self.rect = self.image.get_frect()
        self.rect.center = center

    def render(self, surface):
        surface.blit(self.image, self.rect)



WINDOW_SIZE = (800,600)
MAX_FPS = 60

window = pygame.Window("Tower Defence", WINDOW_SIZE)
surface = window.get_surface()

clock = pygame.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            running = False



    surface.fill("white")
    ...
    window.flip()

    clock.tick(MAX_FPS)
    print(clock.get_fps())





