import random 
import colorsys


class SandParticle():
    def __init__(self):
        self.color = self.randomc_color()

    def randomc_color(self):
        hue = random.uniform(0.1,0.12)
        saturation = random.uniform(0.5,0.7)
        value = random.uniform(0.6,0.8)
        r,g,b = colorsys.hsv_to_rgb(hue,saturation,value)
        return (int(r*255), int(g*255), int(b*255))

    def update(self, grid, row, column):
        if grid.is_cell_empty(row+1, column):
            return row+1, column
        else:
            offsets = [-1,1]
            random.shuffle(offsets)
            for offset in offsets:
                new_column = column + offset
                if grid.is_cell_empty(row+1,new_column):
                    return row+1, new_column
        return row, column
        