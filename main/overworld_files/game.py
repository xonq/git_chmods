import pygame
import subprocess

import pygame.font
from pygame_functions import *
import config
from player import Player
from player import NPC
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
        Reed = NPC(5, 5, '/Users/student/PycharmProjects/pythonProject/git_chmods/main/overworld_files/images/Reed.png')
        self.Reed = Reed
        Simon = NPC(100, 100, '/Users/student/PycharmProjects/pythonProject/git_chmods/main/overworld_files/images/Simon.png')
        self.Simon = Simon
        sign = NPC(12, 10, '/Users/student/PycharmProjects/pythonProject/git_chmods/main/overworld_files/images/sign.png')
        self.sign = sign
        self.objects.append(player)
        self.objects.append(Reed)
        self.objects.append(Simon)
        self.objects.append(sign)
        print(self.objects)
        print('do set up')
        self.game_state = GameState.RUNNING

        # if player moves into a door space need to change overworld to sequencing_center or vice versa
        self.load_map('overworld')

    def update(self):

        self.screen.fill(config.WHITE)

        self.handle_events()

        self.render_map(self.screen)

        for object in self.objects:
            object.render(self.screen)

    def handle_events(self):

        # all NPCs and game object position info
        positions_dict = {'Reed': self.Reed.position,
                          'Simon': self.Simon.position,
                          'sign': self.sign.position
                          }

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED


            # handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.ENDED

                # up
                elif event.key == pygame.K_w:
                    self.move_unit(self.player, [0, -1], positions_dict)
                    new_position = [self.player.position[0] + 0, self.player.position[1] - 1]

                    if self.map[new_position[1]][new_position[0]] == "D":
                        if self.map[0][0] == "G":
                            next_room = 'sequencing_center'
                        if self.map[0][0] == "Z":
                            next_room = 'overworld'
                        self.map = []
                        self.load_map(next_room)
                        self.player.position = [9, 13]
                        self.player.update_position(self.player.position)
                        if next_room == 'sequencing_center':
                            self.Reed.position = [100, 100]
                            self.Reed.update_position(self.Reed.position)
                        if next_room == 'sequencing_center':
                            self.Simon.position = [9, 6]
                            self.Simon.update_position(self.Simon.position)
                        if next_room == 'sequencing_center':
                            self.sign.position = [100, 101]
                            self.sign.update_position(self.sign.position)


                # down
                elif event.key == pygame.K_s:
                    self.move_unit(self.player, [0, 1], positions_dict)
                    new_position = [self.player.position[0] + 0, self.player.position[1] + 1]

                    if new_position[1] == 15:
                        return

                    if self.map[new_position[1]][new_position[0]] == "D":
                        if self.map[0][0] == "G":
                            next_room = 'sequencing_center'
                        if self.map[0][0] == "Z":
                            next_room = 'overworld'
                        self.map = []
                        self.load_map(next_room)
                        self.player.position = [14, 10]
                        self.player.update_position(self.player.position)
                        if next_room == 'overworld':
                            self.Reed.position = [5, 5]
                            self.Reed.update_position(self.Reed.position)
                        if next_room == 'overworld':
                            self.Simon.position = [100, 100]
                            self.Simon.update_position(self.Simon.position)
                        if next_room == 'overworld':
                            self.Reed.position = [12, 10]
                            self.Reed.update_position(self.Reed.position)



                # left
                elif event.key == pygame.K_a:
                    self.move_unit(self.player, [-1, 0], positions_dict)


                # right
                elif event.key == pygame.K_d:
                    self.move_unit(self.player, [1, 0], positions_dict)

                # programming interaction dynamic
                elif event.key == pygame.K_k:
                    self.interact(self.player.position, positions_dict, self.screen)






    def load_map(self, file_name):
        with open ('/Users/student/PycharmProjects/pythonProject/git_chmods/main/overworld_files/maps/' + file_name + '.txt') as map_file:
            count = 0
            for line in map_file:
                tiles = []

                for i in range (0, len(line) - 1, 2):
                    tiles.append(line[i])

                self.map.append(tiles)




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

    def move_unit(self, unit, position_change, positions_dict):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]
        print(new_position)

        for game_object in positions_dict:
            if (positions_dict[game_object])[0] == new_position[0] and (positions_dict[game_object])[1] == new_position[1]:
                return

        if new_position[0] < 0 or new_position[0] > (len(self.map[0]) - 1):
            return

        if new_position[1] < 0 or new_position[1] > (len(self.map[1]) - 1):
            return

        if new_position[1] == 15:
            return

        if self.map[new_position[1]][new_position[0]] in {'G', 'Z'}:

            unit.update_position(new_position)

    def interact(self, player_position, positions_dict, screen):
        possible_interaction_positions = []
        temporary_position_list = []
        for position in positions_dict:
            temporary_position_list.append((positions_dict[position])[0])
            temporary_position_list.append((positions_dict[position])[1])
            possible_interaction_positions.append([temporary_position_list[0], temporary_position_list[1] + 1])
            possible_interaction_positions.append([temporary_position_list[0], temporary_position_list[1] - 1])
            possible_interaction_positions.append([temporary_position_list[0] + 1, temporary_position_list[1]])
            possible_interaction_positions.append([temporary_position_list[0] - 1, temporary_position_list[1]])
            temporary_position_list = []

        pygame.display.set_caption('genome game')

        if player_position in possible_interaction_positions:
            print('INTERACTION!')
            if positions_dict['Reed'][0] + 1 == player_position[0] or positions_dict['Reed'][0] - 1 == player_position[0] or positions_dict['Reed'][1] - 1 == player_position[1] or positions_dict['Reed'][1] + 1 == player_position[1]:
                print(Reed_text)
                pygame.display.set_caption(Reed_text)

        if player_position in possible_interaction_positions:
            print('INTERACTION!')
            if positions_dict['Simon'][0] + 1 == player_position[0] or positions_dict['Simon'][0] - 1 == player_position[0] or positions_dict['Simon'][1] - 1 == player_position[1] or positions_dict['Simon'][1] + 1 == player_position[1]:
                print(Simon_text)
                pygame.display.set_caption(Simon_text)

        if player_position in possible_interaction_positions:
            print('INTERACTION!')
            if positions_dict['sign'][0] + 1 == player_position[0] or positions_dict['sign'][0] - 1 == player_position[0] or positions_dict['sign'][1] - 1 == player_position[1] or positions_dict['sign'][1] + 1 == player_position[1]:
                print(sign_text)
                pygame.display.set_caption(sign_text)






                #subprocess.Popen('say -v Daniel "PAULY Im standing here!"', shell=True)


