class Inventory:
    def __init__(self, items):
        self.items = items

    def getAttribute(self, at):
        r = 0
        for i in range(len(self.items)):
            r += self.items[i].getAttribute(at)

        return r

    def draw(self, SO, table, pos):
        for i in range(len(self.items)):
            SO.blit(table[self.items[i].image[0]][self.items[i].image[1]], (pos[0]*32, pos[1]*32))

print "inventory.py loaded"
