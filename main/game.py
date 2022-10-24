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
        Reed = NPC(5, 5, '/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/Reed.png')
        self.Reed = Reed
        Simon = NPC(100, 100, '/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/Simon.png')
        self.Simon = Simon
        sign = NPC(12, 10, '/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/sign.png')
        self.sign = sign
        Zach = NPC(1, 13, '/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/Zach.png')
        self.Zach = Zach
        mushroom = NPC(2, 13, '/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/mushroom.png')
        self.mushroom = mushroom
        Sofia = NPC(100, 102, '/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/Sofia.png')
        self.Sofia = Sofia
        Snake = NPC(105, 105, '/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/overworld_snake.png')
        self.Snake = Snake
        computer = NPC(200, 200, '/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/computer.png')
        self.computer = computer
        arch = NPC(17, 0, '/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/arch.png')
        self.arch = arch
        self.objects.append(player)
        self.objects.append(Reed)
        self.objects.append(Simon)
        self.objects.append(sign)
        self.objects.append(Zach)
        self.objects.append(mushroom)
        self.objects.append(Sofia)
        self.objects.append(Snake)
        self.objects.append(computer)
        self.objects.append(arch)
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
                          'sign': self.sign.position,
                          'Zach': self.Zach.position,
                          'mushroom': self.mushroom.position,
                          'Sofia': self.Sofia.position,
                          'Snake': self.Snake.position,
                          'computer': self.computer.position,
                          'arch': self.arch.position
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
                            self.Simon.position = [18, 13]
                            self.Simon.update_position(self.Simon.position)
                        if next_room == 'sequencing_center':
                            self.sign.position = [100, 101]
                            self.sign.update_position(self.sign.position)
                        if next_room == 'sequencing_center':
                            self.Zach.position = [100, 101]
                            self.Zach.update_position(self.Zach.position)
                        if next_room == 'sequencing_center':
                            self.mushroom.position = [100, 101]
                            self.mushroom.update_position(self.mushroom.position)
                        if next_room == 'sequencing_center':
                            self.Sofia.position = [11, 7]
                            self.Sofia.update_position(self.Sofia.position)
                        if next_room == 'sequencing_center':
                            self.Snake.position = [1, 1]
                            self.Snake.update_position(self.Snake.position)
                        if next_room == 'sequencing_center':
                            self.computer.position = [3, 10]
                            self.computer.update_position(self.computer.position)
                        if next_room == 'sequencing_center':
                            self.arch.position = [300, 300]
                            self.arch.update_position(self.arch.position)


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
                            self.sign.position = [12, 10]
                            self.sign.update_position(self.sign.position)
                        if next_room == 'overworld':
                            self.Zach.position = [1, 13]
                            self.Zach.update_position(self.Zach.position)
                        if next_room == 'overworld':
                            self.mushroom.position = [2, 13]
                            self.mushroom.update_position(self.mushroom.position)
                        if next_room == 'overworld':
                            self.Sofia.position = [101, 103]
                            self.Sofia.update_position(self.Sofia.position)
                        if next_room == 'overworld':
                            self.Snake.position = [101, 105]
                            self.Snake.update_position(self.Snake.position)
                        if next_room == 'overworld':
                            self.computer.position = [102, 105]
                            self.computer.update_position(self.computer.position)
                        if next_room == 'overworld':
                            self.arch.position = [17, 0]
                            self.arch.update_position(self.arch.position)




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
        with open ('/Users/student/PycharmProjects/pythonProject/git_chmods/main/maps/' + file_name + '.txt') as map_file:
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

        if player_position in possible_interaction_positions:
            print('INTERACTION!')
            if positions_dict['Zach'][0] + 1 == player_position[0] or positions_dict['Zach'][0] - 1 == player_position[0] or positions_dict['Zach'][1] - 1 == player_position[1] or positions_dict['Zach'][1] + 1 == player_position[1]:
                print(Zach_text)
                pygame.display.set_caption(Zach_text)

        if player_position in possible_interaction_positions:
            print('INTERACTION!')
            if positions_dict['mushroom'][0] + 1 == player_position[0] or positions_dict['mushroom'][0] - 1 == player_position[0] or positions_dict['mushroom'][1] - 1 == player_position[1] or positions_dict['mushroom'][1] + 1 == player_position[1]:
                print(mushroom_text)
                pygame.display.set_caption(mushroom_text)

        if player_position in possible_interaction_positions:
            print('INTERACTION!')
            if positions_dict['Sofia'][0] + 1 == player_position[0] or positions_dict['Sofia'][0] - 1 == player_position[0] or positions_dict['Sofia'][1] - 1 == player_position[1] or positions_dict['Sofia'][1] + 1 == player_position[1]:
                print(Sofia_text)
                pygame.display.set_caption(Sofia_text)

        if player_position in possible_interaction_positions:
            print('INTERACTION!')
            if positions_dict['Snake'][0] + 1 == player_position[0] or positions_dict['Snake'][0] - 1 == player_position[0] or positions_dict['Snake'][1] - 1 == player_position[1] or positions_dict['Snake'][1] + 1 == player_position[1]:
                print(Snake_text)
                pygame.display.set_caption(Snake_text)

        if player_position in possible_interaction_positions:
            print('INTERACTION!')
            if positions_dict['computer'][0] + 1 == player_position[0] or positions_dict['computer'][0] - 1 == player_position[0] or positions_dict['computer'][1] - 1 == player_position[1] or positions_dict['computer'][1] + 1 == player_position[1]:
                print(computer_text)
                pygame.display.set_caption(computer_text)

        if player_position in possible_interaction_positions:
            print('INTERACTION!')
            if positions_dict['arch'][0] + 1 == player_position[0] or positions_dict['arch'][0] - 1 == player_position[0] or positions_dict['arch'][1] - 1 == player_position[1] or positions_dict['arch'][1] + 1 == player_position[1]:
                print(arch_text)
                pygame.display.set_caption(arch_text)






                #subprocess.Popen('say -v Daniel "PAULY Im standing here!"', shell=True)


