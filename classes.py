import items, player

class Class:
    def __init__(self, name, inventory, hitDie, spellSlot):
        self.name = name
        self.inventory = inventory
        self.hitDie = hitDie
        self.spellSlot = spellSlot

    def __str__(self):
        inv = []
        for i in self.inventory:
            if i.name == 'Gold':
                inv.append(str(i.value) + ' ' + i.name)
            else:
                inv.append(i.name)
        invstr = ", ".join(inv)
        return "========\nClass: {}\nHit Die: 1d{}\nSpell Slots: {}\nStarting Inventory: {}\n========"\
            .format(self.name, self.hitDie, self.spellSlot, invstr)


class wizard(Class):
    def __init__(self):
        super().__init__(name="Wizard",
                         hitDie=6,
                         inventory=[items.dagger(), items.fireBolt(), items.Gold(5)],
                         spellSlot=10,)


class cleric(Class):
    def __init__(self):
        super().__init__(name="Cleric",
                         hitDie=8,
                         inventory=[items.warhammer(), items.cureWounds(), items.Gold(2)],
                         spellSlot=6)


class barbarian(Class):
    def __init__(self):
        super().__init__(name="Barbarian",
                         hitDie=12,
                         inventory=[items.axe(), items.healthPotion, items.Gold(4)],
                         spellSlot=None)


class ranger(Class):
    def __init__(self):
        super().__init__(name="Ranger",
                         hitDie=10,
                         inventory=[items.bow(), items.shortSword(), items.healthPotion()],  # add more items
                         spellSlot=3)


class rogue(Class):
    def __init__(self):
        super().__init__(name="Rogue",
                         hitDie=8,
                         inventory=[items.dagger(), items.healthPotion(), items.healthPotion()],
                         spellSlot=3)