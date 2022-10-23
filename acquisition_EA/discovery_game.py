#!/usr/bin/env python3
#elaine aquino

import pygame
from pygame.locals import *
pygame.init()

#environment
background = pygame.display.set_mode((600, 600))

# character/sprite images to flip thru
player_image = pygame.image.load(r'Sprite1-200x200.png')

# create clock object to track time
clock = pygame.time.Clock()

# create variable to iterate over the sprite list
# value = 0

# boolean variable for while loop
run = True

# boolean variable for moving
# moving = False

# velocity variable
velocity = 12

# starting coordinates of player 
x = 100
y = 150

# infinite loop to run game 
while run:
	clock.tick(60) # frame rate
	background.blit(player_image, (x, y))
	background.fill((0, 0, 0))
	for event in pygame.event.get(): # iterate over list of events returned by method
		if event.type == pygame.QUIT: # close window and program if event is quit
			run = False
			pygame.quit()
			quit
		key_pressed_is = pygame.key.get_pressed()
		if key_pressed_is[K_LEFT]: # decresing x coordinate with left arrow key
			x -= 8
		if key_pressed_is[K_RIGHT]: # increasing x coordinate with right arrow key
			x += 8
		if key_pressed_is[K_UP]: # decreasing y coordinate with up arrow key
			y -= 8
		if key_pressed_is[K_DOWN]:
			y += 8
		pygame.display.update()

