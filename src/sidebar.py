import pygame
from unit import *
from pygame.locals import *
import math

class Sidebar:
    def __init__(self):
        self.surface = pygame.Surface((128, 512,))
        self.clear()
        
    def clear(self):
        self.surface.fill((30, 30, 30))
        
    def mouseEvent(self, event):      
        x, y =  event.pos
        x -= 512
        tile = (int(math.floor(x/32)), int(math.floor(y/32)))
        
        print "Sidebar", event.pos, tile[0], tile[1]
    
    def selectUnit(self, unit, table):
        self.clear()
        
        if unit == None:
            return
        
        SO = self.surface
        
        body = unit.body
        
        if body.cloak != None:
            image = body.cloak.icon                
            SO.blit(table[image[0]][image[1]], (0*32, 0*32))
                          
        if body.body != None:
            image = body.body.icon                
            SO.blit(table[image[0]][image[1]], (0*32, 1*32))
            
        if body.head != None:
            image = body.head.icon                
            SO.blit(table[image[0]][image[1]], (0*32, 2*32))
            
        if body.legs != None:
            image = body.legs.icon                
            SO.blit(table[image[0]][image[1]], (0*32, 3*32))
            
        if body.boots != None:
            image = body.boots.icon                
            SO.blit(table[image[0]][image[1]], (0*32, 4*32))
        
        if body.torso != None:
            image = body.torso.icon                
            SO.blit(table[image[0]][image[1]], (0*32, 5*32))
            
        if body.hands != None:
            image = body.hands.icon                
            SO.blit(table[image[0]][image[1]], (0*32, 6*32))

        if body.righthand != None:
            image = body.righthand.icon                
            SO.blit(table[image[0]][image[1]], (0*32, 7*32))

        if body.lefthand != None:
            image = body.lefthand.icon                
            SO.blit(table[image[0]][image[1]], (0*32, 8*32))
            
        if body.leftring != None:
            image = body.leftring.icon                
            SO.blit(table[image[0]][image[1]], (0*32, 9*32))
            
        if body.rightring != None:
            image = body.rightring.icon                
            SO.blit(table[image[0]][image[1]], (0*32, 10*32))
            
        if body.amulet != None:
            image = body.amulet.icon                
            SO.blit(table[image[0]][image[1]], (0*32, 11*32))
        
    def draw(self, SO):
        SO.blit(self.surface, (512, 0))
    