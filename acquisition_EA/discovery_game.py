#!/usr/bin/env python3
 
import random
import pygame
import os
import sys
import math
from pygame import mixer
 
# Global Variables
x = 640
y = 480
 
# Object class
class Hero(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()
                self.image = pygame.image.load('images/hero.png')
                self.x = x/2
                self.y = y/2
                self.width = 100
                self.height = 100
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                self.rect = self.image.get_rect(center=(self.x, self.y))
 
        def moveRight(self, pixels):
                self.rect.x += pixels
 
        def moveLeft(self, pixels):
                self.rect.x -= pixels
 
        def moveForward(self, speed):
                self.rect.y += speed * speed/10

        def moveBack(self, speed):
                self.rect.y -= speed * speed/10
 
class HideWildSeq(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()
                self.image = pygame.image.load('images/stage-seq1.png')
                self.x = 50
                self.y = 220
                self.width = 62
                self.height = 64
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                self.rect = self.image.get_rect(center=(self.x, self.y))

class HideBrokenSeq(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()
                self.image = pygame.image.load('images/stage-seq2.png')
                self.x = 540
                self.y = 400
                self.width = 68
                self.height = 62
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                self.rect = self.image.get_rect(center=(self.x, self.y))

class WildSeq(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()
                self.image = pygame.image.load('images/wildviralseq.png')
                self.x = 50
                self.y = 220
                self.width = 400
                self.height = 20
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                self.rect = self.image.get_rect(center=(self.x, self.y))

class BrokenSeq(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()
                self.image = pygame.image.load('images/wildbrokenviralseq.png')
                self.x = 540
                self.y = 400
                self.width = 300
                self.height = 20
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                self.rect = self.image.get_rect(center=(self.x, self.y))
  
def main(): 
 pygame.init()
 clock = pygame.time.Clock()
 #background
 size = (x, y)
 screen = pygame.display.set_mode(size)
 background =pygame.image.load('images/stage.png')
 mixer.music.load('sounds/minuet-of-forest.mp3')
 mixer.music.set_volume(0.25)
 mixer.music.play(-1) 

 all_sprites_list = pygame.sprite.Group()
 hero = Hero()
 hiddenseq1 = HideWildSeq()
 hiddenseq2 = HideBrokenSeq()
 all_sprites_list.add(hero, hiddenseq1, hiddenseq2)

 wild_sprite_list = pygame.sprite.Group()
 wildseq = WildSeq()
 wild_sprite_list.add(wildseq)
 wild_broken_sprite_list = pygame.sprite.Group()
 wildbrokenseq = BrokenSeq()
 wild_broken_sprite_list.add(wildbrokenseq)

 def text_object(text, font):
        textSurface = font.render(text, True, (0, 0, 0))
        return textSurface, textSurface.get_rect()
 def message_display(text):
        popuptext = pygame.font.SysFont('gilsans', 42)
        TextSurf, TextRect = text_object(text, popuptext)
        TextRect.center = ((x/2), (y/2))
        screen.fill((250, 250, 250))
        screen.blit(TextSurf, TextRect)
        pygame.display.update()

 def wild(collision):
        wild_sprite_list.draw(screen)
        pygame.display.update()
        pygame.time.delay(1000)
        message_display("You've Found a Wild Sequence")
        pygame.time.delay(2000)
        sys.exit()

 def broken(collision):
        wild_broken_sprite_list.draw(screen)
        pygame.display.update()
        pygame.time.delay(1000)
        message_display("Found broken sequence! Try again!")
        pygame.time.delay(1500)

 run = True

 while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
                        sys.exit()
                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                                run = False
                                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
                hero.moveLeft(10)
        if keys[pygame.K_RIGHT]:
                hero.moveRight(10)
        if keys[pygame.K_DOWN]:
                hero.moveForward(10)
        if keys[pygame.K_UP]:
                hero.moveBack(10)

        seqfound = hero.rect.colliderect(hiddenseq1.rect)
        if seqfound:
                wildseqfound = mixer.Sound('sounds/06-caught-a-pokemon.mp3')
                wildseqfound.play()
                wild(seqfound)

        brokenseqfound = hero.rect.colliderect(hiddenseq2.rect)
        if brokenseqfound:
                brokenseqfound = mixer.Sound('sounds/spongebob-boowomp.mp3')
                brokenseqfound.play()
                broken(brokenseqfound) 
                pygame.display.update()
               

        all_sprites_list.update()
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)


 pygame.quit()

if __name__ == "__main__":
      main()
