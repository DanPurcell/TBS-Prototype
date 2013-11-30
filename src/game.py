from world import *
from player import *
from unit import *
from tiletable import *
from verbose import *
from sidebar import *

class Game:
    def __init__(self, players, units):
        vprint ("Initialising game")
        indent(1)
        self.world = World()
        self.players = []
        self.units = []

        for i in range(players):
            self.players.append(Player("Player" + str(i + 1)))
            
            for u in range(units):
                unit = Unit(i)
                unit.vReport()
                self.units.append(unit)

        vprint("units:" + str(len(self.units)))
        self.table = load_tile_table("tiles.png", 32, 32)
        
        self.sidebar = Sidebar()
        #self.sidebar.selectUnit(self.units[0], self.table)
           
        indent(-1)
        vprint ("Game initialised")
        
    def mouseEvent(self, event):
        if event.pos[0] >= 512:
            self.sidebar.mouseEvent(event)
        else:
            print "Board", event.pos
            x, y =  event.pos
            tile = (int(math.floor(x/32)), int(math.floor(y/32)))
            print "Board", event.pos, tile[0], tile[1]
            
            self.selectUnit(tile)
            
    def selectUnit(self, tile):
        for u in range(len(self.units)):
            if self.units[u].pos == tile:
                self.sidebar.selectUnit(self.units[u], self.table)
                return
        
        self.sidebar.selectUnit(None, self.table) 
        return None
        

    def draw(self, SO):
        vprint("<game.draw()")
        self.sidebar.draw(SO)
        indent(1)
        self.world.draw(SO, self.table)
        for u in range(len(self.units)):
            self.units[u].draw(SO, self.table)

        indent(-1)
        vprint("game.draw()>")
