import pygame
from MovingObject import MovingObject, Coord

class Asteroid(MovingObject):

    def __init__(self, screen, size, r, pos = Coord(0,0), vel = Coord(0,0)):
        MovingObject.__init__(self, screen, size, pos, vel)
        self.r = r
        self.speed = 0.15

    def draw(self):
        pygame.draw.circle(self.screen, (255,255,255), self.posInt(), self.r, 1)
