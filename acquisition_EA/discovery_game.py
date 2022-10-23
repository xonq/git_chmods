#!/usr/bin/env python3
 
import random
import pygame
import os
import sys
import math
 
# Global Variables
COLOR = (255, 100, 98)
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
 
class WildSeq(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()
                self.image = pygame.image.load('images/wildviralseq.png')
                self.x = 50
                self.y = 220
                self.width = 100
                self.height = 15
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                self.rect = self.image.get_rect(center=(self.x, self.y))
 
class BrokenSeq(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()
                self.image = pygame.image.load('images/wildbrokenviralseq.png')
                self.x = 480
                self.y = 400
                self.width = 80
                self.height = 15
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                self.rect = self.image.get_rect(center=(self.x, self.y))
  
def main() 
pygame.init()
clock = pygame.time.Clock()
size = (x, y)
screen = pygame.display.set_mode(size)
background =pygame.image.load('images/stage.png')


all_sprites_list = pygame.sprite.Group()
hero = Hero()
wildseq = WildSeq()
wildbrokenseq = BrokenSeq()
all_sprites_list.add(hero, wildseq, wildbrokenseq)

def text_object(text, font):
	textSurface = font.render(text, True, (0, 0, 0))
	return textSurface, textSurface.get_rect()
def message_display(text):
	popuptext = pygame.font.SysFont('gilsans', 32)
	TextSurf, TextRect = text_object(text, popuptext)
	TextRect.center = ((x/2), (y/2))
	screen.blit(TextSurf, TextRect)

	pygame.display.update()
	
 
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

        seqfound = hero.rect.colliderect(wildseq.rect)
        if seqfound:
                screen.fill((250, 250, 250))
                message_display("You've found a wild sequence!")
                pygame.time.delay(2000)
                sys.exit()

        brokenseqfound = hero.rect.colliderect(wildbrokenseq.rect)
        if brokenseqfound:
                screen.fill((250, 250, 250))
                message_display("You've found a broken sequence, try again")
                pygame.time.delay(2000)
                play.again()                


        all_sprites_list.update()
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)


pygame.quit()

if __name__ == "__main__":
	main()
