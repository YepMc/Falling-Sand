import pygame, sys
from simulation import Simulation

pygame.init()

WINDOW_WIDTH = 800 
WINDOW_HEIGHT = 600
CELL_SIZE = 20
FPS = 120
GREY = (29,29,29)

window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Falling Sand Sim")

clock = pygame.time.Clock()
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)



#Simulation Loop:

while True: 
    
    #Event Handling:
    for event in pygame.event.get(): #This line of code gets all the events that pygame gets since the last time the while loop ran, and puts them in a list
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Updating State



    #Drawing Grid
    window.fill(GREY)

    simulation.draw(window)
    pygame.display.flip()
    clock.tick(FPS)
