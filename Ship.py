import pygame
from numpy import sin, cos, pi
from Asteroid import Coord, Asteroid
from Bullet import Bullet
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
    
    def update(self):
        MovingObject.update(self)
        self.vel = Coord(0,0)

    def draw(self):
        points = [
            Coord(self.pos.x, self.pos.y - self.r),
            Coord(self.pos.x - self.r/2, self.pos.y + self.r),
            Coord(self.pos.x + self.r/2, self.pos.y + self.r),
            ]
        for i, point in enumerate(points):
            new_point = Coord(
                    self.pos.x + cos(self.rads()) * (point.x - self.pos.x) - sin(self.rads()) * (point.y - self.pos.y),
                    self.pos.y + sin(self.rads()) * (point.x - self.pos.x) + cos(self.rads()) * (point.y - self.pos.y)
                    )
            points[i] = new_point
        pygame.draw.polygon(self.screen, (255,255,255), points, 1)

    def kbin(self, bullets):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle -= 15
            if self.angle <= -360:
                self.angle = 0
        if keys[pygame.K_RIGHT]:
            self.angle += 15
            if self.angle >= 360:
                self.angle = 0
        if keys[pygame.K_UP]:
            self.move(Coord(10,-10))
        if keys[pygame.K_DOWN]:
            self.move(Coord(-10,10))
        if keys[pygame.K_SPACE]:
            bullets.append(self.fireBullet())

    def move(self, v):
        self.vel = Coord(
                self.vel.x + sin(self.rads()) * v.x, 
                self.vel.y + cos(self.rads()) * v.y
                )

    def fireBullet(self):
        speed = 2
        v = Coord(
                sin(self.rads()) * speed,
                cos(self.rads()) * -speed
                )
        return Bullet(self.screen, self.size, self.pos, v) 

