#!/usr/bin/env python3
import pygame
import random



class SpriteSheet(object):
    def __init__(self, file_name):
        self.file_name = file_name #define filename from input
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha() #make obj. sheet and load
    def get_image(self, x, y, width, height): #fun to get image with basic attributes
        image = pygame.Surface([width, height]).convert_alpha() #mk image obj = Surface
        image.blit(self.sprite_sheet, (0,0), (x, y, width, height)) #add Rect info to imageSurface
        return image
        #blit()draws an image onto onther. In this case, sprite_sheet onto image
        # at the same time is defining the image rect as 
        # (0,0) defines the upper left rect  

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, file_name, x, y, width, height, orient):
        super().__init__()
        #make an image object with attributes
        self.file_name = file_name
        sprite_sheet = SpriteSheet(file_name)
        print(f'loading in image from {file_name}')
        self.image = pygame.transform.rotate(sprite_sheet.get_image(0, 0, width, height), orient)
        print(f'for image, {self.image}, type is type{self.image}')
        
        #oldcolor test
       # self.image = pygame.Surface([width, height])
        #self.image.fill(color)

        #give image objects Rect coordinates
        self.rect = self.image.get_rect() #get_rect reads in coordinates from \ 
        #self.image that covers the whole surface
        self.rect.x = x
        self.rect.y = y
        print(f'self.rect: {self.rect} is a {type(self.rect)}')

        #add boundaries and collision
        self.top_boundary = 0
        self.bottom_boundary = 0
        self.left_boundary = 0
        self.right_boundary = 0
        self.passed = False
        self.world_shift = None

class Level():
    def __init__(self, player):
        super().__init__()
        self.background = None
        self.player = player
        self.world_shift = 0
        self.background = pygame.image.load("landscape.png").convert_alpha()
        self.background.set_alpha(5)


    def draw(self, screen):
        screen.blit(self.background, (self.world_shift // 3, 0))
    
    def shift_world(self, shift_x):
        self.world_shift += shift_x


class Player(pygame.sprite.Sprite):
    def __init__(self, file_name, x, y):
        super().__init__()
        #make an image object with attributes
        self.file_name = file_name
        sprite_sheet = SpriteSheet(file_name)
        print(f'loading in image from {file_name}')
        self.image = sprite_sheet.get_image(0, 0, 20, 20) #placeholder for image just to define rect

        #lists for direction facing
        self.face_R = []
        self.face_L = []
        self.face_UP = []
        self.face_DN = []

        #make pull randomly from each list? or cycle
        #right facing snakes
        image = pygame.transform.scale(sprite_sheet.get_image(5, 48, 20, 20), [40, 40])      
        self.face_L.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(68, 48, 20, 20), [40, 40])       
        self.face_L.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(166, 83, 20, 20), [40, 40])        
        self.face_L.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(165, 112, 20, 20), [40, 40])
        self.face_L.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(105, 112, 20, 20), [40, 40])
        self.face_L.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(132, 112, 20, 20), [40, 40])
        self.face_L.append(image)

        #flipr for R
        for obj in self.face_L:
            self.face_R.append(pygame.transform.flip(obj, True, False))
        #rotate for Up
        for obj in self.face_L:
            self.face_UP.append(pygame.transform.rotate(obj, -90))
        #flip up for down
        for obj in self.face_UP:
            self.face_DN.append(pygame.transform.flip(obj, False, True))

        #make image rect!
        self.rect = self.image.get_rect() #adds width/height
        self.rect.x = x #adds coordinates
        self.rect.y = y

        #defines an intial speed
        self.change_x = 0
        self.change_y = 0
        self.direction = "R"

        self.world_shift= None

    def update(self):
        #change image based on direction input
        self.rect.x += self.change_x
        pos = self.rect.x + self.world_shift
        self.rect.y += self.change_y
        if self.direction == "R":
            frame = (pos//30) % len(self.face_R)
            self.image = self.face_R[frame]
        elif self.direction == "L":
            frame = (pos//30) % len(self.face_L)
            self.image = self.face_L[frame]
        elif self.direction == "UP":
            frame = (self.rect.y//30) % len(self.face_UP)
            self.image = self.face_UP[frame]
        else:
            frame = (self.rect.y//30) % len(self.face_DN)
            self.image = self.face_DN[frame]
        
        #keep on screen
        width=640 
        height=480
        if self.rect.x <0:
            self.rect.x = 0
        if self.rect.x > width -1:
            self.rect.x = width -1
        if self.rect.y <0:
            self.rect.y = 0
        if self.rect.y >= height - 1 :
            self.rect.y = height -1 
        
        #define movement
    
    ##defines directions of movement based on direction input
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




def main():
    # Call this function so the Pygame library can initialize itself
    pygame.init()
    print("initalizing")

    WHITE = (255, 255, 255)
    green= (124, 252, 0)
    width=640 
    height=480

    #create screen
    screen = pygame.display.set_mode([width, height]) #makes a window/screen to display
    # Set the title of the window
    pygame.display.set_caption('python!')


    #make two obstacles, add them to block_list
    block_W = 46
    block_H = 375
    
    block_file = "pore_sprite.png"
    
    block_list = pygame.sprite.Group() #makes block_list a sprite group

    #randomize coordinates
    block_coord_x1 = [random.randrange(50, 100), random.randrange(200, 300), random.randrange(350,500),\
        random.randrange(550, 600)]
    block_coord_y = [random.randrange(50, 100, 10), random.randrange(100, 200), random.randrange(50, 300), \
        random.randrange(50, 300)]
    block_big = [] #list of blocks
    for i in [0, 1, 2, 3]:
        block1= Obstacle(block_file, block_coord_x1[i], -block_coord_y[i], block_W, block_H, 0)
        block_coord_y2 = -(block_coord_y[i]) + 350
        block2= Obstacle(block_file, block_coord_x1[i], block_coord_y2, block_W, block_H, -180)
        print(f'block coodry: {block_coord_y[i]}, {block_coord_y2}')
        block_big.append(block1) 
        block_big.append(block2)
        block_list.add(block_big)
        

    #block_coord= [(0,0), (350, 350)]
    #for i in [0,1]:
     #   block= Obstacle(block_file, block_coord[i][0], block_coord[i][1], block_W, block_H)
      #  print(f' for {block_file} at pos {block.rect.x, block.rect.y}, with dimensions: {block_W, block_H}')
       # block_list.add(block)
        #print(block_list, block.rect, block.image)
    #make a level
    

    #make a sprite
    player_sprite = pygame.sprite.Group()
    sprite_file = 'snake_sprite.png'
    player=Player(sprite_file, 20, 150)
    player_sprite.add(player)
    level=Level(player)

    clock = pygame.time.Clock()
    done = False
 
    while not done:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
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
            
            collisions = pygame.sprite.spritecollide(player, block_list, True)
            if collisions:
                print('oh no')
                return

            if player.rect.right >=500:
                diff = player.rect.right - 500
                player.rect.right = 500
                #current_level.shift_world(-diff)

    # --- Game logic
        player_sprite.update()
    
    # place objects
        #screen.fill(WHITE)
        #screen.blit(back_image, (0,0))
        player_sprite.draw(screen)
        block_list.draw(screen)
        level.draw(screen)
        screen.blit(background_image, [0,0])
       
 
    # Flip screen
        pygame.display.flip()
 
    # Pause
        clock.tick(30)
 
    pygame.quit()

if __name__ == '__main__':
    main()