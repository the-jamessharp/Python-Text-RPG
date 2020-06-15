class NPC:
    def __init__(self, name, race, hp, ac, charClass, str, con, dex, int, wis, cha):
        self.name = name
        self.race = race
        self.hp = hp
        self.ac = ac
        self.charClass = charClass
        self.str = str
        self.con = con
        self.dex = dex
        self.int = int
        self.wis = wis
        self.cha = cha

    def is_alive(self):
        return self.hp > 0

    def npc_mod(self, stat):
        if stat >= 20:
            statMod = 5
        elif stat >= 18:
            statMod = 4
        elif stat >= 16:
            statMod = 3
        elif stat >= 14:
            statMod = 2
        elif stat >= 12:
            statMod = 1
        elif stat >= 10:
            statMod = 0
        elif stat >= 8 :
            statMod = -1
        elif stat >= 6:
            statMod = -2
        elif stat >= 4:
            statMod = -3
        else:
            statMod = -4
        return statMod

    def __str__(self):
        return "\n========\nName: {}\nRace: {}\nClass: {}\nHP: {}\nAC: {}\nSTR: {}\tCON: {}\tDEX: {}\nINT: {}\tWIS: {}\tCHA: {}\n========" \
            .format(self.name, self.race, self.charClass, self.hp, self.ac, self.str, self.con, self.dex, self.int, self.wis, self.cha)


class sypha(NPC):
    def __init__(self):
        super().__init__(name="Sypha",
                         race="Human",
                         charClass="Sorcerer",
                         hp=22,
                         ac=13,
                         str=10,
                         con=12,
                         dex=11,
                         int=15,
                         wis=10,
                         cha=18)


class rilma(NPC):
    def __init__(self):
        super().__init__(name="Ril'ma",
                         race="Elf",
                         charClass="Rogue",
                         hp=19,
                         ac=18,
                         str=12,
                         con=11,
                         dex=20,
                         int=13,
                         wis=16,
                         cha=8)


class ulfgar(NPC):
    def __init__(self):
        super().__init__(name="Ulfgar",
                         race="Dwarf",
                         charClass="Barbarian",
                         hp=45,
                         ac=14,
                         str=18,
                         con=16,
                         dex=12,
                         int=6,
                         wis=8,
                         cha=14)


class tirin(NPC):
    def __init__(self):
        super().__init__(name="Tirin",
                         race="Gnome",
                         charClass="Cleric",
                         hp=24,
                         ac=16,
                         str=11,
                         con=12,
                         dex=10,
                         int=16,
                         wis=18,
                         cha=10)


class kvass(NPC):
    def __init__(self):
        super().__init__(name="K'vass",
                         race="Human",
                         charClass="Wizard",
                         hp=50,
                         ac=15,
                         str=11,
                         con=14,
                         dex=10,
                         int=20,
                         wis=16,
                         cha=16)