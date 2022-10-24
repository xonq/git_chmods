#!/usr/bin/env python3
import pygame
import random



class SpriteSheet(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()
    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert_alpha()
        image.blit(self.sprite_sheet, (0,0), (x, y, width, height))
        return image


class Pore_up(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        #make a list to hold your two sprite block
        self.pore_up = []

        sprite_sheet = SpriteSheet('pore_sprite.png')
        print(f'fetching nanopores from {sprite_sheet}')
        image = pygame.transform.scale(sprite_sheet.get_image(0, 0, 46, 375), [50, 1500])
        self.pore_up.append(image)
        #initiate pore position
        self.image = self.pore_up[0]
        
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
        print(self.pore_up)

class Pore_down(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        #make a list to hold your two sprite block
        self.pore_down = []

        sprite_sheet = SpriteSheet('pore_sprite.png')
        print(f'fetching nanopores from {sprite_sheet}')
        image = pygame.transform.scale(sprite_sheet.get_image(0, 0, 46, 375), [50, 1500])
        self.pore_down.append(pygame.transform.rotate(image, -180))
        #initiate pore position
        self.image = self.pore_down[0]
        
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
        print(self.pore_down)


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
        self.trail = set()

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
            self.face_L2.append(pygame.transform.scale(obj, [50, 50]))
        for obj in self.face_R:
            self.face_R2.append(pygame.transform.scale(obj, [50, 50]))
        for obj in self.face_UP:
            self.face_UP2.append(pygame.transform.scale(obj, [50, 50]))
        for obj in self.face_DN:
            self.face_DN2.append(pygame.transform.scale(obj, [50, 50]))
        
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        WHITE = (255, 255, 255)
        green= (124, 252, 0)

    
    #for each change in position, change:    
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
        #keep on screen
        
        pos = self.rect.center
        print(pos)
        if self.trail:
            if self.trail[-1] != pos:
                self.trail.append(pos)
        else:
            self.trail = [pos, pos]
        print(self.trail)

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
        
        #sprite coordinates
#        self.sprite_coord_list = []
#        self.sprite_coord = ()
 #       self.sprite_coord = (self.rect.x, self.rect.y)
  #      self.sprite_coord_list.append(self.sprite_coord)
   #     print(f'coordinates are {self.sprite_coord_list}')


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

LEFT, CENTER, RIGHT = range(3)
TOP, MIDDLE, BOTTOM = range(3)

#Define class for dna trail
class Trail(pygame.sprite.Sprite):
    def __init__(self, screen, text='text', pos=(0, 0), pos_rel=(LEFT, TOP),
                 font=None, size=20, color=(0, 0, 0), antialias=True):
        
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(font, size)
        
        self.color = color
        self.text = text
        self.pos = pos
        self.pos_rel = pos_rel
        self.screen = screen
        self.antialias = antialias

        self.rerender()


    def update(self):
        pass

    def calculate_position(self):
        return (
            self.pos_rel[0]*(self.screen.get_size()[0]/2 - self.rect.width/2)
            + (1-2*(self.pos_rel[0]/2))*self.pos[0],
            self.pos_rel[1]*(self.screen.get_size()[1]/2 - self.rect.height/2)
            + (1-2*(self.pos_rel[1]/2))*self.pos[1],
            )

    def print_text(self, text, pos=None):
        self.text = text
        if pos:
            self.pos = pos
        self.rerender()

    def rerender(self):
        self.image = self.font.render(self.text, self.antialias, self.color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.calculate_position()

def main():
    # Call this function so the Pygame library can initialize itself
    pygame.init()
    print("initalizing")

    WHITE = (255, 255, 255)
    green= (124, 252, 0)
    width=640 
    height=480
    #create screen
    screen = pygame.display.set_mode([width, height])
 
    # Set the title of the window
    pygame.display.set_caption('python!')
    background_image = pygame.image.load("landscape.png").convert_alpha()
    background_image.set_alpha(10)
    
    
    #create Pore object with Pore(x,y) x, y = position on screen
    block_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()
    list_x_coords = []
    print(f'#195 {block_list}, {type(block_list)}')
    temp_int = 20
    temp_int2 = 200
    for i in [1,2]:
        #define top block
        block_up = Pore_up(20, 20)

        #give x a random position 
        block_up.rect.x=random.randrange(temp_int, temp_int2)
        
        #capture x coord
        x_coord = block_up.rect.x
        print(f'x = {x_coord}')

        #define y coord
        block_up.rect.y = random.randrange(-1300, -1100)
        y_coord = block_up.rect.y
        print(f'y ={y_coord}')

        block_down = Pore_down(20, 20)
        block_down.rect.x = x_coord
        block_down.rect.y = (y_coord+1300)
        print(f'block_down.rect.y is {block_down.rect.y}')
       
        block_up.change_x = 300

        #whole_pore.left_boundary = 0
        #whole_pore.top_boundary = 0
        #whole_pore.right_boundary = 480
        #whole_pore.bottom_boundary = 400

        #add to coordinate list
        list_x_coords.append(x_coord)

        block_list.add(block_up)
        block_list.add(block_down)
        all_sprites_list.add(block_up)
        all_sprites_list.add(block_down)
        
        #all_sprites_list.add(block)
        temp_int *= 10
        temp_int2 *= 3.1
        print(f'int_end is {temp_int}')

    # Create the player object
    
    all_sprites_list = pygame.sprite.Group()
    player = Player(0, 200)
    all_sprites_list.add(player)
    print(f'added player to all_sprites: {all_sprites_list}')

    #DNA object
    
    nt_seq_list = pygame.sprite.Group()
    nt_load = ['ATG', 'GGC', 'GCA', 'TTA']
    for nt in nt_load:
        nt_trail = Trail(screen, nt) #figure out how to put in player.trail -1 as coordinates
        nt_seq_list.add(nt_trail)
        print(nt_seq_list)


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
            
            

            collisions = pygame.sprite.spritecollide(player, block_list, True)
            if collisions:
                print('oh no')
                return
 
    # --- Game logic
     
    # This calls update on all the sprites
        all_sprites_list.update()
 
    # -- Draw everything
    
    # Draw sprites
        
        all_sprites_list.draw(screen)
        block_list.draw(screen)
        #nt_seq_list.draw(screen)
        #pygame.draw.lines(screen, (RBG), False, player.trail)
        screen.blit(background_image, [0,0])
        
 
    # Flip screen
        pygame.display.flip()
 
    # Pause
        clock.tick(30)
 
    pygame.quit()

if __name__ == '__main__':
    main()