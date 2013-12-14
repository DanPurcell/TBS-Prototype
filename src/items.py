from spells import *

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
            return 0.0

#Body
malebody = Item(({'Health':30.0,
              'Mana':10.0,
              'Cast Speed':100.0,
              'Mana Regen': 1.0,
              'Health Regen':1.0,
              'Speed':2.0,
              'Attack Speed':100.0
              }), 'Male Body', (1, 31), (1, 31))

femalebody = Item(({'Health':30.0,
              'Mana':10.0,
              'Cast Speed':100.0,
              'Mana Regen': 1.0,
              'Health Regen':1.0,
              'Speed':2.00,
              'Attack Speed':100.0
              }), 'Female Body', (0, 31), (0, 31))

bodies = (malebody, femalebody)

#Cloak
bluecloak = Item(({'Mana':1.0}), 'Blue Cloak', (22, 34), (5, 21))

purplecloak = Item(({'Attack Speed':10.0}), 'Purple Cloak', (27, 34), (6, 21))

cloaks = (bluecloak, purplecloak)

#Legs
jeans = Item(({'Damage':1.0}), 'Jeans', (44, 41), (44, 41))

greentrousers = Item(({'Health':5.0}), 'Green Trousers', (46, 41), (46, 41))

chaintrousers = Item(({'Armor':1.0}), 'Chain Trousers', (43, 41), (43, 41))

purpletrousers = Item(({'Magicpen':1.0}), 'Purple Trousers', (45, 41), (45, 41))

legs = (jeans, purpletrousers, chaintrousers, greentrousers)
#Boots
leatherboots = Item(({'Speed':1.0}), 'Leather Boots', (10, 34), (60, 20))

chainboots = Item(({'Armor':1.0}), 'Chain Boots', (12, 34), (49, 21))

boots = (leatherboots, chainboots)

#Torso
blackrobe = Item(({'Magicpen':1.0}), 'Black Robe', (0, 33), (2, 22))

tshirt = Item(({'Heath':5.0}), 'T-Shirt', (4, 33), (4, 33))

platearmor = Item(({'Armor':2.0}), 'Plate Armor', (6, 33), (31, 21))

torso = (blackrobe, tshirt, platearmor)

#Right Hand
axe = Item(({'Damage':15.0,
             'Attack Speed':-20.0}), 'Axe', (0, 38), (44, 27))

sword = Item(({'Damage':10.0,
              'Armorpen':2.0}), 'Sword', (43, 35), (4,29))

flail = Item(({'Damage':8.0,
              'Attack Speed':10.0}), 'Flail', (14,36), (45, 28))

shortbow = Item(({'Damage':5.0,
              'Attack Speed':10.0,
              'Range':4.0}), 'Short Bow', (57,35), (1, 30))

longbow = Item(({'Damage':5.0,
              'Attack Speed':-10.0,
              'Range':6.0}), 'Long Bow', (58,35), (5, 30))

righthand = (axe, sword, flail, shortbow, longbow)

#Left Hand
lightbook = Item(({}), 'Light Book', (51, 39), (1, 23))

shield = Item(({'Armor': 2.0}), 'Shield', (32, 39), (46, 22))

lefthand = (lightbook, shield)

#Head
brownhat = Item(({'Magic Resist':1.0}), 'Brown Hat', (21, 41), (39, 22))
helm = Item(({'Armor':1.0}), 'Helm', (63, 40), (41, 22))

head = (brownhat, helm)

#Hands
leathergloves = Item(({'Attack Speed':10.0}), 'Leather Gloves', (58, 34), (38, 44))
whitegloves = Item(({'Mana Regen':1.0,
                       'Magicpen':2.0}), 'White Gloves', (8, 35), (58, 21))

hands = (leathergloves, whitegloves)
#Rings
healthring = Item(({'Health':5.0,
                       'Health Regen':1.0}), 'Health Ring', (0, 0), (52, 25))
manaring = Item(({'Mana':1.0,
                       'Mana Regen':2.0}), 'Health Ring', (0, 0), (55, 25))
speedring = Item(({'Speed':1.0}), 'Speed Ring', (0, 0), (50, 25))

damagering = Item(({'Damage':1.0}), 'Damage Ring', (0, 0), (18, 25))

apenring = Item(({'Armorpen':1.0}), 'Armorpen Ring', (0, 0), (19, 25))

mpenring = Item(({'Magicpen':1.0}), 'Magicpen Ring', (0, 0), (16, 25))

rangering = Item(({'Range':1.0}), 'Range Ring', (0, 0), (56, 25))

rings = (healthring, manaring, speedring, damagering, apenring, mpenring, rangering)

#Amulets
healthamulet = Item(({'Health':5.0,
                       'Health Regen':1.0}), 'Health Amulet', (0, 0), (12, 20))
manaamulet = Item(({'Mana':1.0,
                       'Mana Regen':2.0}), 'Mana Amulet', (0, 0), (11, 20))

speedamulet = Item(({'Speed':1.0}), 'Speed Amulet', (0, 0), (13, 20))

armorpenamulet = Item(({'Armorpen':1.0}), 'Armorpen Amulet', (0, 0), (8, 20))

armoramulet = Item(({'Armor':1.0}), 'Armor Amulet', (0, 0), (10, 20))

damageamulet = Item(({'Damage':1.0}), 'Damage Amulet', (0, 0), (15, 20))

magicresistamulet = Item(({'Magic Resist':1.0}), 'Magic Resist Amulet', (0, 0), (10, 20))

mpenamulet = Item(({'Magicpen':1.0}), 'Magicpen Amulet', (0, 0), (16, 20))

rangeamulet = Item(({'Range':1.0}), 'Range Amulet', (0, 0), (17, 20))

amulets = (healthamulet, manaamulet, speedamulet, armorpenamulet, magicresistamulet, damageamulet, mpenamulet, rangeamulet)

print "items.py loaded"
