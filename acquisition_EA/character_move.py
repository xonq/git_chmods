#!/usr/bin/env python3

from typing import Tuple

import pygame
import sys
import os

'''
Variables
'''

worldx = 960
worldy = 720
fps = 40
speed = 3
ani = 100
world = pygame.display.set_mode([worldx, worldy])

player = pygame.image.load(os.path.join('images', 'stage.png'))

'''
Setup
'''

backdrop = pygame.image.load(os.path.join('images', 'stage.png'))
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

#player = Player()  # spawn player
player.rect.x = 400  # go to x
player.rect.y = 400  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10

def player(x,y):
    gameDisplay.blit(player, (x,y))

x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0

'''
Main Loop
'''

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                x_change -= speed 
   #             print('left')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                x-cahnge += speed 
   #             print('right')
            if event.key == pygame.K_UP or event.key == ord('w'):
                y += speed
   #              print('jump')
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                y -= speed 
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    world.blit(backdrop, backdropbox)
    player.update()
    player_list.draw(world) #draw player
    pygame.display.flip()
    clock.tick(fps)
