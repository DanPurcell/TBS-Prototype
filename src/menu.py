import pygame, sys
from pygame.locals import *
from items import *
from messages import *

class Menu:
    def __init__(self, unit=None):
        self.unit = unit
        if self.unit != None:
            print type(unit)
        
        self.slots = {'Cloak':cloaks,
                      'Body':bodies,
                      'Head':head,
                      'Legs':legs,
                      'Boots':boots,
                      'Torso':torso,
                      'Hands':hands,
                      'Right Hand':righthand,
                      'Left Hand':lefthand,
                      'Right Ring':rings,
                      'Left Ring':rings,
                      'Amulet':amulets}
        
        
    def itemAt(self, p):
        slots = self.slots
        
        x, y = 0, 0
        
        for slot in slots.values():
            for item in slot:
                if p == (x, y):                       
                    return item                    
                x += 1
                    
            x = 0
            y += 1
            
        return None           
        
    def mouseover(self, SO):
        mp = pygame.mouse.get_pos()

        p = ((mp[0])/32, mp[1]/32)
        
        item = self.itemAt(p)
        
        if item == None:
            return
        
        m = message(item.name, (255,255,255))
                
        pos = (mp[0] + 16, mp[1] + 16)
        SO.blit(m, pos)
            
        nudge = 12
            
        for s in item.stats.iteritems():
            m = message(s[0] + ":" + str(s[1]), (255,255,255))
            SO.blit(m, (pos[0],pos[1]+nudge))
            nudge += 12                             
                     
    
    def mouseEvent(self, event, SO):
        print "Menu Mouse Event"
    
    def highlightEquipped(self, SO):
        #TODO
        return
    
    def draw(self, SO, table):    
        x, y = 0, 0

        for slot in self.slots.values():
            for item in slot:
                image = item.icon
                SO.blit(table[image[0]][image[1]], (x*32, y*32))
                
                x += 1
            y += 1
            x = 0
        
        self.highlightEquipped(SO)    
        self.mouseover(SO)
            