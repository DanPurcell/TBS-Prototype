from verbose import *
class Player:
    def __init__(self, name):
        vprint("<" + name)
        indent(1)
        self.name = name
        indent(-1)
        vprint(name + ">")

print "player.py loaded"
