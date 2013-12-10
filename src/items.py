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

#Body
malebody = Item(({'Health':30,
              'Mana':50,
              'Cast Speed':100,
              'Mana Regen': 2,
              'Health Regen':1,
              'Speed':2,
              'Attack Speed':100
              }), 'Male Body', (1, 31), (1, 31))

femalebody = Item(({'Health':30,
              'Mana':50,
              'Cast Speed':100,
              'Mana Regen': 2,
              'Health Regen':1,
              'Speed':2,
              'Attack Speed':100
              }), 'Female Body', (0, 31), (0, 31))

bodies = (malebody, femalebody)

#Cloak
bluecloak = Item(({'Mana':5}), 'Blue Cloak', (22, 34), (5, 21))

purplecloak = Item(({'Attack Speed':10}), 'Purple Cloak', (27, 34), (6, 21))

cloaks = (bluecloak, purplecloak)

#Legs
jeans = Item(({'Damage':1}), 'Jeans', (44, 41), (44, 41))

greentrousers = Item(({'Health':5}), 'Green Trousers', (46, 41), (46, 41))

chaintrousers = Item(({'Armor':1}), 'Chain Trousers', (43, 41), (43, 41))

purpletrousers = Item(({'Magicpen':1}), 'Purple Trousers', (45, 41), (45, 41))

legs = (jeans, purpletrousers, chaintrousers, greentrousers)
#Boots
leatherboots = Item(({'Speed':1}), 'Leather Boots', (10, 34), (60, 20))

chainboots = Item(({'Armor':1}), 'Chain Boots', (12, 34), (49, 21))

boots = (leatherboots, chainboots)

#Torso
blackrobe = Item(({'Magicpen':1}), 'Black Robe', (0, 33), (2, 22))

tshirt = Item(({'Heath':5}), 'T-Shirt', (4, 33), (4, 33))

platearmor = Item(({'Armor':2}), 'Plate Armor', (6, 33), (31, 21))

torso = (blackrobe, tshirt, platearmor)

#Right Hand
axe = Item(({'Damage':15,
             'Attack Speed':-20}), 'Axe', (0, 38), (44, 27))

sword = Item(({'Damage':10,
              'Armorpen':2}), 'Sword', (43, 35), (4,29))

flail = Item(({'Damage':8,
              'Attack Speed':10}), 'Flail', (14,36), (45, 28))

shortbow = Item(({'Damage':5,
              'Attack Speed':10,
              'Range':4.0}), 'Short Bow', (57,35), (1, 30))

longbow = Item(({'Damage':5,
              'Attack Speed':-10,
              'Range':6.0}), 'Long Bow', (58,35), (5, 30))

righthand = (axe, sword, flail, shortbow, longbow)

#Left Hand
redbook = Item(({'Magic Damage':5}), 'Red Book', (47, 39), (2, 23))

bluebook = Item(({'Slots':2,
                   'Cast Speed': 1}), 'Blue Book', (49, 39), (3, 23))

whitebook = Item(({'Slots':2,
                   'Cast Speed': 1}), 'White Book', (50, 39), (19, 23))

shield = Item(({'Armor': 2}), 'Shield', (32, 39), (46, 22))

lefthand = (redbook, shield)

#Head
brownhat = Item(({'Magic Resist':1}), 'Brown Hat', (21, 41), (39, 22))
helm = Item(({'Armor':1}), 'Helm', (63, 40), (41, 22))

head = (brownhat, helm)

#Hands
leathergloves = Item(({'Attack Speed':10}), 'Leather Gloves', (58, 34), (38, 44))
whitegloves = Item(({'Mana Regen':1,
                       'Magicpen':2}), 'White Gloves', (8, 35), (58, 21))

hands = (leathergloves, whitegloves)
#Rings
healthring = Item(({'Health':5,
                       'Health Regen':1}), 'Health Ring', (0, 0), (52, 25))
manaring = Item(({'Mana':15,
                       'Mana Regen':2}), 'Health Ring', (0, 0), (55, 25))
speedring = Item(({'Speed':1}), 'Speed Ring', (0, 0), (50, 25))

damagering = Item(({'Damage':1}), 'Damage Ring', (0, 0), (18, 25))

apenring = Item(({'Armorpen':1}), 'Armorpen Ring', (0, 0), (19, 25))

mpenring = Item(({'Magicpen':1}), 'Magicpen Ring', (0, 0), (16, 25))

rangering = Item(({'Range':1.0}), 'Range Ring', (0, 0), (56, 25))

rings = (healthring, manaring, speedring, damagering, apenring, mpenring, rangering)

#Amulets
healthamulet = Item(({'Health':5,
                       'Health Regen':1}), 'Health Amulet', (0, 0), (12, 20))
manaamulet = Item(({'Mana':5,
                       'Mana Regen':2}), 'Mana Amulet', (0, 0), (11, 20))

speedamulet = Item(({'Speed':1}), 'Speed Amulet', (0, 0), (13, 20))

armorpenamulet = Item(({'Armorpen':1}), 'Armorpen Amulet', (0, 0), (8, 20))

armoramulet = Item(({'Armor':1}), 'Armor Amulet', (0, 0), (10, 20))

damageamulet = Item(({'Damage':1}), 'Damage Amulet', (0, 0), (15, 20))

magicresistamulet = Item(({'Magic Resist':1}), 'Magic Resist Amulet', (0, 0), (10, 20))

mpenamulet = Item(({'Magicpen':1}), 'Magicpen Amulet', (0, 0), (16, 20))

rangeamulet = Item(({'Range':1}), 'Range Amulet', (0, 0), (17, 20))

amulets = (healthamulet, manaamulet, speedamulet, armorpenamulet, magicresistamulet, damageamulet, mpenamulet, rangeamulet)

print "items.py loaded"
