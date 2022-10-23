import pygame

import config
from player import Player
from game_state import GameState


class Game:

    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = GameState.NONE
        self.map = []



    def set_up(self):
        player = Player(1, 1)
        self.player = player
        self.objects.append(player)
        print(self.objects)
        print('do set up')
        self.game_state = GameState.RUNNING

        # if player moves into a door space need to change overworld to sequencing_center or vice versa
        self.load_map('overworld')

    def update(self):

        self.screen.fill(config.BLACK)

        self.handle_events()

        self.render_map(self.screen)

        for object in self.objects:
            object.render(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            # handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.ENDED
                # up
                elif event.key == pygame.K_w:
                    self.move_unit(self.player, [0, -1])
                    new_position = [self.player.position[0] + 0, self.player.position[1] - 1]

                    # need to change map with this if statement
                    #if self.map[new_position[1]][new_position[0]] == "D":




                # down
                elif event.key == pygame.K_s:
                    self.move_unit(self.player, [0, 1])

                # left
                elif event.key == pygame.K_a:
                    self.move_unit(self.player, [-1, 0])


                # right
                elif event.key == pygame.K_d:
                    self.move_unit(self.player, [1, 0])


                # try putting door check here somehow



    def load_map(self, file_name):
        with open ('maps/' + file_name + '.txt') as map_file:
            count = 0
            for line in map_file:
                tiles = []

                for i in range (0, len(line) - 1, 2):
                    tiles.append(line[i])

                self.map.append(tiles)

            print(self.map)


    def render_map(self, screen):
        y_position = 0
        for line in self.map:
            x_position = 0
            for tile in line:

                image = map_tile_image[tile]
                rect = pygame.Rect(x_position * config.SCALE, y_position * config.SCALE, config.SCALE, config.SCALE)
                screen.blit(image, rect)
                x_position += 1
            y_position += 1

    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]
        print(new_position)

        if new_position[0] < 0 or new_position[0] > (len(self.map[0]) - 1):
            return

        if new_position[1] < 0 or new_position[1] > (len(self.map[1]) - 1):
            return

        if new_position[1] == 15:
            return

        if self.map[new_position[1]][new_position[0]] == "G":

            unit.update_position(new_position)

        #if self.map[new_position[1]][new_position[0]] == "D":
            #load_map('sequencing_center')
















map_tile_image = {
    'G': pygame.transform.scale(pygame.image.load('images/grass.png'), (config.SCALE, config.SCALE)),
    'L': pygame.transform.scale(pygame.image.load('images/topLeftPond.png'), (config.SCALE, config.SCALE)),
    'R': pygame.transform.scale(pygame.image.load('images/topRightPond.png'), (config.SCALE, config.SCALE)),
    'O': pygame.transform.scale(pygame.image.load('images/bottomLeftPond.png'), (config.SCALE, config.SCALE)),
    'P': pygame.transform.scale(pygame.image.load('images/bottomRightPond.png'), (config.SCALE, config.SCALE)),
    'N': pygame.transform.scale(pygame.image.load('images/bottomLeftWall.png'), (config.SCALE, config.SCALE)),
    'B': pygame.transform.scale(pygame.image.load('images/realBottomWall.png'), (config.SCALE, config.SCALE)),
    'D': pygame.transform.scale(pygame.image.load('images/door.png'), (config.SCALE, config.SCALE)),
    'M': pygame.transform.scale(pygame.image.load('images/bottomRightWall.png'), (config.SCALE, config.SCALE)),
    'l': pygame.transform.scale(pygame.image.load('images/leftWall.png'), (config.SCALE, config.SCALE)),
    'r': pygame.transform.scale(pygame.image.load('images/rightWall.png'), (config.SCALE, config.SCALE)),
    'W': pygame.transform.scale(pygame.image.load('images/wall.png'), (config.SCALE, config.SCALE)),
    'H': pygame.transform.scale(pygame.image.load('images/roof.png'), (config.SCALE, config.SCALE)),
    'S': pygame.transform.scale(pygame.image.load('images/sign.png'), (config.SCALE, config.SCALE)),


                  }
