import pygame
from unit import *
from pygame.locals import *
from messages import *
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
        
        m = message("Max Health: " + str(unit.getAttribute('Health')))
        SO.blit(m, (0, 128))
        m = message("Health: " + str(unit.currenthealth))
        SO.blit(m, (0, 140))
        m = message("Max Mana: " + str(unit.getAttribute('Mana')))
        SO.blit(m, (0, 152))
        m = message("Mana: " + str(unit.currentmana))
        SO.blit(m, (0, 164))
        m = message("Armor: " + str(unit.getAttribute('Armor')))
        SO.blit(m, (0, 176))
        m = message("MagR: " + str(unit.getAttribute('Magic Resist')))
        SO.blit(m, (0, 188))
        m = message("Speed: " + str(unit.getAttribute('Speed')))
        SO.blit(m, (0, 200))
        m = message("Range: " + str(unit.getAttribute('Range')))
        SO.blit(m, (0, 212))
        m = message("ArmorP: " + str(unit.getAttribute('Armorpen')))
        SO.blit(m, (0, 224))
        m = message("AttSpd: " + str(unit.getAttribute('Attack Speed')))
        SO.blit(m, (0, 236))
        m = message("Damage: " + str(unit.getAttribute('Damage')))
        SO.blit(m, (0, 248))
        m = message("MDamage: " + str(unit.getAttribute('Magic Damage')))
        SO.blit(m, (0, 260))
        m = message("Magicpen: " + str(unit.getAttribute('Magicpen')))
        SO.blit(m, (0, 272))
        
        body = unit.body
        
        if body.cloak != None:
            image = body.cloak.icon                
            SO.blit(table[image[0]][image[1]], (0*32, 0*32))
                          
        if body.body != None:
            image = body.body.icon                
            SO.blit(table[image[0]][image[1]], (1*32, 0*32))
            
        if body.head != None:
            image = body.head.icon                
            SO.blit(table[image[0]][image[1]], (2*32, 0*32))
            
        if body.legs != None:
            image = body.legs.icon                
            SO.blit(table[image[0]][image[1]], (3*32, 0*32))
            
        if body.boots != None:
            image = body.boots.icon                
            SO.blit(table[image[0]][image[1]], (0*32, 1*32))
        
        if body.torso != None:
            image = body.torso.icon                
            SO.blit(table[image[0]][image[1]], (1*32, 1*32))
            
        if body.hands != None:
            image = body.hands.icon                
            SO.blit(table[image[0]][image[1]], (2*32, 1*32))

        if body.righthand != None:
            image = body.righthand.icon                
            SO.blit(table[image[0]][image[1]], (3*32, 1*32))

        if body.lefthand != None:
            image = body.lefthand.icon                
            SO.blit(table[image[0]][image[1]], (0*32, 2*32))
            
        if body.leftring != None:
            image = body.leftring.icon                
            SO.blit(table[image[0]][image[1]], (1*32, 2*32))
            
        if body.rightring != None:
            image = body.rightring.icon                
            SO.blit(table[image[0]][image[1]], (2*32, 2*32))
            
        if body.amulet != None:
            image = body.amulet.icon                
            SO.blit(table[image[0]][image[1]], (3*32, 2*32))
        
    def draw(self, SO):
        SO.blit(self.surface, (512, 0))
    