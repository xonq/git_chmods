#!/usr/bin/env python3

import pygame

#make a class for snake
class Sprite_Sheet(object):
    #pull in filename
    def __init__(self, file_name): 
        
        #load in snake sprite
        self.sprite_sheet = pygame.image.load(file_name).convert()

    #fetch sprite from tilesheet
    def get_image(self, x, y, width, height):
        #makes a new blank image
        image = pygame.Surface([width, height]).convert()
        #pulls in a sprite from sheet
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        #image.set_colorkey(c)
        return image

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #these are attributes
        #slithering ~> frames:
        self.slither_frame = []

        #start at no movement
        self.change_x =0
        self.change_y = 0

        #list of sprites snake can run into
        #self.level = #add

        #load in images
        snake_sprite = Sprite_Sheet("snake_sprite.png")
        image = snake_sprite.get_image(0, 0, 200, 400)
        self.walking_frames_r.append(image)
        print(image)
    
    #define change speed
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    #update snake location
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
   
#initiate pygame
pygame.init()

#window dimensions
screen = pygame.display.set_mode([800, 600])

#design the background
white = (255, 255, 255)
#black = (0, 0, 0)
#red = (213, 0, 0)

#make a screen
pygame.display.update()
pygame.display.set_caption('This python will slither your organism \
    through the sequencer')

#make snake object
snake = Snake()
#add to sprite list

game_over = False

#event sequence
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                snake.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                snake.changespeed(0, -3)
            elif event.key ==pygame.K_DOWN:
                snake.changespeed(0,3)
    #updates snake location
    snake.update()

    #background load
    screen.fill(white)

    #draw sprite
    snake.draw(screen)




print('yes that ran')
pygame.quit()
quit()