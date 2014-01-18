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

NoItem = Item(({}), 'Nothing',(0,0),(0,0))

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
bluecloak = Item(({'Mana Regen':2.0}), 'Blue Cloak', (22, 34), (5, 21))
purplecloak = Item(({'Health Regen':1.0}), 'Purple Cloak', (27, 34), (6, 21))
browncloak = Item(({'Range':1.0}), 'Brown Cloak', (28, 34), (3, 21))
greycloak = Item(({'Attack Speed':5.0}), 'Grey Cloak', (25, 34), (4, 21))

cloaks = (bluecloak, purplecloak, browncloak, greycloak)

#Legs
jeans = Item(({'Attack Speed':5.0}), 'Jeans', (44, 41), (44, 41))
greentrousers = Item(({'Health':5.0}), 'Green Trousers', (46, 41), (46, 41))
chaintrousers = Item(({'Armor':2.0}), 'Chain Trousers', (43, 41), (43, 41))
purpletrousers = Item(({'Health Regen':1.0}), 'Purple Trousers', (45, 41), (45, 41))

legs = (jeans, purpletrousers, chaintrousers, greentrousers)

#Boots
leatherboots = Item(({'Speed':1.0}), 'Leather Boots', (10, 34), (60, 20))
chainboots = Item(({'Armor':2.0}), 'Chain Boots', (12, 34), (49, 21))
greenboots = Item(({'Armor':1.0,
                    'Health':1.0}), 'Green Boots', (416/32, 1088/32), (2016/32, 640/32))

boots = (leatherboots, chainboots, greenboots)

#Torso
blackrobe = Item(({'Cast Speed':5.0}), 'Black Robe', (0, 33), (2, 22))
bluerobe = Item(({'Magic Damage':1.0}), 'Blue Robe', (672/32, 1056/32), (1696/32, 672/32))
leatherarmor = Item(({'Armor':1.0,
                      'Speed':1.0}), 'Leather Armor', (1504/32, 1024/32), (704/32, 672/32))
tshirt = Item(({'Heath':5.0}), 'T-Shirt', (4, 33), (4, 33))
chainarmor = Item(({'Armor':3.0,
                    'Cast Speed':-10,
                    'Attack Speed:':-5}), 'Chain Armor', (5, 32), (2, 21))
platearmor = Item(({'Armor':5.0,
                    'Cast Speed':-20,
                    'Attack Speed:':-10}), 'Plate Armor', (6, 33), (31, 21))

torso = (blackrobe, bluerobe, leatherarmor, tshirt, chainarmor, platearmor)

#Right Hand
dagger = Item(({'Damage':6.0,
             'Attack Speed':20.0}), 'Dagger', (704/32, 1152/32), (896/32, 896/32))
axe = Item(({'Damage':15.0,
             'Attack Speed':-20.0}), 'Axe', (0, 38), (44, 27))
longsword = Item(({'Damage':10.0}), 'Long Sword', (43, 35), (4,29))
katana = Item(({'Damage':9.0,
              'Armorpen':3.0,
              'Attack Speed':5.0}), 'Katana', (1536/32, 1152/32), (1280/32, 1504/32))
flail = Item(({'Damage':8.0,
              'Attack Speed':10.0}), 'Flail', (14,36), (45, 28))
shortbow = Item(({'Damage':5.0,
              'Attack Speed':10.0,
              'Range':4.0}), 'Short Bow', (57,35), (1, 30))
longbow = Item(({'Damage':5.0,
              'Attack Speed':-10.0,
              'Range':6.0}), 'Long Bow', (58,35), (5, 30))

righthand = (dagger, axe, longsword, katana, flail, shortbow, longbow)

#Left Hand
lightbook = Item(({}), 'Light Book', (51, 39), (1, 23))

shield = Item(({'Armor': 4.0}), 'Shield', (1, 39), (54, 22))
greenshield = Item(({'Armor': 2.0,
                     'Health':5.0}), 'Green Shield', (23, 39), (5, 22))
blueshield = Item(({'Armor': 2.0,
                     'Magic Resist':2.0}), 'Blue Shield', (26, 39), (48, 22))
