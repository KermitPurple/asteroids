import pygame
from random import random, randint, uniform
from numpy import sin, cos, pi
from collections import namedtuple

Coord = namedtuple("Coord", ('x', 'y'))

class MovingObject:

    def __init__(self, screen, size, pos, vel):
        self.screen = screen
        self.size = size
        self.pos = pos
        self.vel = vel

    def randomPos(self):
        self.pos = Coord(randint(0, self.size.x), randint(0, self.size.y))
    
    def randomVel(self):
        theta = uniform(0, 2 * pi)
        self.vel = Coord(cos(theta) * self.speed, sin(theta) * self.speed)

    def posInt(self):
        return Coord(int(self.pos.x), int(self.pos.y))

    def update(self, repeat = True):
        pos = Coord(self.pos.x + self.vel.x, self.pos.y + self.vel.y)
        if pos.x - self.r > self.size.x:
            if repeat:
                pos = Coord(-self.r, pos.y)
            return False
        if pos.x + self.r < 0:
            if repeat:
                pos = Coord(self.size.x + self.r, pos.y)
            return False
        if pos.y -self.r > self.size.y:
            if repeat:
                pos = Coord(pos.x, -self.r)
            return False
        if pos.y + self.r< 0:
            if repeat:
                pos = Coord(pos.x, self.size.y + self.r)
            return False
        self.pos = pos
        return True
