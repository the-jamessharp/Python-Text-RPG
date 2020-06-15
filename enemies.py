from random import randint

class Enemy:
    def __init__(self, name, hp, ac, type, diceNum, diceSide, atkMod, dmgMod, initMod):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.type = type
        self.diceNum = diceNum
        self.diceSide = diceSide
        self.atkMod = atkMod
        self.dmgMod = dmgMod
        self.initMod = initMod

    def is_alive(self):
        return self.hp > 0

    def attack(self):
        return randint(1,20) + self.atkMod


class giantWolf(Enemy):
    def __init__(self):
        super().__init__(name="Giant Wolf",
                         hp=37,
                         ac=14,
                         type="Beast",
                         diceNum=2,
                         diceSide=6,
                         atkMod=5,
                         dmgMod=3,
                         initMod=2)


class wolf(Enemy):
    def __init__(self):
        super().__init__(name="Wolf",
                         hp=11,
                         ac=13,
                         type="Beast",
                         diceNum=2,
                         diceSide=4,
                         atkMod=4,
                         dmgMod=2,
                         initMod=2)


class thug(Enemy):
    def __init__(self):
        super().__init__(name="Thug",
                         hp=32,
                         ac=11,
                         type="Human",
                         diceNum=1,
                         diceSide=6,
                         atkMod=4,
                         dmgMod=2,
                         initMod=0)


class bandit(Enemy):
    def __init__(self):
        super().__init__(name="Bandit",
                         hp=11,
                         ac=12,
                         type="Human",
                         diceNum=1,
                         diceSide=6,
                         atkMod=3,
                         dmgMod=1,
                         initMod=1)