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

    def addTime(self, time):
        self.atime += time

    def takeDamage(self, damage):
        self.currenthealth -= damage
        if self.currenthealth <= 0:
            self.alive = False
            self.currenthealth = 0

    def costMana(self, cost):
        self.currentmana -= cost
        if self.currentmana < 0.0:
            self.currentmana = 0.0

    def setPos(self, pos):
        self.pos = pos

    def draw(self, SO, table, time, color, pos=False):
        
        if pos == False:
            pos = self.pos
           
        #SO.blit(table[self.image[0]][self.image[1]], (self.pos[0]*32, self.pos[1]*32))
        self.body.draw(SO, table, pos)
        pygame.draw.rect(SO, color, (pos[0]*32 + 28, pos[1]*32, 4, 4))
        
        hp = int((self.currenthealth/self.getAttribute('Health'))*12)
        mp = int((self.currentmana/self.getAttribute('Mana'))*12)
        
        pygame.draw.line(SO, (255, 0, 0), (pos[0]*32, pos[1]*32 + 2), (pos[0]*32 + hp, pos[1]*32 + 2), 2)
        pygame.draw.line(SO, (0, 0, 255), (pos[0]*32, pos[1]*32 + 4), (pos[0]*32 + mp, pos[1]*32 + 4), 2)
        if self.atime > time:
            SO.blit(table[59][24], (pos[0]*32, pos[1]*32))

print "unit.py loaded"
