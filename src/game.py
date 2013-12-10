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
        
        while (units * players) >= 16:
            units -= 1

        for i in range(players):
            self.players.append(Player("Player" + str(i + 1), (0, 255*i, 255)))
            
            for u in range(units):
                unit = Unit(i, (13*i + 1, 5+u))
                self.units.append(unit)

        self.table = load_tile_table("tiles.png", 32, 32)
        
        self.sidebar = Sidebar()
        self.sidebar.selectUnit(None, self.table)
        
        self.selected = None
           
        self.nextUnit()
        
    def nextUnit(self):    
        units = []
        
        self.units.sort(key=lambda x: x.atime, reverse=False)
        
        for u in self.units:
            if u.alive:
                units.append(u)
                
        if len(units) == 0:
            return None
                
        self.units = units
                
        self.selectUnit(self.units[0].pos)
        self.time = self.selected.atime
        
    def drawOrder(self, SO):
        for i in range(len(self.units)):
            self.units[i].draw(SO, self.table, self.time, self.players[self.units[i].owner].color, (i, 16))
        
    def wait(self):
        if self.selected == None:
            return
        
        self.selected.atime += 1.0
        self.nextUnit()
        
    def tileOccupied(self, tile):
        for u in range(len(self.units)):
            if self.units[u].pos == tile:
                if self.units[u].alive:
                    return True
        
        return False
    
    def adjacentFriends(self):
        friends = []
        
        
    
    def unitAt(self, tile):
        for u in range(len(self.units)):
            if self.units[u].pos == tile:
                return self.units[u]
        
        return None
        
    def mouseEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return
        
        x, y =  event.pos
        tile = (int(math.floor(x/32)), int(math.floor(y/32)))
        
        if event.button == 3:
            self.sidebarUnit(self.unitAt(tile))
            return
        
        if event.pos[0] >= 512:
            self.sidebar.mouseEvent(event)
        else:            
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
                        self.attack(self.unitAt(tile))
                        self.nextUnit()
                        return
                
            self.selectUnit(tile)
            
    def selectUnit(self, tile):        
        for u in range(len(self.units)):
            if self.units[u].pos == tile:
                self.selected = self.units[u]
                
                return
        
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
        
        self.selected.addTime(t)
        
        print "Act Time: " + str(t) + " Next: " + str(self.selected.atime)

    def attack(self, targ):
        damage = self.selected.getAttribute('Damage')
        ap = self.selected.getAttribute('Armorpen')

        armor = targ.getAttribute('Armor')
        
        ap -= armor
        ap *= 0.05
        
        mdamage = self.selected.getAttribute('Magic Damage')
        mpen = self.selected.getAttribute('Magicpen')
        mresist = targ.getAttribute('Magic Resist')
        
        mpen -= mresist
        mpen *= 0.05
        
        mdamage = mdamage + (mdamage*mpen)
        
        damage = damage + (damage*ap)
        
        if self.selected.currentmana < mdamage:
            mdamage = 0.0
        else:
            self.selected.costMana(mdamage)
        
        
        targ.takeDamage(damage + mdamage)
        
        a = self.selected.getAttribute('Attack Speed')
        
        t = 1.0/a * 100
        
        self.selected.addTime(t)
        
        print "Damage: " + str(damage) + " mod: " + str(ap) + " Magic Damage: " + str(mdamage)
        print "Act Time: " + str(t) + " Next: " + str(self.selected.atime)
    
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
             
    def listAdjacent(self, pos):
        adj = []
        adjacent = ((-1,-1),
                (0,-1),
                (1,-1),
                (-1,0),
                (1,0),
                (-1,1),
                (0,1),
                (1,1))
        
        for p in adjacent:
            checkx = pos[0] + p[0]
            checky = pos[1] + p[1]
            
            u = self.unitAt((checkx, checky))
            
            if u == None:
                continue
            
            if u.alive == True:
                adj.append(u)
                
        return adj
             
    def listLine(self, start, end):
        x1 = start[0]
        y1 = start[1]
        x2 = end[0]
        y2 = end[1]
        
        points = []
        issteep = abs(y2-y1) > abs(x2-x1)
        
        if issteep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
            
        rev = False
        
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            rev = True
            
        deltax = x2 - x1
        deltay = abs(y2-y1)
        error = int(deltax / 2)
        y = y1
        ystep = None
        
        if y1 < y2:
            ystep = 1
        else:
            ystep = -1
        for x in range(x1, x2 + 1):
            if issteep:
                points.append((y, x))
            else:
                points.append((x, y))
            error -= deltay
            if error < 0:
                y += ystep
                error += deltax
        # Reverse the list if the coordinates were reversed
        if rev:
            points.reverse()            
            
        return points
             
    def getAttacks(self):                                             
        if self.selected == None:
            return None
        if self.selected.atime > self.time:
            return []
        
        canattack = []
        
        pos = self.selected.pos
        
        if self.selected.body.righthand.name.find("Bow") != -1:
            for adj in self.listAdjacent(pos):
                if (adj.owner != self.selected.owner):
                    return []
            
            for i in range(len(self.units)):
                if self.units[i].owner != self.selected.owner:
                    x1 = pos[0]
                    y1 = pos[1]
                    x2 = self.units[i].pos[0]
                    y2 = self.units[i].pos[1]
                    
                    dist = sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
                    
                    if dist <= self.selected.getAttribute('Range'):
                        canattack.append(self.units[i].pos)
                        
            return canattack
        
        for adj in self.listAdjacent(pos):
            if (adj.owner != self.selected.owner):
                canattack.append(adj.pos)
            
        return canattack
                 
    def spellBeam(self, SO):
        blist = []
        
        b = pygame.Surface((32,32))
        b.set_alpha(50)
        b.fill((255,255,0))
        
        mp = pygame.mouse.get_pos()
        
        r = pygame.Surface((32,32))
        r.set_alpha(50)
        r.fill((255,0,0))
        
        for p in self.listLine(self.selected.pos, (mp[0]/32, mp[1]/32)):
            u = self.unitAt(p)
            if u == None:
                SO.blit(b, (p[0]*32, p[1]*32))
                continue
            
            if self.unitAt(p).alive & (u != self.selected):
                SO.blit(r, (p[0]*32, p[1]*32))
                blist.append(p)                        
         
        return blist
     
    def highlightUnit(self, SO):
        #self.spellBeam(SO) #TODO+-
        
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
      
    def sidebarUnit(self, unit):
        self.sidebar.selectUnit(unit, self.table)
            
    def draw(self, SO):
        self.sidebar.draw(SO)

        self.world.draw(SO, self.table)
        for i in range(len(self.units)):
            if self.units[i].alive:
                self.units[i].draw(SO, self.table, self.time, self.players[self.units[i].owner].color)
            
        self.drawOrder(SO)    
        
        if self.selected != None:
            self.highlightUnit(SO)
