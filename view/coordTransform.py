
class CoordTransform:

    def __init__(self, display_size, coord_size):
        self.display_size = display_size
        self.coord_size = coord_size

    def display_x_to_x(self, display_x):
        return 2*self.coord_size[0]/self.display_size[0] * display_x - self.coord_size[0]

    def coord_x_to_display(self, x):
        return (x+self.coord_size[0])*self.display_size[0]/(2*self.coord_size[0])

    def display_y_to_y(self, display_y):
        return self.coord_size[1] - (2*self.coord_size[1])*display_y/self.display_size[1]

    def coord_y_to_display(self, y):
        return (self.coord_size[1]-y)*self.display_size[1]/(2*self.coord_size[1])