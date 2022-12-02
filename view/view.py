from Lagrange.control.controller import Controller
from Lagrange.view.coordTransform import CoordTransform

import pygame


class View:
    def __init__(self):
        self.size_display = (600, 400)
        self.size_coord = (10, 10)
        self.controller = Controller()
        self.coordTransform = CoordTransform(self.size_display, self.size_coord)

    def draw_line(self, screen, color, point_one, point_two):
        pygame.draw.line(screen, color, point_one, point_two)

    def draw_axes(self, screen):
        x_min = self.coordTransform.coord_x_to_display(self.size_coord[0] * (-1))
        x_max = self.coordTransform.coord_x_to_display(self.size_coord[0])
        y_min = self.coordTransform.coord_y_to_display(self.size_coord[1] * (-1))
        y_max = self.coordTransform.coord_y_to_display(self.size_coord[1])
        zero_x = self.coordTransform.coord_x_to_display(0)
        zero_y = self.coordTransform.coord_y_to_display(0)

        self.draw_line(screen, (0, 0, 0), (x_min, zero_y), (x_max, zero_y))
        self.draw_line(screen, (0, 0, 0), (zero_x, y_min), (zero_x, y_max))

    def draw_lagrange(self, screen):
        for x in range(self.size_display[0]):
            y = self.coordTransform.coord_y_to_display(
                self.controller.get_lagrange(self.coordTransform.display_x_to_x(x)))
            y_next = self.coordTransform.coord_y_to_display(
                self.controller.get_lagrange(self.coordTransform.display_x_to_x(x+1)))
            self.draw_line(screen, (0, 255, 0), (x, y), (x+1, y_next))

    def draw_points(self, screen):
        points = self.controller.get_points()
        for p in points:
            p_x = self.coordTransform.coord_x_to_display(p[0])
            p_y = self.coordTransform.coord_y_to_display(p[1])
            pygame.draw.circle(screen, (0, 0, 0), (p_x, p_y), 3)

    def draw_graph(self, screen, is_draw_lagrange):
        self.draw_axes(screen)
        if is_draw_lagrange:
            self.draw_points(screen)
            self.draw_lagrange(screen)

    def run(self):
        screen = pygame.display.set_mode(self.size_display, pygame.RESIZABLE)
        pygame.display.update()
        play = True
        is_draw_lagrange = False

        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play  = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x = self.coordTransform.display_x_to_x(event.pos[0])
                        y = self.coordTransform.display_y_to_y(event.pos[1])
                        self.controller.add_point(x, y)
                        is_draw_lagrange = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.controller.reset()
                        is_draw_lagrange = False
                screen.fill('WHITE')
                self.draw_graph(screen, is_draw_lagrange)
                pygame.display.update()
