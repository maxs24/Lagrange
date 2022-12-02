

class PolynomialLagrange:
    def __init__(self):
        self.n = 0
        self.points = []

    def add_point(self, x, y):
        self.points.append((x, y))
        self.n += 1

    def delete_all_points(self):
        self.points = []
        self.n = 0

    def lagrange(self, x):
        value_lagrange = 0
        for i in range(self.n):
            value_lagrange += self.points[i][1] * self.basic_polynom(x, i)
        return value_lagrange

    def basic_polynom(self, x, i):
        value_basic = 1
        for j in range(self.n):
            if j != i:
                if self.points[i][0] - self.points[j][0] == 0:
                    print("Ошибка")
                value_basic *= (x - self.points[j][0])/(self.points[i][0] - self.points[j][0])
        return value_basic

    def get_points(self):
        return self.points
