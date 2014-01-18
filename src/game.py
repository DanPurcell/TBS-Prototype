from world import *
from math import *
from player import *
from unit import *
from tiletable import *
from sidebar import *
from misc import *
from menu import *
from messages import *

class Game:
    def __init__(self, players, units):
        self.world = World()
        self.players = []
        self.units = []

        self.time = 0.0
        
        self.menu = None
        
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
        
        self.currentplayer = 0
        
        self.selected = None
        
        self.attacks = None
           
        self.nextUnit()
        
    def advanceTime(self, time):
        self.time = time
        
        for u in self.units:
            u.update(time)
        
    def nextUnit(self):    
        units = []
        
        self.units.sort(key=lambda x: x.atime, reverse=False)
        
        for u in self.units:
            if u.alive:
                units.append(u)
                
        if len(units) == 0:
            return None           
                
        if units[0].owner != self.currentplayer:
            self.units = units
            self.selectUnit(self.units[0].pos)
            self.advanceTime(self.selected.atime)
            self.nextPlayer()
                        
            return
        
        best = units[0].atime
         
        for u in range(1, len(units)):
            if units[u].atime == best:
                if units[u].owner != self.currentplayer:
                    self.units = units
                    self.selectUnit(self.units[u].pos)
                    self.advanceTime(self.selected.atime)
                    self.nextPlayer()
                   
                    return
                 
        self.units = units
        self.selectUnit(self.units[0].pos)
        self.advanceTime(self.selected.atime)
                
        return
    
    def nextPlayer(self):
        self.currentplayer = (self.currentplayer + 1) % len(self.players)
        
    def drawOrder(self, SO):
        mp = pygame.mouse.get_pos()
        mp = (mp[0]/32, mp[1]/32)
        
        for i in range(len(self.units)):
            self.units[i].draw(SO, self.table, self.time, self.players[self.units[i].owner].color, (i, 16))
            t = self.units[i].atime - self.time
            t = "%0.2f" % t
            m = message(str(t), (255,255,255))
            SO.blit(m, ((i*32) + 10, 532))
            
            if mp == self.units[i].pos:
                pygame.draw.rect(SO, (255,255,255), (i*32, 512, 32, 32),1)          
        
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
        
        for f in self.listAdjacent(self.selected.pos):
            if f.owner == self.selected.owner:
                friends.append(f)

        return friends
    
    def unitAt(self, tile):
        for u in range(len(self.units)):
            if self.units[u].pos == tile:
                return self.units[u]
        
        return None
     
    def castStun(self):
        if self.attacks == None:
            return
        
        u = self.unitAt(self.attacks[0])
        
        if u != None:
            a = self.selected.getAttribute('Cast Speed')

            t = 1.0/a * 100.0
    
            self.selected.addTime(t)
            
            mpen = self.selected.getAttribute('Magicpen')
            mresist = u.getAttribute('Magic Resist')
        
            mpen -= mresist
            mpen *= 0.05
        
            s = 1.0 + (1.0*mpen)            
            
            u.addTime(s)
   
    def castBeam(self, SO):
        for v in self.spellTargetsBeam(SO, False):
            
            targ = self.unitAt(v)

            mdamage = self.selected.getAttribute('Magic Damage')
            mpen = self.selected.getAttribute('Magicpen')
            mresist = targ.getAttribute('Magic Resist')
                    
            d = bonusDamage(mdamage, mpen, mresist)
                    
            targ.takeDamage(d)
            
        a = self.selected.getAttribute('Cast Speed')

        t = 1.0/a * 100.0
    
        self.selected.addTime(t)          
    
    def castSpell(self, SO):
        if self.selected == None:
            return
        
        if self.selected.memorised == None:
            return
        
        mc = self.selected.memorised.getAttribute('Mana Cost')
        
        if self.selected.currentmana < mc:
            return
        
        self.selected.currentmana -= mc
        
        n = self.selected.memorised.name
        
        if n == "Spell Beam":               
            self.castBeam(SO)
        elif n == "Spell Stun":
            self.castStun()
           
        self.nextUnit()
            
    def mouseEvent(self, event, SO):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return
        
        x, y =  event.pos
        tile = (int(math.floor(x/32)), int(math.floor(y/32)))
        
        if self.menu != None:
            self.menu.mouseEvent(event, SO)
            return
        
        if event.button == 3:
            self.sidebarUnit(self.unitAt(tile))
            return
        
        if event.pos[0] >= 512:
            self.sidebar.mouseEvent(event)
        else:       
            if self.selected == None:
                self.selectUnit(tile)
                return
            
            moves = self.getMoves()
            
            for m in moves:
                if m == tile:
                    self.moveSelected(m)
                    self.nextUnit()
                    return
            
            if self.selected.memorised != None:
                self.selectUnit(tile)

            self.getAttacks(SO)
            
            if self.attacks != None:
                for a in self.attacks:
                    if a == tile:
                        self.attack(self.unitAt(tile))
                        self.nextUnit()
                        return
                
            self.selectUnit(tile)
            
    def selectUnit(self, tile):
        for u in range(len(self.units)):
            if self.units[u].pos == tile:
                self.selected = self.units[u]
                self.sidebar.selectUnit(self.selected, self.table)
                
                return
        
        self.sidebar.selectUnit(None, self.table)
        return None
    
    def moveSelected(self, pos):
        d = dist(self.selected.pos, pos)
    
        self.selected.setPos(pos)
        
        speed = self.selected.getAttribute('Speed')
        t = (1.0/speed) * d
        
        self.selected.addTime(t)
        
    def attack(self, targ):
        damage = self.selected.getAttribute('Damage')
        ap = self.selected.getAttribute('Armorpen')

        armor = targ.getAttribute('Armor')
        
        d = bonusDamage(damage, ap, armor)
        
        targ.takeDamage(d)
        
        a = self.selected.getAttribute('Attack Speed')

        t = 1.0/a * 100
        
        self.selected.addTime(t)
            
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
             
    def spellTargetsBeam(self, SO, draw = False):
        blist = []
        
        b = pygame.Surface((32,32))
        b.set_alpha(50)
        b.fill((255,255,0))
        
        mp = pygame.mouse.get_pos()
        
        if mp[0] >= 512:
            mp = (512, mp[1])
        if mp[1] >= 512:
            mp = (mp[0], 512)
        
        r = pygame.Surface((32,32))
        r.set_alpha(50)
        r.fill((255,0,0))
        
        for p in self.listLine(self.selected.pos, (mp[0]/32, mp[1]/32)):
            u = self.unitAt(p)
            if p[0] > 15 or p[1] > 15 or p[0] < 0 or p[1] < 0:
                continue
            if u == None:
                SO.blit(b, (p[0]*32, p[1]*32))
                continue
            
            if self.unitAt(p).alive & (u != self.selected):
                SO.blit(r, (p[0]*32, p[1]*32))
                blist.append(p)                        
         
        return blist
    
    def spellTargetLOS(self, SO):
        attacks = []
        
        mp = pygame.mouse.get_pos()     
        
        b = pygame.Surface((32,32))
        b.set_alpha(50)
        b.fill((255,255,0))
        
        r = pygame.Surface((32,32))
        r.set_alpha(50)
        r.fill((255,0,0))
        
        l = self.listLine(self.selected.pos, (mp[0]/32, mp[1]/32))
        a = []
        
        for p in l:
            u = self.unitAt(p)
            if p[0] > 15 or p[1] > 15 or p[0] < 0 or p[1] < 0:
                continue
            if u == None:
                SO.blit(b, (p[0]*32, p[1]*32))
                continue
            else:
                if u != self.selected:
                    a.append(u.pos)                   

        if len(a) == 0:
            return []
        t = a[0]
        attacks.append(t)
        SO.blit(r, (t[0]*32, t[1]*32))
        
        return attacks      
             
    def getAttacks(self, SO):
        if self.selected == None:
            self.attacks = None
            return None
        if self.selected.atime > self.time:
            self.attacks = []
            return
        
        canattack = []
        
        pos = self.selected.pos
        
        if self.selected.memorised != None:
            mc = self.selected.memorised.getAttribute('Mana Cost')
            if self.selected.currentmana < mc:
                self.attacks = []
                return
            
            if self.selected.memorised.name == "Spell Beam":   
                self.attacks = self.spellTargetsBeam(SO, True)          
                return
            
            if self.selected.memorised.name == "Spell Stun":   
                self.attacks = self.spellTargetLOS(SO)          
                return
        
        if self.selected.body.righthand.name.find("Bow") != -1:
            for adj in self.listAdjacent(pos):
                if (adj.owner != self.selected.owner):
                    self.attacks = []
                    return
            
            for i in range(len(self.units)):
                if self.units[i].owner != self.selected.owner:
                    d = dist(pos, self.units[i].pos)
                    
                    if d <= self.selected.getAttribute('Range'):
                        canattack.append(self.units[i].pos)
                        
            self.attacks = canattack
            return
        
        for adj in self.listAdjacent(pos):
            if (adj.owner != self.selected.owner):
                canattack.append(adj.pos)
    
        self.attacks = canattack
        return
     
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
                             
        self.getAttacks(SO)
                             
        for p in self.attacks:
            if p[0]>15:
                continue
            if p[1]>15:
                continue
            if p[0]<0:
                continue
            if p[1]<0:
                continue
            
            SO.blit(r, (p[0]*32, p[1]*32))
            
        if self.selected.body.righthand.name.find("Bow") != -1:
                r = self.selected.getAttribute("Range")
                pygame.draw.circle(SO, (100, 0, 0), (16 + self.selected.pos[0]*32, 16 + self.selected.pos[1]*32), int(r*32), 2)
      
    def sidebarUnit(self, unit):
        self.sidebar.selectUnit(unit, self.table)
            
    def Menu(self):
        if self.selected.atime > 0.0:
            return
        
        if self.menu != None:
            self.selected.currenthealth = self.selected.getAttribute('Health')
            self.selected.currentmana = self.selected.getAttribute('Mana')
            self.menu = None
            return
        
        if self.selected == None:
            return
        
        self.menu = Menu(self.selected)
    
    def draw(self, SO):
        if self.menu != None:
            self.menu.draw(SO, self.table)
            return        
        
        self.world.draw(SO, self.table)
        for i in range(len(self.units)):
            if self.units[i].alive:
                self.units[i].draw(SO, self.table, self.time, self.players[self.units[i].owner].color)
            
        self.drawOrder(SO)    
        
        if self.selected != None:
            self.highlightUnit(SO)
            
        self.sidebar.draw(SO, self.table)
