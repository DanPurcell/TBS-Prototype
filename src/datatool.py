import pygame, sys
from pygame.locals import *

import random

import tiletable as tt

pygame.init()
fpsClock = pygame.time.Clock()

wSO = pygame.display.set_mode((512, 512))
pygame.display.set_caption('Yo!')

font = pygame.font.Font('freesansbold.ttf', 10)

class Datatool:
    def __init__(self):
        self.table = tt.load_tile_table("tiles.png", 32, 32)
        self.tile = (0, 0)
        self.tiles = [x[:] for x in [[None]*len(self.table)]*len(self.table[0])]
        self.index = 0
        self.data = [x[:] for x in [[[]]*len(self.table)]*len(self.table[0])]
        
    def draw(self, SO):
        SO.blit(self.table[self.tile[0]][self.tile[1]], (0, 0))

    def nexttile(self):
        x = len(self.table) - 1
        y = len(self.table[0]) - 1

        self.tile = (random.randint(0, x), random.randint(0, y))

datatool = Datatool()

while True:
    wSO.fill((0,0,0))

    datatool.draw(wSO)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_q:
                pygame.quit()
                sys.exit()

            if event.key == K_n:
                datatool.nexttile()
    
    pygame.display.update()
    fpsClock.tick(30)
