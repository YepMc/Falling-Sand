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

    def update(self):
        for row in range(self.grid.rows - 2, -1, -1):
            for column in range(self.grid.columns):
                particle = self.grid.get_cell(row, column)
                if particle is not None:
                    new_pos = particle.update(self.grid, row, column)
                    if new_pos != (row, column):
                        self.grid.set_cell(new_pos[0], new_pos[1], particle)
                        self.grid.remove_particle(row,column)