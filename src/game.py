from world import *
from math import *
from player import *
from unit import *
from tiletable import *
from sidebar import *

class Game:
    def __init__(self, players, units):
        self.world = World()
        self.players = []
        self.units = []

        self.time = 0.0

        for i in range(players):
            self.players.append(Player("Player" + str(i + 1), (0, 255*i, 255)))
            
            for u in range(units):
                unit = Unit(i, (15*i, 3+u))
                self.units.append(unit)

        self.table = load_tile_table("tiles.png", 32, 32)
        
        self.sidebar = Sidebar()
        
        self.selected = None
           
        self.nextUnit()
        
    def nextUnit(self):
        atime = 99999.9
        best = None
        for u in range(len(self.units)):
            if (self.units[u].atime < atime) & (self.units[u].alive):
                best = u
                atime = self.units[u].atime
                
        if best == None:
            print "None son"
            return None
        
        best = self.units[best]        
                
        self.selectUnit(best.pos)
        
        self.time = self.selected.atime
        
        print "Time: " + str(self.time)
        
    def wait(self):
        self.selected.atime += 1.0
        self.nextUnit()
        
    def tileOccupied(self, tile):
        for u in range(len(self.units)):
            if self.units[u].pos == tile:
                if self.units[u].alive:
                    return True
        
        return False
    
    def unitAt(self, tile):
        for u in range(len(self.units)):
            if self.units[u].pos == tile:
                return self.units[u]
        
        return None
        
    def mouseEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return
        
        if event.pos[0] >= 512:
            self.sidebar.mouseEvent(event)
        else:
            x, y =  event.pos
            tile = (int(math.floor(x/32)), int(math.floor(y/32)))
            
            moves = self.getMoves()
            
            for m in moves:
                if m == tile:
                    self.moveSelected(m)
                    self.nextUnit()
                    return
                    
            attacks = self.getAttacks()
            
            if attacks != None:            
                for a in attacks:
                    if a == tile:
                        self.attack(self.selected, self.unitAt(tile))
                        self.nextUnit()
                        return
                
            self.selectUnit(tile)
            
    def selectUnit(self, tile):        
        for u in range(len(self.units)):
            if self.units[u].pos == tile:
                self.sidebar.selectUnit(self.units[u], self.table)
                self.selected = self.units[u]
                
                print "Next: " + str(self.selected.atime)
                
                return
        
        self.sidebar.selectUnit(None, self.table)
        self.selected = None
        return None
    
    def moveSelected(self, pos):
        x1 = self.selected.pos[0]
        y1 = self.selected.pos[1]
        x2 = pos[0]
        y2 = pos[1]
        
        dist = sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    
        self.selected.setPos(pos)
        
        speed = self.selected.getAttribute('Speed')
        t = (1.0/speed) * dist
        
        self.selected.atime += t
        
        print "Act Time: " + str(t) + " Next: " + str(self.selected.atime)

    def attack(self, att, targ):
        damage = att.getAttribute('Damage')
        ap = att.getAttribute('Armorpen')
        
        hp = targ.currenthealth
        armor = targ.getAttribute('Armor')
        
        ap -= armor
        ap *= 0.05
        
        damage = damage + (damage*ap)
        
        targ.takeDamage(damage)
        
        a = att.getAttribute('Attack Speed')
        
        t = 1.0/a * 100
        
        att.atime += t
        
        print "Damage: " + str(damage)
        print "Act Time: " + str(t) + " Next: " + str(att.atime)
    
    def getMoves(self):
        if self.selected == None:
            return []
        
        if self.selected.atime > self.time:
            return []
              
        canmove = []
        cantmove = []
                
        pos = self.selected.pos
        
        cantmove.append(pos)
        
        udlr = ((0,-1),
                (0,1),
                (-1,0),
                (1,0))
        
        steps = self.selected.getAttribute('Speed')       
        
        def checkcanlist(p):
            for m in canmove:
                if m == p:
                    return True
                
            return False
        
        def checkcantlist(p):
            for m in canmove:
                if m == p:
                    return True
                
            return False
        
        tocheck = []
        
        tocheck.append((pos[0], pos[1], steps))
        
        while len(tocheck) > 0:            
            p = tocheck.pop()  
                                         
            for d in udlr:
                checkx = p[0] + d[0]
                checky = p[1] + d[1]        

                if self.tileOccupied((checkx, checky)):
                    if checkcantlist((checkx, checky)) == False:
                        cantmove.append((checkx, checky))
                else:    
                    if p[2] > 0:                                       
                        tocheck.append((checkx, checky, p[2] - 1))
                        if checkcanlist((checkx, checky)) == False:
                            canmove.append((checkx, checky))                                      
        
        return canmove              
             
    def getAttacks(self):        
        if self.selected == None:
            return None
        if self.selected.atime > self.time:
            return []
        
        canattack = []
        
        pos = self.selected.pos
        
        adjacent = ((0,-1),
                (0,1),
                (-1,0),
                (1,0),
                (-1,-1),
                (-1,1),
                (1,1),
                (1,-1))
        
        for p in adjacent:
            checkx = pos[0] + p[0]
            checky = pos[1] + p[1]
            
            u = self.unitAt((checkx, checky))
            
            if u == None:
                continue
            
            if u.alive & (u.owner != self.selected.owner):
                canattack.append((checkx, checky))
            
        return canattack
                       
    def highlightUnit(self, SO):
        r = (self.selected.pos[0]*32, self.selected.pos[1]*32, 32, 32)
        pygame.draw.rect(SO, self.players[self.selected.owner].color, r, 1)
               
        g = pygame.Surface((32,32))
        g.set_alpha(50)
        g.fill((0,255,0))
        
        r = pygame.Surface((32,32))
        r.set_alpha(50)
        r.fill((255,0,0))     
        
        for p in self.getMoves():
            if p[0]>15:
                continue
            if p[1]>15:
                continue
            if p[0]<0:
                continue
            if p[1]<0:
                continue
            
            SO.blit(g, (p[0]*32, p[1]*32))
                             
        for p in self.getAttacks():
            if p[0]>15:
                continue
            if p[1]>15:
                continue
            if p[0]<0:
                continue
            if p[1]<0:
                continue
            
            SO.blit(r, (p[0]*32, p[1]*32))
            
    def draw(self, SO):
        self.sidebar.draw(SO)

        self.world.draw(SO, self.table)
        for u in range(len(self.units)):
            if self.units[u].alive:
                self.units[u].draw(SO, self.table, self.time, self.players[self.units[u].owner].color)
            
        if self.selected != None:
            self.highlightUnit(SO)
