import pygame, os
from Asteroid import Asteroid, Coord
from Ship import Ship
from Bullet import Bullet
os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"

pygame.display.init()
size = Coord(600, 600)
screen = pygame.display.set_mode(size)
asteroids = []
bullets = []
for i in range(10):
    asteroids.append(Asteroid(screen, size, 20))
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
            player.kbin(bullets)
    screen.fill((0,0,0))
    for asteroid in asteroids:
        asteroid.update()
        asteroid.draw()
    for i, bullet in enumerate(bullets):
        bullet.update()
        bullet.draw()
        if bullet.dead:
            _ = bullets.pop(i)
    player.update()
    player.draw()
    pygame.display.update()

