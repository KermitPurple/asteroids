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

    def collide(self, asteroids):
        for asteroid in asteroids:
            if self.pos.x + self.r > asteroid.pos.x - asteroid.r and self.pos.x - self.r < asteroid.pos.x + asteroid.r and self.pos.y + self.r > asteroid.pos.y - asteroid.r and self.pos.y - self.r < asteroid.pos.y + asteroid.r:
                asteroid.dead = True
                self.dead = True
