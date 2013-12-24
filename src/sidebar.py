import pygame
from unit import *
from pygame.locals import *
from messages import *
import math

class Sidebar:
    def __init__(self):
        self.surface = pygame.Surface((128, 512,))
        self.clear()
        self.unit = None
        
    def clear(self):
        self.surface.fill((30, 30, 30))
        
    def mouseEvent(self, event):      
        x, y =  event.pos
        x -= 512
        tile = (int(math.floor(x/32)), int(math.floor(y/32)))
            
    def selectUnit(self, unit, table):
        self.unit = unit        
        
    def drawInventory(self, table):
        self.clear()
        
        unit = self.unit
        
        if unit == None:
            return
        
        SO = self.surface
        
        total = unit.getAttribute('Health') + unit.getAttribute('Armor') + unit.getAttribute('Magic') + unit.getAttribute('Magic Resist')
               
        maxhealth  = (unit.getAttribute('Health')/total) * 128.0
        health = (unit.currenthealth/unit.getAttribute('Health')) * maxhealth
        armor = (unit.getAttribute('Armor')/total) * 128.0
        magicr = (unit.getAttribute('Magic Resist')/total) * 128.0
        
        hregen = (unit.getAttribute('Health Regen')/total) * 128.0
       
        pygame.draw.line(SO, (100, 0, 0), (0, 128), (maxhealth, 128), 12)
                
        pygame.draw.line(SO, (200, 0, 0), (0, 128), (health, 128), 12)
        if armor > 0.0:
            pygame.draw.line(SO, (200, 200, 200), (128, 128), (128 - armor, 128), 12)
        if magicr > 0.0:
            pygame.draw.line(SO, (200, 100, 0), (128 - armor, 128), (128 - armor - magicr, 128), 12)
        if hregen > 0.0:
            pygame.draw.line(SO, (255, 0, 0), (0, 128), (hregen, 128), 12)
            
        h = unit.getAttribute('Health')
        t = h
        while t > 0.0:
            d = (t/h)*maxhealth
            pygame.draw.line(SO, (80, 0, 0), (d,123) ,(d,140), 1)
            t -= 10.0

        mmana = unit.getAttribute('Mana')    
        cmana = (unit.currentmana/mmana) * 128.0
        mregen = (unit.getAttribute('Mana Regen')/mmana) * 128.0
        pygame.draw.line(SO, (0, 0, 100), (0, 140), (128, 140), 12)
        pygame.draw.line(SO, (0, 0, 200), (0, 140), (cmana, 140), 12)
        
        if (mregen > 0.0) & (mregen <= cmana):
            pygame.draw.line(SO, (0, 0, 255), (0, 140), (mregen, 140), 12)    
            
        m = unit.getAttribute('Mana')
        t = m
        while t > 0.0:
            d = (t/m)*128.0
            pygame.draw.line(SO, (0, 0, 80), (128 - d,135) ,(128 - d,148), 1)
            t -= 10.0  
        
        
        a = "%0.1f" % unit.getAttribute('Damage')  
        b = "%0.1f" % unit.getAttribute('Armorpen')  
        m = message(str(a) + " : " + str(b), (255,0,0))
        SO.blit(m, (4, 150))
        
        a = "%0.1f" % unit.getAttribute('Magic Damage')  
        b = "%0.1f" % unit.getAttribute('Magicpen')
        m = message(str(a) + " : " + str(b), (50,50,255))
        SO.blit(m, (4, 162))
        
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
            r = body.righthand.getAttribute("Range")
            if r > 0.0:
                rt = body.getAttribute("Range")
                c = (0, 0, 0)
                if rt > r:
                    c = (0,200,0)
                else:
                    c = (255,255,255)
                rt = "%0.1f" % rt
                m = message(str(rt), c)
                
                SO.blit(m, (3*32, 1*32))

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
        
    def mouseover(self, SO):
        mp = pygame.mouse.get_pos()
        
        if mp[0] < 512:
            return
        
        if self.unit == None:
            return
        
        p = ((mp[0] - 512)/32, mp[1]/32)
        
        body = self.unit.body
        
        slots = ((body.cloak, (0, 0)),
                (body.body, (1, 0)),
                (body.head, (2, 0)),
                (body.legs, (3, 0)),
                (body.boots, (0, 1)),
                (body.torso, (1, 1)),
                (body.hands, (2, 1)),
                (body.righthand, (3, 1)),
                (body.lefthand, (0, 2)),
                (body.leftring, (1, 2)),
                (body.rightring, (2, 2)),
                (body.amulet, (3, 2)))
        
        for i in slots:     
            if i[0] == None:
                continue
                 
            if p == i[1]:
                m = message(i[0].name, (255,255,255))
                
                pos = (mp[0] - m.get_width(), mp[1] + 16)
                SO.blit(m, pos)
                
                nudge = 12
                
                for s in i[0].stats.iteritems():
                    m = message(s[0] + ": " + str(s[1]), (255,255,255))
                    SO.blit(m, (pos[0],pos[1]+nudge))
                    nudge += 12
                
                return
        
    def draw(self, SO, table):
        self.drawInventory(table)
        SO.blit(self.surface, (512, 0))
        self.mouseover(SO)
    