Reed_text = "Reed: PAULY, I'm standing here!"
Simon_text = "Simon: Welcome to our Sequencing Center!"
sign_text = "Sign: Simon and Sofia's Sequencing Center"




















map_tile_image = {
    'G': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/overworld_files/images/grass.png'), (config.SCALE, config.SCALE)),
    'L': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/overworld_files/images/topLeftPond.png'), (config.SCALE, config.SCALE)),
    'R': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/overworld_files/images/topRightPond.png'), (config.SCALE, config.SCALE)),
    'O': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/overworld_files/images/bottomLeftPond.png'), (config.SCALE, config.SCALE)),
    'P': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/overworld_files/images/bottomRightPond.png'), (config.SCALE, config.SCALE)),
    'N': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/overworld_files/images/bottomLeftWall.png'), (config.SCALE, config.SCALE)),
    'B': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/overworld_files/images/realBottomWall.png'), (config.SCALE, config.SCALE)),
    'D': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/overworld_files/images/door.png'), (config.SCALE, config.SCALE)),
    'M': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/overworld_files/images/bottomRightWall.png'), (config.SCALE, config.SCALE)),
    'l': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/overworld_files/images/leftWall.png'), (config.SCALE, config.SCALE)),
    'r': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/overworld_files/images/rightWall.png'), (config.SCALE, config.SCALE)),
    'W': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/overworld_files/images/wall.png'), (config.SCALE, config.SCALE)),
    'H': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/overworld_files/images/roof.png'), (config.SCALE, config.SCALE)),
    'S': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/overworld_files/images/sign.png'), (config.SCALE, config.SCALE)),
    'Z': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/overworld_files/images/sequencingCenterFloor.png'), (config.SCALE, config.SCALE)),

                  }
