import pygame
from random import random, randint
from numpy import sin, cos
from collections import namedtuple

Coord = namedtuple("Coord", ('x', 'y'))

class Asteroid:

    def __init__(self, screen, size, r, pos = Coord(0,0), vel = Coord(0,0)):
        self.screen = screen
        self.size = size
        self.r = r
        self.pos = pos
        self.vel = vel

    def randomPos(self):
        self.pos = Coord(randint(0, self.size.x), randint(0, self.size.y))
    
    def randomVel(self):
        theta = random() * 5
        self.vel = Coord(cos(theta), sin(theta))

    def draw(self):
        pygame.draw.circle(self.screen, (255,255,255), self.pos, self.r, 1)
