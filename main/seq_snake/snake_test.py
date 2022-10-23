#!/usr/bin/env python3
import pygame
import random

WHITE = (255, 255, 255)

class SpriteSheet(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.sprite_sheet = pygame.image.load(file_name).convert()
    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0,0), (x, y, width, height))
        return image



class Player(pygame.sprite.Sprite):
 
    # -- Methods
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        sprite_sheet = SpriteSheet('snake_sprite.png')
        self.image = sprite_sheet.get_image(103, 12, 20, 20)
        print("loading in sprite")
        
        self.face_R = []
        self.face_L = []
        self.face_UP = []
        self.face_DN = []

        self.direction = "D"

        #make pull randomly from each list? or cycle
        #right facing snakes
        image = sprite_sheet.get_image(5, 48, 20, 20)
        self.face_L.append(image)
        image = sprite_sheet.get_image(68, 48, 20, 20)
        self.face_L.append(image)
        image = sprite_sheet.get_image(166, 83, 20, 20)
        self.face_L.append(image)
        image = sprite_sheet.get_image(165, 112, 20, 20)
        self.face_L.append(image)
        image = sprite_sheet.get_image(105, 112, 20, 20)
        self.face_L.append(image)
        image = sprite_sheet.get_image(132, 112, 20, 20)
        self.face_L.append(image)
        self.face_L[0].get_view()
        print(self.face_L[1], type(self.face_L[1]))
        #self.image = self.face_L[0]

        #Left to right flip
        for obj in self.face_L:
            temp = pygame.transform.flip(obj, True, False)
            self.face_R.append(temp)

        
        #fix up/down sprites have black
        #define UP sprites
        image = sprite_sheet.get_image(71, 142, 20, 20)
        self.face_UP.append(image)
        image = sprite_sheet.get_image(16, 142, 20, 20)
        self.face_UP.append(image)
        image = sprite_sheet.get_image(165, 142, 20, 20)
        self.face_UP.append(image)
        image = pygame.transform.rotate(sprite_sheet.get_image(197, 81, 20, 20), -90)
        self.face_UP.append(image)
        image = pygame.transform.rotate(sprite_sheet.get_image(69, 50, 20, 20), -90)
        self.face_UP.append(image)
        image = pygame.transform.rotate(sprite_sheet.get_image(6, 50, 20, 20), -90)
        self.face_UP.append(image)

        #define down
        for obj in self.face_UP:
            self.face_DN.append(pygame.transform.flip(obj, False, True))
       # print("defining scale")
        #for obj in self.face_DN:
        #    self.face_DN.append(pygame.transform.scale(self.image, [40, 40]))
       # print("sprites scaled to 60x60")
        #self.image = self.face_R[0]
        
        

        #self.image = pygame.transform.scale(self.image, [60, 60])
        #print("sprites scaled to 60x60")
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
    
    
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.direction == "R":
            frame = (self.rect.x//30) % len(self.face_R)
            self.image = self.face_R[frame]
        elif self.direction == "L":
            frame = (self.rect.x//30) % len(self.face_L)
            self.image = self.face_L[frame]
        elif self.direction == "UP":
            frame = (self.rect.y//30) % len(self.face_UP)
            self.image = self.face_UP[frame]
        else:
            frame = (self.rect.y//30) % len(self.face_DN)
            self.image = self.face_DN[frame]
    
    def go_left(self):
        self.change_x = -3
        self.direction = "L"

    def go_right(self):
        self.change_x = 3
        self.direction = "R"
    
    def go_up(self):
        self.change_y = -3
        self.direction = "UP"

    def go_down(self):
        self.change_y = 3
        self.direction = "DOWN"

    def stop(self):
        self.change_x = 0
        self.change_y = 0

        

#Define class for obstacles/pores


def main():
    # Call this function so the Pygame library can initialize itself
    pygame.init()
    print("initalizing")
    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])
 
    # Set the title of the window
    pygame.display.set_caption('Test')
 
    # Create the player object
    player = Player(100, 100)
    #player.rect.x = 340
    #player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(player)
    print(all_sprites_list)
 
    #snake_image = pygame.image.load("snake_sprite.png").convert()

    clock = pygame.time.Clock()
    done = False
 
    while not done:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
        # Set the speed based on the key pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                elif event.key == pygame.K_RIGHT:
                    player.go_right()
                elif event.key == pygame.K_UP:
                    player.go_up()
                elif event.key == pygame.K_DOWN:
                    player.go_down()
 
        # Reset speed when key goes up
            if event.type == pygame.KEYUP:
                player.stop()

 
    # --- Game logic
     
    # This calls update on all the sprites
        all_sprites_list.update()
       #screen.blit(snake_image, [50, 50])
 
    # -- Draw everything
    # Clear screen
        screen.fill(WHITE)
 
    # Draw sprites
        all_sprites_list.draw(screen)
 
    # Flip screen
        pygame.display.flip()
 
    # Pause
        clock.tick(60)
 
    pygame.quit()

if __name__ == '__main__':
    main()