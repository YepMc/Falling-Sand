import pygame


pygame.init()

WINDOW_WIDTH = 800 
WINDOW_HEIGHT = 600

window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Falling Sand Sim")

clock = pygame.time.Clock()
 