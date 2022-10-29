import pygame
import sys

pygame.init()


# Screen Size
WIDTH, HEIGHT = 640, 480

clock = pygame.time.Clock()
# Colors
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60


class Player:
    def __init__(self, path_to_img, pos, screen):
        self.path_to_img = path_to_img
        self.x, self.y = pos
        self.screen = screen
        self.player_img = pygame.transform.scale2x(
            pygame.image.load(self.path_to_img))
        self.player_rect = self.player_img.get_rect()
        self.moveSpeed = 2

    def show_on_screen(self):
        self.screen.blit(self.player_img, (self.x, self.y))

    def move(self, x : int , y : int):
        self.x += self.moveSpeed * x
        self.y += self.moveSpeed * y

    def rotate(self, deg : float):
        pygame.transform.rotate(self.player_img, deg)
    
    def get_location(self):
        return self.x, self.y
    
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.move(-1, 0)
        if keys[pygame.K_d]:
            player.move(1, 0)
        if keys[pygame.K_w]:
            player.move(0, -1)
        if keys[pygame.K_s]:
            player.move(0, 1)

    def shoot(self):
        pass

    class Bullet:
        def __init__(self, pos, direction):
            self.pos = pos
            self.direction = direction
        
        def move(self, x : int, y : int):
            pass

player = Player("Assets/Player.png", (WIDTH/2-32, HEIGHT/2-32), screen)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    player.input()

    screen.fill(BLACK)
    player.show_on_screen()

    pygame.display.flip()
    clock.tick(FPS)
