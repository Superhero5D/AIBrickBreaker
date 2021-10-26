import pygame
import datetime


def define_parameters():
    def define_parameters():
        params = dict()
        # Neural Network
        params['epsilon_decay_linear'] = 1 / 100
        params['learning_rate'] = 0.00013629
        params['first_layer_size'] = 200  # neurons in the first layer
        params['second_layer_size'] = 20  # neurons in the second layer
        params['third_layer_size'] = 50  # neurons in the third layer
        params['episodes'] = 250
        params['memory_size'] = 2500
        params['batch_size'] = 1000
        # Settings
        params['weights_path'] = 'weights/weights.h5'
        params['train'] = False
        params["test"] = True
        params['plot_score'] = True
        params['log_path'] = 'logs/scores_' + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")) + '.txt'
        return params

class Game:
    """ Initialize the game"""
    def __init__(self, game_width, game_height):
        pygame.display.set_caption('BrickBreaker')

        self.game_width = game_width
        self.game_height = game_height
        self.gameDisplay = pygame.display.set_mode((game_width, game_height))
        self.bg = pygame.image.load('img/bricks.jpeg')
        self.player = Player(self)
        self.bricks = Bricks()
        self.ball = Ball()
        self.score = 0
        self.level = 1
        self.timer = 0


class Player(object):
    def __init__(self, game):
        x = 0.45 * game.game_width
        y = 0.1 * game.game_height

    class Bricks(object):
        def __init__(self, game, xpos, ypos):
            self.x_brick = xpos
            self.y_brick = ypos
            self.image=pygame.image.load('')

    class Ball(object):
        def __init__(self, game, xpos, ypos):
            self.x_ball = xpos
            self.y_ball = ypos
            self.image=pygame.image.load('img/basketBall.png')

