#===============
#author = James Sharp
#purpose = list of currency, weapon, and spell classes
#===============

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class healthPotion(Item):
    def __init__(self):
        self.diceNum = 4
        self.diceSide = 4
        super().__init__(name="Health Potion",
                         description="A small vial with red, glittery liquid inside.")

    def __str__(self):
        return "\n========\n{}\nHealing Value: {}d{}\n========\n".format(self.name, self.diceNum, self.diceSide)

class Currency(Item):
    def __init__(self, name, description, value):
        self.value = value
        super().__init__(name, description)

    def __str__(self):
        return "\n========\n{}\nValue: {}\n========\n".format(self.name, self.value)

class Gold(Currency):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin that glistens in the sunlight.",
                         value=self.amt)


class Silver(Currency):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Silver",
                         description="Not quite as good as gold, but it'll do.",
                         value=self.amt)


class Copper(Currency):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Copper",
                         description="This may buy you a loaf of bread...",
                         value=self.amt)


class Weapon(Item):
    def __init__(self, name, description, diceNum, diceSide):
        self.diceNum = diceNum
        self.diceSide = diceSide
        super().__init__(name, description)

    def __str__(self):
        return "\n========\n{}\nDamage: {}d{}\n========\n".format(self.name, self.diceNum, self.diceSide)


class Melee(Weapon):
    def __init__(self, name, description, diceNum, diceSide, value):
        self.value = value
        super().__init__(name, description, diceNum, diceSide)

    def __str__(self):
        return "\n========\n{}\nDamage: {}d{}\nValue: {}\n========\n".format(self.name, self.diceNum, self.diceSide, self.value)


class Range(Weapon):
    def __init__(self, name, description, diceNum, diceSide, value):
        self.value = value
        super().__init__(name, description, diceNum, diceSide)

    def __str__(self):
        return "\n========\n{}\nDamage: {}d{}\nValue: {}\n========\n".format(self.name, self.diceNum, self.diceSide, self.value)


class Spell(Weapon):
    def __init__(self, name, description, diceNum, diceSide, school):
        self.school = school
        super().__init__(name, description, diceNum, diceSide)

    def __str__(self):
        return "\n========\n{}\nDamage: {}d{}\nSchool of Magic: {}\n========\n".format(self.name, self.diceNum, self.diceSide, self.school)


class dagger(Melee):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small blade, good for hiding, and also throwing!",
                         value=2,
                         diceNum=1,
                         diceSide=4)


class shortSword(Melee):
    def __init__(self):
        super().__init__(name="Short Sword",
                         description="A simple short sword",
                         value=10,
                         diceNum=1,
                         diceSide=6)


class longSword(Melee):
    def __init__(self):
        super().__init__(name="Long Sword",
                         description="A typical weapon for a knight.",
                         value=15,
                         diceNum=1,
                         diceSide=8)


class axe(Melee):
    def __init__(self):
        super().__init__(name="Axe",
                         description="A dual-bladed weapon good for decapitation!",
                         value=10,
                         diceNum=1,
                         diceSide=8)


class warhammer(Melee):
    def __init__(self):
        super().__init__(name="Warhammer",
                         description="A large hammer good for bashing in skulls.",
                         value=15,
                         diceNum=1,
                         diceSide=8)


class bow(Range):
    def __init__(self):
        super().__init__(name="Bow",
                         description="A standard bow for an archer.",
                         value=25,
                         diceNum=1,
                         diceSide=6)


class crossBow(Range):
    def __init__(self):
        super().__init__(name="Crossbow",
                         description="A compact, powerful ranged weapon",
                         value=25,
                         diceNum=1,
                         diceSide=8)


class fireBolt(Spell):
    def __init__(self):
        super().__init__(name="Fire Bolt",
                         school="Evocation",
                         description="A simple blast of magical fire.",
                         diceNum=2,
                         diceSide=8)


class magicMissile(Spell):
    def __init__(self):
        super().__init__(name="Magic Missile",
                         school="Evocation",
                         description="Three arcane missiles that blast your foe.",
                         diceNum=3,
                         diceSide=4)


class fireBall(Spell):
    def __init__(self):
        super().__init__(name="Fireball",
                         school="Evocation",
                         description="A massive ball of flame explodes on your enemy!",
                         diceNum=8,
                         diceSide=6)


class cureWounds(Spell):
    def __init__(self):
        super().__init__(name="Cure Wounds",
                         school="Life",
                         description="Heals major wounds",
                         diceNum=3,
                         diceSide=8)


class healingWord(Spell):
    def __init__(self):
        super().__init__(name="Healing Word",
                         school="Life",
                         description="Heals minor wounds",
                         diceNum=2,
                         diceSide=4)