from body import *
import pygame

def nextid(static={"count":0}):
        static["count"]+=1
        return static["count"]

class Unit:    
    def __init__(self, owner, pos):

        self.iD = nextid()

        self.body = Body()
        
        self.owner = owner

        self.pos = pos

        self.attributes = {}

        self.currenthealth = self.getAttribute('Health')
        self.currentmana = self.getAttribute('Mana')
        
        self.alive = True
        
        self.atime = 0.0
        
        print self.getAttribute('Speed')
        
        self.image = (1, 31)

    def getAttribute(self, at):
        return self.body.getAttribute(at)

    def takeDamage(self, damage):
        self.currenthealth -= damage
        if self.currenthealth <= 0:
            self.alive = False
            self.currenthealth = 0

    def setPos(self, pos):
        self.pos = pos

    def draw(self, SO, table, time, color):
        #SO.blit(table[self.image[0]][self.image[1]], (self.pos[0]*32, self.pos[1]*32))
        self.body.draw(SO, table, self.pos)
        pygame.draw.line(SO, color, (self.pos[0]*32, self.pos[1]*32 + 32), (self.pos[0]*32 + 32, self.pos[1]*32 + 32), 1)
        if self.atime > time:
            SO.blit(table[59][24], (self.pos[0]*32, self.pos[1]*32))

print "unit.py loaded"
