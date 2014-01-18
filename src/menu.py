import pygame, sys
from pygame.locals import *
from items import *
from messages import *

class Menu:
    def __init__(self, unit=None):
        self.unit = unit
                
        self.slots = (cloaks,
                      bodies,
                      head,
                      legs,
                      boots,
                      torso,
                      hands,
                      righthand,
                      lefthand,
                      rings,
                      rings,
                      amulets)
                
    def itemAt(self, p):
        slots = self.slots
        
        x, y = 0, 0
        
        for slot in slots:
            for item in slot:
                if p == (x, y):                       
                    return item                    
                x += 1
                    
            x = 0
            y += 1
            
        return NoItem           
        
    def mouseover(self, SO):
        mp = pygame.mouse.get_pos()

        p = ((mp[0])/32, mp[1]/32)
        
        item = self.itemAt(p)
        
        if item == NoItem:
            return
        
        m = message(item.name, (255,255,255))
                
        pos = (mp[0] + 16, mp[1] + 16)
        SO.blit(m, pos)
            
        nudge = 12
            
        for s in item.stats.iteritems():
            m = message(s[0] + ": " + str(s[1]), (255,255,255))
            SO.blit(m, (pos[0],pos[1]+nudge))
            nudge += 12                             
                     
    
    def mouseEvent(self, event, SO):
        pos = (event.pos[0]/32, event.pos[1]/32)
        
        if pos == (16,0):
            name = raw_input("Name: ")
            self.unit.body.save(name)
            return
        if pos == (17,0):
            name = raw_input("Name: ")
            self.unit.body.load(name)
            return
        
        item = self.itemAt(pos)
        
        if item == NoItem:
            return
        
        body = self.unit.body
        
        if pos[1] == 0:
            body.cloak = item     
            
        if pos[1] == 1:
            body.body = item         
            
        if pos[1] == 2:
            body.head = item

        if pos[1] == 3:
            body.legs = item

        if pos[1] == 4:
            body.boots = item

        if pos[1] == 5:
            body.torso = item

        if pos[1] == 6:
            body.hands = item

        if pos[1] == 7:
            body.righthand = item
                
        if pos[1] == 8:
            body.lefthand = item

        if pos[1] == 9:
            body.leftring = item
            
        if pos[1] == 10:
            body.rightring = item
            
        if pos[1] == 11:
            body.amulet = item
            
        if body.lefthand.name.find("Book") != -1:
            body.righthand = nullspell
            
        if body.righthand.name.find("Bow") != -1:
            body.lefthand = NoItem
            
        self.unit.body = body
        
        if self.unit.body.lefthand != None:
            if self.unit.body.lefthand.name.find("Book") > 0:
                self.unit.spellbook = spellbooks[self.unit.body.lefthand.name]
                self.unit.memorised = self.unit.spellbook.spells[0]  
                self.unit.body.righthand = self.unit.memorised
            else:
                self.unit.memorised = None

    
    def highlightEquipped(self, SO):
        h = pygame.Surface((32,32))
        h.set_alpha(50)
        h.fill((255,255,0))
        
        x, y = 0, 0
        
        body = self.unit.body
        
        for i in self.slots[0]:
            if body.cloak == i:
                SO.blit(h, (x*32, y*32))
            x += 1
        
        y += 1
        x = 0
            
        for i in self.slots[1]:
            if body.body == i:
                SO.blit(h, (x*32, y*32))
            x += 1
        
        y += 1
        x = 0
            
        for i in self.slots[2]:
            if body.head == i:
                SO.blit(h, (x*32, y*32))
            x += 1
        
        y += 1
        x = 0
            
        for i in self.slots[3]:
            if body.legs == i:
                SO.blit(h, (x*32, y*32))
            x += 1
        
        y += 1
        x = 0
        
        for i in self.slots[4]:
            if body.boots == i:
                SO.blit(h, (x*32, y*32))
            x += 1
        
        y += 1
        x = 0
            
        for i in self.slots[5]:
            if body.torso == i:
                SO.blit(h, (x*32, y*32))
            x += 1
        
        y += 1
        x = 0
            
        for i in self.slots[6]:
            if body.hands == i:
                SO.blit(h, (x*32, y*32))
            x += 1
        
        y += 1
        x = 0
            
        for i in self.slots[7]:
            if body.righthand == i:
                SO.blit(h, (x*32, y*32))
            x += 1
        
        y += 1
        x = 0
            
        for i in self.slots[8]:
            if body.lefthand == i:
                SO.blit(h, (x*32, y*32))
            x += 1
        
        y += 1
        x = 0
            
        for i in self.slots[9]:
            if body.leftring == i:
                SO.blit(h, (x*32, y*32))
            x += 1
        
        y += 1
        x = 0
            
        for i in self.slots[10]:
            if body.rightring == i:
                SO.blit(h, (x*32, y*32))
            x += 1
        
        y += 1
        x = 0
            
        for i in self.slots[11]:
            if body.amulet == i:
                SO.blit(h, (x*32, y*32))
            x += 1
            
        return
    
    def draw(self, SO, table):    
        x, y = 0, 0

        for slot in self.slots:
            for item in slot:
                image = item.icon
                SO.blit(table[image[0]][image[1]], (x*32, y*32))
                
                x += 1
            y += 1
            x = 0
        
        s = pygame.Surface((32,32))
        s.fill((255,0,0))
        g = pygame.Surface((32,32))
        g.fill((0,255,0))
        
        SO.blit(s, (512,0))
        SO.blit(g, (544,0))
        
        
        self.highlightEquipped(SO)    
        self.mouseover(SO)
            