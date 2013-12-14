from items import *
from random import *

class Body:
    def __init__(self):
        self.randomGear()  

    def randomGear(self):
        self.cloak = cloaks[randint(0, len(cloaks) - 1)]
        self.body = bodies[randint(0, len(bodies) - 1)]
        self.head = head[randint(0, len(head) - 1)]
        self.legs = legs[randint(0, len(legs) - 1)]
        self.boots = boots[randint(0, len(boots) - 1)]
        self.torso = torso[randint(0, len(torso) - 1)]
        self.hands = hands[randint(0, len(hands) - 1)]
        self.righthand = righthand[randint(0, len(righthand) - 1)]
        if self.righthand.name.find("Bow") == -1:
            self.lefthand = lefthand[randint(0, len(lefthand) - 1)]
            if self.lefthand.name.find("Book") != -1:
                self.righthand = nullspell 
        else:  
            self.lefthand = None  
        
        self.leftring = rings[randint(0, len(rings) - 1)]
        self.rightring = rings[randint(0, len(rings) - 1)]
        self.amulet = amulets[randint(0, len(amulets) - 1)]  
        
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
       

print "body.py loaded"
