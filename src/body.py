from items import *
from verbose import *

class Body:
    def __init__(self):
        vprint("<Body")
        indent(1)
        
        self.cloak = purplecloak
        self.body = malebody
        self.head = brownhat
        self.legs = jeans
        self.boots = leatherboots
        self.torso = blackrobe
        self.hands = leathergloves
        self.righthand = axe
        self.lefthand = bluebook
        self.leftring = manaring
        self.rightring = healthring
        self.amulet = manaamulet
                
        self.slots = 3        

        indent(-1)
        vprint("Body>")

    def getAttribute(self, at):
        r = 0

        if self.cloak != None:
            r += self.cloak.getAttribute(at)
        if self.body != None:
            r += self.body.getAttribute(at)
        if self.head != None:
            r += self.head.getAttribute(at)
        if self.legs != None:
            r += self.legs.getAttribute(at)
        if self.boots != None:
            r += self.boots.getAttribute(at)
        if self.torso != None:
            r += self.torso.getAttribute(at)
        if self.hands != None:
            r += self.hands.getAttribute(at)
        if self.righthand != None:
            r += self.righthand.getAttribute(at)
        if self.lefthand != None:
            r += self.lefthand.getAttribute(at)
        if self.leftring != None:
            r += self.leftring.getAttribute(at)
        if self.rightring != None:
            r += self.rightring.getAttribute(at)
        if self.amulet != None:
            r += self.amulet.getAttribute(at)
        
        return r

    def draw(self, SO, table, pos):
        vprint("<body.draw()")
        indent(1)   
        
        if self.cloak != None:
            image = self.cloak.image                
            SO.blit(table[image[0]][image[1]], (pos[0]*32, pos[1]*32))
                          
        if self.body != None:
            image = self.body.image                
            SO.blit(table[image[0]][image[1]], (pos[0]*32, pos[1]*32))
            
        if self.head != None:
            image = self.head.image                
            SO.blit(table[image[0]][image[1]], (pos[0]*32, pos[1]*32))
            
        if self.legs != None:
            image = self.legs.image                
            SO.blit(table[image[0]][image[1]], (pos[0]*32, pos[1]*32))
            
        if self.boots != None:
            image = self.boots.image                
            SO.blit(table[image[0]][image[1]], (pos[0]*32, pos[1]*32))
        
        if self.torso != None:
            image = self.torso.image                
            SO.blit(table[image[0]][image[1]], (pos[0]*32, pos[1]*32))
            
        if self.hands != None:
            image = self.hands.image                
            SO.blit(table[image[0]][image[1]], (pos[0]*32, pos[1]*32))

        if self.righthand != None:
            image = self.righthand.image                
            SO.blit(table[image[0]][image[1]], (pos[0]*32, pos[1]*32))

        if self.lefthand != None:
            image = self.lefthand.image                
            SO.blit(table[image[0]][image[1]], (pos[0]*32, pos[1]*32))
            
        indent(-1)
        vprint("body.draw()>")

print "body.py loaded"
