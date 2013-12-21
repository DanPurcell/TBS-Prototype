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
            if event.key == K_c:
                game.castSpell(wSO)
            if event.key == K_s:
                if game.selected != None:
                    game.selected.nextSpell()
            if event.key == K_g:
                game = Game(2, 6)
            if event.key == K_m:
                game.Menu()
                
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            game.mouseEvent(event, wSO)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            game.mouseEvent(event, wSO)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            game.mouseEvent(event, wSO)
            print "right down"
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            print "up down"
            game.mouseEvent(event, wSO)
    
    pygame.display.update()
    fpsClock.tick(30)
    
