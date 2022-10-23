#!/usr/bin/env python3
import pygame
import random

WHITE = (255, 255, 255)
green= (124, 252, 0)

class SpriteSheet(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.sprite_sheet = pygame.image.load(file_name).convert()
    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0,0), (x, y, width, height))
        return image


class Pore(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        #make a list to hold your two sprite block
        self.pore_Lshift = []

        sprite_sheet = SpriteSheet('pore_sprite.png')
        print(f'fetching nanopores from {sprite_sheet}')
        image = pygame.transform.scale(sprite_sheet.get_image(0, 0, 40, 750), [50, 1500])
        self.pore_Lshift.append(image)
        #initiate pore position
        self.image = self.pore_Lshift[0]

        self.top_boundary = 0
        self.bottom_boundary = 0
        self.left_boundary = 0
        self.right_boundary = 0
        self.passed = False

        #blit Pore(x, y) inputs at position in screen
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #edf block, change
        self.change_x = 0


        


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

        #Left to right flip
        for obj in self.face_L:
            temp = pygame.transform.flip(obj, True, False)
            self.face_R.append(temp)

        #define UP sprites
        image = pygame.transform.rotate(sprite_sheet.get_image(5, 48, 20, 20), -90)
        self.face_UP.append(image)
        image = pygame.transform.rotate(sprite_sheet.get_image(68, 48, 20, 20), -90) 
        self.face_UP.append(image)
        image = pygame.transform.rotate(sprite_sheet.get_image(166, 83, 20, 20), -90)
        self.face_UP.append(image)
        image = pygame.transform.rotate(sprite_sheet.get_image(165, 112, 20, 20), -90)
        self.face_UP.append(image)
        image = pygame.transform.rotate(sprite_sheet.get_image(105, 112, 20, 20), -90)
        self.face_UP.append(image)
        image = pygame.transform.rotate(sprite_sheet.get_image(132, 112, 20, 20), -90)
        self.face_UP.append(image)

        self.face_L2 = []
        self.face_R2 = []
        self.face_UP2 = []
        self.face_DN2 = []

        #define down by flipping up
        for obj in self.face_UP:
            self.face_DN.append(pygame.transform.flip(obj, False, True))
       # scale up
        for obj in self.face_L:
            self.face_L2.append(pygame.transform.scale(obj, [30, 30]))
        for obj in self.face_R:
            self.face_R2.append(pygame.transform.scale(obj, [30, 30]))
        for obj in self.face_UP:
            self.face_UP2.append(pygame.transform.scale(obj, [30, 30]))
        for obj in self.face_DN:
            self.face_DN2.append(pygame.transform.scale(obj, [30, 30]))
        
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
            frame = (self.rect.x//30) % len(self.face_R2)
            self.image = self.face_R2[frame]
        elif self.direction == "L":
            frame = (self.rect.x//30) % len(self.face_L2)
            self.image = self.face_L2[frame]
        elif self.direction == "UP":
            frame = (self.rect.y//30) % len(self.face_UP2)
            self.image = self.face_UP2[frame]
        else:
            frame = (self.rect.y//30) % len(self.face_DN2)
            self.image = self.face_DN2[frame]
        block_hit_list = pygame.sprite.spritecollide(self, Pore) #check self.pore
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.left




    def go_left(self):
        self.change_x = -2
        self.direction = "L"

    def go_right(self):
        self.change_x = 2
        self.direction = "R"
    
    def go_up(self):
        self.change_y = -2
        self.direction = "UP"

    def go_down(self):
        self.change_y = 2
        self.direction = "DOWN"

    def stop(self):
        self.change_x = 0
        self.change_y = 0

        

#Define class for obstacles/pores


def main():
    # Call this function so the Pygame library can initialize itself
    pygame.init()
    print("initalizing")

    #create screen
    screen = pygame.display.set_mode([640, 480])
 
    # Set the title of the window
    pygame.display.set_caption('python!')
    
    #create Pore object with Pore(x,y) x, y = position on screen
    block_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()
    print(f'#195 {block_list}, {type(block_list)}')
    temp_int = 1
    temp_int2 = 1
    for i in [1,2,3]:
        block = Pore(20, 20)
        
        print(f'int_start is {temp_int}')
        block.rect.x=random.randrange((20*(temp_int)), (170*(temp_int2)))
        print(f'block rect x {block.rect.x}')
        block.rect.y = random.randrange(-550, -300)
        print(f'block rect y {block.rect.y}')
        
        block.change_x = random.randrange(block.rect.x, 600, 80)
        print(f'x change {block.change_x}')
        block.left_boundary = 0
        block.top_boundary = 0
        block.right_boundary = 480
        block.bottom_boundary = 400

        block_list.add(block)


        #all_sprites_list.add(block)
        print(f'block_list {block_list}, all_sprite_list {all_sprites_list}')
        temp_int2 += 1
        temp_int += 5
        print(f'int2_end is {temp_int}')

    # Create the player object
    
    all_sprites_list = pygame.sprite.Group()
    #print(all_sprites_list)
    #all_sprites_list.add(block)
    player = Player(0, 200)
    all_sprites_list.add(player)
    print(f'added player to all_sprites: {all_sprites_list}')
    
    #pore_image = Pore(10, 20)


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

        #if pass through pore boundaries, add nt
 
    # --- Game logic
     
    # This calls update on all the sprites
        all_sprites_list.update()
 
    # -- Draw everything
    # background 
        screen.fill(WHITE)
 
    # Draw sprites
        
        block_list.draw(screen)
        all_sprites_list.draw(screen)
       # screen.blit(pore_image[0], [20,20])
 
    # Flip screen
        pygame.display.flip()
 
    # Pause
        clock.tick(60)
 
    pygame.quit()

if __name__ == '__main__':
    main()