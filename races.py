class Race:
    def __init__(self, name, strMod, conMod, dexMod, intMod, wisMod, chaMod):
        self.name = name
        self.strMod = strMod
        self.conMod = conMod
        self.dexMod = dexMod
        self.intMod = intMod
        self.wisMod = wisMod
        self.chaMod = chaMod

    def __str__(self):
        return "\n========\nRace: {}\nSTR Mod: {}\nCON Mod: {}\nDEX Mod: {}\nINT Mod: {}\nWIS Mod: {}\nCHA Mod: {}\n========"\
                .format(self.name, self.strMod, self.conMod, self.dexMod, self.intMod, self.wisMod, self.chaMod)


class human(Race):
    def __init__(self):
        super().__init__(name="Human",
                         strMod=1,
                         conMod=1,
                         dexMod=1,
                         intMod=1,
                         wisMod=1,
                         chaMod=1)


class elf(Race):
    def __init__(self):
        super().__init__(name="Elf",
                         strMod=0,
                         conMod=0,
                         dexMod=2,
                         intMod=1,
                         wisMod=0,
                         chaMod=0)


class dwarf(Race):
    def __init__(self):
        super().__init__(name="Dwarf",
                         strMod=2,
                         conMod=2,
                         dexMod=0,
                         intMod=0,
                         wisMod=0,
                         chaMod=0)


class gnome(Race):
    def __init__(self):
        super().__init__(name="Gnome",
                         strMod=0,
                         conMod=0,
                         dexMod=1,
                         intMod=2,
                         wisMod=0,
                         chaMod=0)


class tiefling(Race):
    def __init__(self):
        super().__init__(name="Tiefling",
                         strMod=0,
                         conMod=1,
                         dexMod=0,
                         intMod=0,
                         wisMod=0,
                         chaMod=2)


class halforc(Race):
    def __init__(self):
        super().__init__(name="Half-Orc",
                         strMod=2,
                         conMod=0,
                         dexMod=0,
                         intMod=0,
                         wisMod=0,
                         chaMod=1)