spikedshield = Item(({'Armor': 2.0,
                      'Damage':2.0}), 'Spiked Shield', (1152/32, 1248/32), (1376/32, 1408/32))

lefthand = (lightbook, shield, greenshield, blueshield, spikedshield)

#Head
brownhat = Item(({'Mana Regen':2.0}), 'Brown Hat', (21, 41), (39, 22))
helm = Item(({'Armor':2.0}), 'Helm', (63, 40), (41, 22))

head = (brownhat, helm)

#Hands
leathergloves = Item(({'Attack Speed':5.0}), 'Leather Gloves', (58, 34), (38, 44))
gauntlets = Item(({'Armor':2.0}), 'Gauntlets', (1952/32, 1088/32), (37, 44))
whitegloves = Item(({'Mana Regen':2.0}), 'White Gloves', (8, 35), (58, 21))

hands = (leathergloves, gauntlets, whitegloves)
#Rings
healthring = Item(({'Health':5.0}), 'Health Ring', (0, 0), (52, 25))
manaring = Item(({'Mana':2.0}), 'Mana Ring', (0, 0), (55, 25))
speedring = Item(({'Speed':1.0}), 'Speed Ring', (0, 0), (50, 25))
armorring = Item (({'Armor':1.0}), 'Armor Ring', (0, 0), (57, 25))
apenring = Item(({'Armorpen':2.0}), 'Armorpen Ring', (0, 0), (19, 25))
damagering = Item(({'Damage':1.0}), 'Damage Ring', (0, 0), (18, 25))
magicresistring = Item(({'Magic Resist':1.0}), 'Magic Resist Ring', (0, 0), (49, 25))
mpenring = Item(({'Magicpen':1.0}), 'Magicpen Ring', (0, 0), (16, 25))
rangering = Item(({'Range':1.0}), 'Range Ring', (0, 0), (56, 25))
mdamagering = Item(({'Magic Damage':1.0}), 'Magic Damage Ring', (0, 0), (28, 46))
cspeedring = Item(({'Cast Speed':5.0}), 'Cast Speed Ring', (0, 0), (29, 46))
aspeedring = Item(({'Attack Speed':5.0}), 'Attack Speed Ring', (0, 0), (30, 46))

rings = (healthring, manaring, speedring, armorring, apenring, damagering, magicresistring, mpenring, rangering, mdamagering, cspeedring, aspeedring)

#Amulets
healthamulet = Item(({'Health':10.0}), 'Health Amulet', (0, 0), (12, 20))
manaamulet = Item(({'Mana':4.0}), 'Mana Amulet', (0, 0), (11, 20))
speedamulet = Item(({'Speed':2.0}), 'Speed Amulet', (0, 0), (13, 20))
armorpenamulet = Item(({'Armorpen':4.0}), 'Armorpen Amulet', (0, 0), (8, 20))
armoramulet = Item(({'Armor':2.0}), 'Armor Amulet', (0, 0), (10, 20))
damageamulet = Item(({'Damage':2.0}), 'Damage Amulet', (0, 0), (15, 20))
magicresistamulet = Item(({'Magic Resist':1.0}), 'Magic Resist Amulet', (0, 0), (9, 20))
mpenamulet = Item(({'Magicpen':2.0}), 'Magicpen Amulet', (0, 0), (18, 20))
rangeamulet = Item(({'Range':2.0}), 'Range Amulet', (0, 0), (17, 20))
mdamageamulet = Item(({'Magic Damage':2.0}), 'Magic Damage Amulet', (0, 0), (46, 20))
cspeedamulet = Item(({'Cast Speed':10.0}), 'Cast Speed Amulet', (0, 0), (44, 20))
aspeedamulet = Item(({'Attack Speed':10.0}), 'Attack Speed Amulet', (0, 0), (42, 20))

amulets = (healthamulet, manaamulet, speedamulet, armoramulet, armorpenamulet, damageamulet, magicresistamulet, mpenamulet, rangeamulet, mdamageamulet, cspeedamulet, aspeedamulet)

print "items.py loaded"
