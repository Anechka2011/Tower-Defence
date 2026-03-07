import pygame


class Sprite:
    def __init__(self, center, image):
        self.image = image
        self.rect = self.image.get_frect()
        self.rect.center = center

    def render(self, surface):
        surface.blit(self.image, self.rect)


class MoveSprite(Sprite):
    def __init__(self, center, image, speed, direction):
        super().__init__(center, image)
        self.speed = speed
        self.direction = direction.normalize()

    def update(self):
        vector = self.direction * self.speed
        self.rect.move_ip(vector)



WINDOW_SIZE = (800,600)
MAX_FPS = 60

window = pygame.Window("Tower Defence", WINDOW_SIZE)
surface = window.get_surface()

clock = pygame.Clock()

center = WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2
image = pygame.Surface((50,50))
image.fill('red')
player = Sprite(center,image)
bullets = []


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            image = pygame.Surface((6,6))
            image.fill("blue")
            center = pygame.Vector2(player.rect.center)
            pos = pygame.Vector2(pygame.mouse.get_pos())
            direction = pos - center
            bullet = MoveSprite(center, image, 7, direction)
            bullets.append(bullet)

    for bullet in bullets:
        bullet.update()

    surface.fill("white")
    player.render(surface)
    for bullet in bullets:
        bullet.render(surface)
    window.flip()

    clock.tick(MAX_FPS)
    print(clock.get_fps())





