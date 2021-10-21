import pygame
def define_parameters():

class Game:
    """ Initialize the game"""
    def __init__(self, game_width, game_height):
        pygame.display.set_caption('BrickBreaker')
        self.game_width = game_width
        self.game_height = game_height
        self.gameDisplay = pygame.display.set_mode((game_width, game_height))
        self.player = Player(self)
        self.bricks = Bricks()
        self.ball = Ball()
        self.score = 0

class Player(object):
class Bricks(object):
class Ball(object):
