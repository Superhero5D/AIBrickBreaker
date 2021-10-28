import pygame
import datetime
import logging

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
def find_bricks(filename):
    logging.debug("Starting Program")
    brickline = []
    row = 0;
    with open(filename, 'r') as f:
        for line in f:
            col = []
            for i in range(0, len(line)-1, 2):
                if line[i] + line[i+1] == "~~":
                    col[i] = 0
                brickline[row] += col[i]
    return brickline




print (find_bricks('Levels/levelOne.txt'))
class Game:
    """ Initialize the game"""
    def __init__(self, game_width, game_height):
        pygame.display.set_caption('BrickBreaker')

        self.game_width = game_width
        self.game_height = game_height
        self.gameDisplay = pygame.display.set_mode((game_width, game_height))
        self.bg = pygame.image.load('img/bricks.jpeg')
        self.player = Player(self)
       # self.bricks = Bricks()
     #   self.ball = Ball()
        self.score = 0
        self.level = 1
        self.timer = 0


class Player(object):
    def __init__(self, game):
        x = 0.45 * game.game_width
        y = 0.1 * game.game_height

   # class Bricks(object):
     #   def __init__(self):

        #def levels(self):


    #class Ball(object):
    #    def __init__(self, game, xpos, ypos):
    #        self.x_ball = xpos
     #       self.y_ball = ypos
     #       self.image=pygame.image.load('img/basketBall.png')


