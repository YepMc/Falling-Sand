import pygame 
LIGHT_GREY = (55,55,55)


class Grid:
    def __init__(self, width, height, cell_size): 
        self.rows = height//cell_size
        self.columns = width//cell_size
        self.cell_size = cell_size
        self.cells = [[None for _ in range(self.columns)] for _ in range(self.rows)]

    def draw(self, window):
        for row in range(self.rows):
            for column in range(self.columns):

                color = LIGHT_GREY
                particle = self.cells[row][column]

                if particle is not None:
                    color = particle.color

                pygame.draw.rect(window, color,
                 (column * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1))
    def add_particle(self, row, column, particle_type):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.cells[row][column] = particle_type()

    def remove_particle(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.cells[row][column] = None  