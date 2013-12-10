import pygame, sys
from pygame.locals import *
from body import *
from unit import *
from items import *
from world import *
from game import *
from player import *

pygame.init()
fpsClock = pygame.time.Clock()

wSO = pygame.display.set_mode((640, 544))
pygame.display.set_caption('Yo!')
                                     
game = Game(2, 6)
    
while True:
    wSO.fill((0,0,0))
    game.draw(wSO)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_q:
                pygame.quit()
                sys.exit()
                
            if event.key == K_n:
                game.nextUnit()
            if event.key == K_w:
                game.wait()
            if event.key == K_g:
                game = game = Game(2, 6)
                
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            game.mouseEvent(event)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            game.mouseEvent(event)
    
    pygame.display.update()
    fpsClock.tick(30)
    
