import pygame, sys

pygame.init()


# Screen Size
WIDTH, HEIGHT = 640, 480

# Colors
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BLACK)
