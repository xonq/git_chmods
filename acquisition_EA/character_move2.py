#!/usr/bin/env python3

import pygame
from pygame.locals import *
import os


class GameObject:
     def __init__(self, image, height, speed):
         self.speed = speed
         self.image = image
         self.pos = image.get_rect().move(0, height)
     def move(self):
       if right:
         self.pos.right += self.speed
       if left:
         self.pos.right -= self.speed
       if down:
         self.pos.top += self.speed
       if up:
         self.pos.top -= self.speed
       if self.pos.right > WIDTH:
         self.pos.left = 0
       if self.pos.top > HEIGHT-SPRITE_HEIGHT:
         self.pos.top = 0
       if self.pos.right < SPRITE_WIDTH:
         self.pos.right = WIDTH
       if self.pos.top < 0:
         self.pos.top = HEIGHT-SPRITE_HEIGHT





screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()            #get a pygame clock object
player = pygame.image.load(os.path.join('images', 'hero.png')).convert()
background = pygame.image.load(os.path.join('images', 'stage.png')).convert()
screen.blit(background, (0, 0))
objects = []
p = GameObject(player, 10, 3)          #create the player object
while True:
     keys = pygame.key.get_pressed()
     if keys[pygame.K_UP]:
         p.move(up=True)
     if keys[pygame.K_DOWN]:
         p.move(down=True)
     if keys[pygame.K_LEFT]:
         p.move(left=True)
     if keys[pygame.K_RIGHT]:
         p.move(right=True)
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             sys.exit()
     for o in objects:
         screen.blit(background, o.pos, o.pos)
     for o in objects:
         o.move()
         screen.blit(o.image, o.pos)
     pygame.display.update()
     clock.tick(60)
