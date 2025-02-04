from random import random

import pygame, random

from pygame.locals import *

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def collision(c1,c1):
    return(c1[0] == c2[0]) and (c1[1] == c2[1])


UP =0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Goob')


goob = [(200, 200), (210, 200), (220, 200)]
goob_skin = pygame.Surface((10,10))
goob_skin.fill((255,255,255))

apple_pos = (random.randint(0,590), random.randint(0,590))
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key != K_UP:
                my_direction UP
            if event.key == K_DOWN:
                my_direction DOWN
            if event.key == K_RIGHT:
                my_direction RIGHT
            if event.key == K_LEFT:
                my_direction LEFT

        if collision(goob[0], apple_pos):
            apple_pos = on_grid_random()
            goob.append((0,0))


    if my_direction == UP:
        goob[0] = (goob[0][0], goob[0][1] - 10)
    if my_direction == DOWN:
        goob[0] = (goob[0][0], goob[0][1] + 10)
    if my_direction == RIGHT:
        goob[0] = (goob[0][0] + 10, goob[0][1])
    if my_direction == LEFT:
        goob[0] = (goob[0][0] - 10, goob[0][1] - 10)

    for i in range(len(goob) - 1, 0, -1):
        goob[i] = (goob[i-1][0], goob[i-1][1])

    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    for pos in goob:
        screen.blit(goob_skin, pos)

    pygame.display.update()






