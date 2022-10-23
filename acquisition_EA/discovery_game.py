#!/usr/bin/env python3

#!/usr/bin/env python3
  2 
  3 import random
  4 import pygame
  5 import os
  6 import sys
  7 import math
  8 
  9 # Global Variables
 10 COLOR = (255, 100, 98)
 11 x = 640
 12 y = 480
 13 
 14 # Object class
 15 class Hero(pygame.sprite.Sprite):
 16         def __init__(self):
 17                 super().__init__()
 18                 self.image = pygame.image.load('images/hero.png')
 19                 self.x = x/2
 20                 self.y = y/2
 21                 self.width = 100
 22                 self.height = 100
 23                 self.image = pygame.transform.scale(self.image, (self.width, self.heigh    t))
 24                 self.rect = self.image.get_rect(center=(self.x, self.y))
 25 
 26         def moveRight(self, pixels):
 27                 self.rect.x += pixels
 28 
 29         def moveLeft(self, pixels):
 30                 self.rect.x -= pixels
 31 
 32         def moveForward(self, speed):
 33                 self.rect.y += speed * speed/10
 34 
 35         def moveBack(self, speed):
 36                 self.rect.y -= speed * speed/10
 37 
 38 class WildSeq(pygame.sprite.Sprite):
 39         def __init__(self):
 40                 super().__init__()
 41                 self.image = pygame.image.load('images/wildviralseq.png')
 42                 self.x = 50
 43                 self.y = 220
 44                 self.width = 100
 45                 self.height = 15
 46                 self.image = pygame.transform.scale(self.image, (self.width, self.heigh    t))
 47                 self.rect = self.image.get_rect(center=(self.x, self.y))




             self.width = 100
 45                 self.height = 15
 46                 self.image = pygame.transform.scale(self.image, (self.width, self.heigh    t))
 47                 self.rect = self.image.get_rect(center=(self.x, self.y))
 48 
 49 class BrokenSeq(pygame.sprite.Sprite):
 50         def __init__(self):
 51                 super().__init__()
 52                 self.image = pygame.image.load('images/wildbrokenviralseq.png')
 53                 self.x = 480
 54                 self.y = 400
 55                 self.width = 80
 56                 self.height = 15
 57                 self.image = pygame.transform.scale(self.image, (self.width, self.heigh    t))
 58                 self.rect = self.image.get_rect(center=(self.x, self.y))
 59 
 60 
 61 pygame.init()
 62 
 63 size = (x, y)
 64 screen = pygame.display.set_mode(size)
 65 background =pygame.image.load('images/stage.png')
 66 
 67 
 68 all_sprites_list = pygame.sprite.Group()
 69 hero = Hero()
 70 wildseq = WildSeq()
 71 wildbrokenseq = BrokenSeq()
 72 all_sprites_list.add(hero, wildseq, wildbrokenseq)

hero = Hero()
 70 wildseq = WildSeq()
 71 wildbrokenseq = BrokenSeq()
 72 all_sprites_list.add(hero, wildseq, wildbrokenseq)
 73 
 74 run = True
 75 clock = pygame.time.Clock()
 76 
 77 while run:
 78         for event in pygame.event.get():
 79                 if event.type == pygame.QUIT:
 80                         run = False
 81                         sys.exit()
 82                 elif event.type == pygame.KEYDOWN:
 83                         if event.key == pygame.K_q:
 84                                 exit = False
 85                                 sys.exit()
 86 
 87         keys = pygame.key.get_pressed()
 88         if keys[pygame.K_LEFT]:
 89                 hero.moveLeft(10)
 90         if keys[pygame.K_RIGHT]:
 91                 hero.moveRight(10)
 92         if keys[pygame.K_DOWN]:
 93                 hero.moveForward(10)
 94         if keys[pygame.K_UP]:
 95                 hero.moveBack(10)
 96 
 97         seqfound = hero.rect.colliderect(wildseq.rect)
 98         if seqfound:
 99                 screen.fill((250, 250, 250))
100                 text = font
101                 print('collision')
102         brokenseqfound = hero.rect.colliderect(wildbrokenseq.rect)
103         if brokenseqfound:
104                 print('brokencollision')
105 
106         all_sprites_list.update()
107         screen.fill((0, 0, 0))
108         screen.blit(background, (0, 0))
109         all_sprites_list.draw(screen)
110         pygame.display.flip()
111         clock.tick(60)
112 
113 pygame.quit()

