class Spell:
    def __init__(self, info, name, image = (21, 0), icon = (21, 0)):
        self.name = name
        self.stats = info
        self.image = image
        self.icon = icon
        
    def getAttribute(self, at):
        if self.stats.has_key(at):
            return self.stats[at]
        else:
            return 0
        
nullspell = Spell(({}), 'Spell Null')

spellbeam = Spell(({'Magic Damage':4.0,
                   'Cast Type':'beam',
                   'Mana Cost':5.0}), 'Spell Beam', (63, 38), (42, 35))

spellstun = Spell(({'Effect':'stun',
                   'Cast Type':'los',
                   'Mana Cost':5.0}), 'Spell Stun', (60, 38), (58, 42))

class Spellbook:
    def __init__(self, name, spells):
        self.name = name
        self.spells = spells
        
lightspellbook = Spellbook("Light Book", (spellbeam, spellstun))

spellbooks = {'Light Book':lightspellbook}
        
