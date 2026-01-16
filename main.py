# Timestamp 8:56

# src/main.py
import pygame
from pygame import mixer

pygame.init()

# Initial setup
WIDTH = 1400
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Beat Machine')
label_font = pygame.font.Font('freesansbold.ttf', 32)

fps = 60
timer = pygame.time.Clock()
# Colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

# Game loop
run = True
# clock = pygame.time.Clock()

while run:
    timer.tick(fps)
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

pygame.quit()
