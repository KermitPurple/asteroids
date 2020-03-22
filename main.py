import pygame, os
from Asteroid import Asteroid, Coord
os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"

pygame.display.init()
size = Coord(600, 600)
screen = pygame.display.set_mode(size)
asteroids = []
for i in range(30):
    asteroids.append(Asteroid(screen, size, 20))
    asteroids[i].randomPos()
    asteroids[i].randomVel()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    for asteroid in asteroids:
        asteroid.update()
        asteroid.draw()
    pygame.display.update()

