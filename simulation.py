from grid import Grid
from particle import SandParticle
class Simulation:
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)

    def draw(self, window):
        self.grid.draw(window)

    def add_particle(self, row, column):
        self.grid.add_particle(row, column, SandParticle)

    def remove_particle(self, row, column):
        self.grid.remove_particle(row, column)