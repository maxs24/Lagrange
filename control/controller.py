import math

from Lagrange.model.polynomialLagrange import PolynomialLagrange


class Controller:
    def __init__(self):
        self.lagrange = PolynomialLagrange()

    def add_point(self, x, y):
        if self.is_close(x, y):
            self.lagrange.add_point(x, y)

    def is_close(self, x, y):
        points = self.lagrange.get_points()
        for p in points:
            if p[0] == x:
                return False
        return True
    def reset(self):
        self.lagrange.delete_all_points()

    def get_lagrange(self, x):
        return self.lagrange.lagrange(x)

    def get_points(self):
        return self.lagrange.get_points()
