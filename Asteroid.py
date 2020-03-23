import pygame
from MovingObject import MovingObject, Coord

class Asteroid(MovingObject):

    def __init__(self, screen, size, r, pos = Coord(0,0), vel = Coord(0,0)):
        MovingObject.__init__(self, screen, size, pos, vel)
        self.r = r
        self.speed = 0.15
        self.dead = False

    def draw(self):
        pygame.draw.circle(self.screen, (255,255,255), self.posInt(), self.r, 1)

    def explode(self, asteroids):
        if self.r/2 > 4:
            p1 = self.pos
            v1 = Coord(self.vel.y, self.vel.x)
            asteroids.append(Asteroid(self.screen, self.size, int(self.r/2), p1, v1))
            p2 = self.pos
            v2 = Coord(-self.vel.y, -self.vel.x)
            asteroids.append(Asteroid(self.screen, self.size, int(self.r/2), p2, v2))
