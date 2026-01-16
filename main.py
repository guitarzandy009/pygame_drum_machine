# src/main.py
import pygame

pygame.init()

# Initial setup
WIDTH = 1400
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Drum Machine')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game loop
run = True
clock = pygame.time.Clock()

while run:
    clock.tick(60)
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

pygame.quit()
