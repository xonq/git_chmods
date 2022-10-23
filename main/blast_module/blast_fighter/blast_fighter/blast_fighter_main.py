#!/usr/bin/env python3

import pygame
import subprocess

from pygame.surface import Surface, SurfaceType

from fighters import Fighter

pygame.init()

# create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen: Surface | SurfaceType = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Blast Brawl')

# set framerate
clock = pygame.time.Clock()
FPS = 60

#define colors
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# load background image
bg_image = pygame.image.load('blast_fighter/assets/images/background/8pixel_lab.jpg').convert_alpha()


# add a fxn for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

#fxn for drawing health
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 3, y - 3, 406, 36))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))


# create 2 instances of fighters
fighter_1 = Fighter(200, 0)
fighter_2 = Fighter(700, 375)

# create game loop
count = 0
run = True
while run:

    #set framerate
    clock.tick(FPS)

    # draw background
    draw_bg()

    #draw health bar
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)

    #move fighters
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
    #fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT)

    # draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display
    pygame.display.update()

    if not count:
        voice_cmd = 'say -v Daniel "hello, this is Simon, ' \
                   + 'the wizard of Cold Spring Harbor Laboratory. ' \
                  + 'Prepare for me to BLAST your ass."'
        subprocess.Popen(voice_cmd, shell=True)
        count += 1

# exit pygame
pygame.quit()
