class Item:
    def __init__(self, stats, name, image = (21, 0), icon = (21, 0)):
        self.stats = stats
        self.name = name
        self.image = image
        self.icon = icon

    def getAttribute(self, at):
        if self.stats.has_key(at):
            return self.stats[at]
        else:
            return 0

#Cloak
bluecloak = Item(({'Armor':1,
              'Magic Resist':1.0}), 'Blue Cloak', (22, 34), (5, 21))

purplecloak = Item(({'Armor':1,
              'Magic Resist':1.0}), 'Purple Cloak', (27, 34), (6, 21))

#Legs
jeans = Item(({'Armor':1,
              'Magic Resist':1.0}), 'Jeans', (44, 41), (44, 41))

#Boots
leatherboots = Item(({'Armor':1,
              'Magic Resist':1.0}), 'Leather Boots', (10, 34), (60, 20))

#Torso
blackrobe = Item(({'Armor':2,
              'Magic Resist':1.0}), 'Black Robe', (0, 33), (2, 22))

tshirt = Item(({'Armor':1,
              'Magic Resist':1.0}), 't-Shirt', (4, 33), (4, 33))

#Right Hand
axe = Item(({'Damage':10,
              'Armorpen':1.0}), 'Axe', (0, 38), (44, 27))

sword = Item(({'Damage':10,
              'Armorpen':1}), 'Sword', (43, 35), (4,29))

#Left Hand
bluebook = Item(({'Slots':2,
                   'Cast Speed': 1}), 'Blue Book', (39, 39), (3, 23))

#Body
malebody = Item(({'Health':100,
              'Mana':100,
              'Cast Speed':10,
              'Mana Regen': 5,
              'Health Regen':1,
              'Speed':2,
              'Attack Speed':10
              }), 'Male Body', (1, 31), (1, 31))

femalebody = Item(({'Health':100,
              'Mana':100,
              'Cast Speed':10,
              'Mana Regen': 5,
              'Health Regen':1,
              'Speed':2,
              'Attack Speed':10
              }), 'Female Body', (0, 31), (0, 31))

#Head
brownhat = Item(({'Magic Resist':2,
              'Health':10}), 'Brown Hat', (21, 41), (39, 22))

#Hands
leathergloves = Item(({'Armor':1,
                       'Magic Resist':1}), 'Leather Gloves', (58, 34), (38, 44))

#Rings
healthring = Item(({'Health':50,
                       'Health Regen':1}), 'Health Ring', (0, 0), (52, 25))
manaring = Item(({'Mana':50,
                       'Mana Regen':2}), 'Health Ring', (0, 0), (55, 25))

#Amulets
healthamulet = Item(({'Health':50,
                       'Health Regen':1}), 'Health Amulet', (0, 0), (12, 20))
manaamulet = Item(({'Mana':50,
                       'Mana Regen':2}), 'Health Amulet', (0, 0), (11, 20))

print "items.py loaded"
