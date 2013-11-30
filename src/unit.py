from body import *
from verbose import *

def nextid(static={"count":0}):
        static["count"]+=1
        return static["count"]

class Unit:    
    def __init__(self, owner):
        self.iD = nextid()

        vprint("<Unit" + str(self.iD))
        indent(1)

        self.body = Body()
        
        self.owner = owner

        self.pos = (8, 8)

        self.attributes = {}

        self.currenthealth = self.getAttribute('Health')
        self.currentmana = self.getAttribute('Mana')
        
        print self.getAttribute('Armor')
        
        self.image = (1, 31)

        indent(-1)
        vprint("Unit" + str(self.iD) + ">")
        self.vReport()

    def getAttribute(self, at):
        return self.body.getAttribute(at)

    def setPos(self, pos):
        self.pos = pos

    def draw(self, SO, table):
        vprint("<unit.draw()")
        indent(1)
        #SO.blit(table[self.image[0]][self.image[1]], (self.pos[0]*32, self.pos[1]*32))
        self.body.draw(SO, table, self.pos)
        indent(-1)
        vprint("unit.draw()>")

    def vReport(self):
        vprint("<Unit" + str(self.iD) + " report")
        indent(1)
        vprint("pos: " + str(self.pos))
        indent(-1)
        vprint("Unit" + str(self.iD) + " report>")

print "unit.py loaded"
