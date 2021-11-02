import pygame
pygame.init()
import datetime
import logging
import ctypes


def find_bricks(filename):
    logging.debug("Starting Program")
    brickline = []
<<<<<<< HEAD
    row = 0
=======
    #row = 0;
>>>>>>> 2ef8218cd169612532022ce594afede367457a5e
    with open(filename, 'r') as f:
        for line in f:
            col = []
            for i in range(0, len(line)-1, 2):
                if line[i] + line[i+1] == "~~":
                    col.append(0)
                elif line[i] + line[i+1] == "1R":
                    col.append(11)
                elif line[i] + line[i+1] == "2R":
                    col.append(12)
                elif line[i] + line[i + 1] == "3R":
                    col.append(13)
            brickline.append(col)
    return brickline

<<<<<<< HEAD
=======


>>>>>>> 2ef8218cd169612532022ce594afede367457a5e
print (find_bricks('Levels/levelOne.txt'))
class Game:
    """ Initialize the game"""
    def __init__(self, game_width, game_height):
        pygame.display.set_caption('BrickBreaker')

        self.game_width = game_width
        self.game_height = game_height
        self.pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.bg = pygame.image.load('img/bricks.jpeg')
       # self.bricks = Bricks()
     #self.ball = Ball()
        self.score = 0
        self.level = 1
        self.timer = 0

#class Bricks(object):
    #def placebrick:
     #   for i


    #class Ball(object):
    #    def __init__(self, game, xpos, ypos):
    #        self.x_ball = xpos
     #       self.y_ball = ypos
     #       self.image=pygame.image.load('img/basketBall.png')


