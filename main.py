import pygame, os
from Asteroid import Asteroid, Coord
from Ship import Ship
from Bullet import Bullet
os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"

def tik():
    global tiks
    tiks += 1
    if tiks >= 10000:
        tiks = 0

pygame.display.init()
size = Coord(600, 600)
screen = pygame.display.set_mode(size)
tiks = 0
asteroids = []
bullets = []
for i in range(10):
    asteroids.append(Asteroid(screen, size, 50))
    asteroids[i].randomPos()
    asteroids[i].randomVel()
player = Ship(screen, size)
pygame.key.set_repeat(80)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.unicode == "e":
                for asteroid in asteroids:
                    asteroid.dead = True
    if tiks % 20 == 0:
        player.kbin(bullets)
    screen.fill((0,0,0))
    for i, asteroid in enumerate(asteroids):
        asteroid.update()
        asteroid.draw()
        if asteroid.dead:
            asteroid.explode(asteroids)
            _ = asteroids.pop(i)
    for i, bullet in enumerate(bullets):
        bullet.update()
        bullet.draw()
        bullet.collide(asteroids)
        if bullet.dead:
            _ = bullets.pop(i)
    player.update()
    player.draw()
    pygame.display.update()
    tik()
