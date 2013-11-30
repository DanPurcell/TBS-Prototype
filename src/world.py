from verbose import *

class World:
    def __init__(self):
        vprint("<World")
        indent(1)
        self.tiles = [x[:] for x in [[(0,0)]*16]*16]

        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[0])):
                if x%2 == 0:
                    if y%2 == 0:
                        self.tiles[x][y] = (14, 13)
                    else:
                        self.tiles[x][y] = (29, 13)
                else:
                    if y%2 == 1:
                        self.tiles[x][y] = (14, 13)
                    else:
                        self.tiles[x][y] = (29, 13)

        indent(-1)
        vprint("World>")
                
                        
    def placeUnit(self, unit, pos):
        if self.tiles[pos[0]][pos[1]] != None:
            print pos, "occupied", unit, "not placed"
            return

        self.tiles[pos[0]][pos[1]] = unit

    def draw(self, SO, table):
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[0])):
                SO.blit(table[self.tiles[x][y][0]][self.tiles[x][y][1]], (x*32, y*32))

print "world.py loaded"

