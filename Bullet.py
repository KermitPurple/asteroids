import pygame
from MovingObject import MovingObject

class Bullet(MovingObject):

    def __init__(self, screen, size, pos , vel):
        MovingObject.__init__(self, screen, size, pos, vel)
        self.r = 5
        self.dead = False

    def update(self):
        if not MovingObject.update(self, False):
            self.dead = True

    def draw(self):
        pygame.draw.circle(self.screen, (255,255,255) ,self.posInt(), self.r)
