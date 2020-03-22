import pygame
from numpy import pi
from Asteroid import Coord, Asteroid
from MovingObject import MovingObject, Coord

class Ship(MovingObject):

    def __init__(self, screen, size, pos = None, vel = Coord(0,0)):
        if pos == None:
            pos = Coord(size.x/2, size.y/2)
        MovingObject.__init__(self, screen, size, pos, vel)
        self.angle = 0
        self.r = 20

    def rads(self):
        return self.angle / 180 * pi

    def draw(self):
        points = [
            Coord(self.pos.x, self.pos.y - self.r),
            Coord(self.pos.x - self.r/2, self.pos.y + self.r),
            Coord(self.pos.x + self.r/2, self.pos.y + self.r),
            ]
        pygame.draw.polygon(self.screen, (255,255,255), points, 1)
