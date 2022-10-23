#!/usr/bin/env python3

import pygame
import subprocess
import random

# make fighter class

simonisms = ['You got me fucker', 'splendid', 'great form', 'keen for another round', 'wanker',
             'buy me a drink first', 'bloody hell']

class Fighter():
    def __init__(self, x, y):
        self.flip = False
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0

        #get keypresses
        key = pygame.key.get_pressed()

        #can only perform other actions if only not attacking
        if self.attacking == False:

        #movement
            if key[pygame.K_a]:
                dx = -SPEED
            if key[pygame.K_d]:
                dx = SPEED

            #jumping
            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -30
                self.jump = True

            #attacks
            if key[pygame.K_r] or key[pygame.K_t]:
                self.attack(surface, target)

                #which attack type is used
                if key[pygame.K_r]:
                    self.attack_type = 1
                if key[pygame.K_t]:
                    self.attack_type = 2

            # apply gravity
            self.vel_y += GRAVITY
            dy += self.vel_y

            #make player stay on screen
            if self.rect.left + dx < 0:
                dx = -self.rect.left
            if self.rect.right + dx > screen_width:
                dx = screen_width - self.rect.right
            if self.rect.bottom + dy > screen_height - 45:
                self.vel_y = 0
                self.jump = False
                dy = screen_height - 45 - self.rect.bottom

            #make players face each other
            if target.rect.centerx > self.rect.centerx:
                self.flip = False
            else:
                self.flip = True


            # update player position
            self.rect.x += dx
            self.rect.y += dy

        #define attack method

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height) #makes attack surface 2x the player
        if attacking_rect.colliderect(target.rect):
            voice_cmd = f'say -v Daniel "{random.choice(simonisms)}"'
            subprocess.Popen(voice_cmd, shell=True)
            target.health -= 10

        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)