Reed_text = "Reed: PAULY, I'm standing here!"
Simon_text = "Simon: Welcome to our Sequencing Center!"
sign_text = "Simon and Sofia's Sequencing Center"
Zach_text = "Zach: Dude, check out this mushroom. Its biosynthetic gene clusters probably coevolved..."
mushroom_text = "mushroom: First, you should probably collect a DNA sample"
Sofia_text = "Sofia: If you have a sequencing sample, you should run it in the Nanopore! Talk to the snake"
Snake_text = "snake: Hey if you have a sequencing sample I'll run it, dude. Press K again and I'll do it!"
computer_text = "computer: Hello, organic user. If you press K again, you can try to assemble your reads."
arch_text = "arch: Yo go through me and you might get some hecking DNA. Press K to enter."
















map_tile_image = {
    'G': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/grass.png'), (config.SCALE, config.SCALE)),
    'L': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/topLeftPond.png'), (
    config.SCALE, config.SCALE)),
    'R': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/topRightPond.png'), (
    config.SCALE, config.SCALE)),
    'O': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/bottomLeftPond.png'), (
    config.SCALE, config.SCALE)),
    'P': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/bottomRightPond.png'), (
    config.SCALE, config.SCALE)),
    'N': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/bottomLeftWall.png'), (
    config.SCALE, config.SCALE)),
    'B': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/realBottomWall.png'), (
    config.SCALE, config.SCALE)),
    'D': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/door.png'), (config.SCALE, config.SCALE)),
    'M': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/bottomRightWall.png'), (
    config.SCALE, config.SCALE)),
    'l': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/leftWall.png'), (config.SCALE, config.SCALE)),
    'r': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/rightWall.png'), (
    config.SCALE, config.SCALE)),
    'W': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/wall.png'), (config.SCALE, config.SCALE)),
    'H': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/roof.png'), (config.SCALE, config.SCALE)),
    'S': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/sign.png'), (config.SCALE, config.SCALE)),
    'Z': pygame.transform.scale(pygame.image.load('/Users/student/PycharmProjects/pythonProject/git_chmods/main/images/sequencingCenterFloor.png'), (
    config.SCALE, config.SCALE)),

                  }
