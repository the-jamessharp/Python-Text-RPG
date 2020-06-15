from random import randint
import races, classes, items, world, tiles

class Player:
    def __init__(self, name, race, charClass, inventory, str, con, dex, wis, int, cha):
        self.name = name
        self.race = race
        self.charClass = charClass
        self.inventory = inventory
        self.ac = 13 + self.player_mod(dex)
        self.hp = self.get_hp(charClass, con)
        self.str = str
        self.con = con
        self.dex = dex
        self.wis = wis
        self.int = int
        self.cha = cha
        self.spellMod = self.get_spellMod(charClass)
        self.location_x, self.location_y = world.starting_position
        self.victory = False

    def __str__(self):
        return """========
        \nPlayer Name: {}\nPlayer Race: {}\nPlayer Class: {}\nAC: {}\nHP: {}\nSTR: {}\tCON: {}\tDEX: {}\nWIS: {}
        \tINT: {}\t CHA: {}\n========""".format(self.name, self.race.name, self.charClass.name, self.ac, self.hp,
                                                self.str, self.con, self.dex, self.wis, self.int, self.cha)

    def is_alive(self):
        return self.hp > 0

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def print_inventory(self):
        invStr = ''
        for item in self.inventory:
            invStr += item.name + '\n'
        print(invStr)

    def changeWeapon(self):
        global activeWeapon
        weapons = {}
        print('\nAvailable weapons or spells:')
        for item in self.inventory:
            if isinstance(item, items.Weapon):
                if isinstance(item, items.Spell):
                    if not item.school == 'Life':
                        weapons.update({item.name: item})
                    else:
                        continue
                weapons.update({item.name: item})
                print(item.name)
        while True:
            weaponChoice = input('\nPlease pick a weapon or spell to attack with: ')
            if weaponChoice in weapons:
                activeWeapon = weapons.get(weaponChoice)
                break
            else:
                print('Invalid weapon, please try again: ')
                continue

    def attack(self, enemy):
        damage = 0
        try:
            activeWeapon
        except NameError:
            self.changeWeapon()
        if isinstance(activeWeapon, items.Melee):
            mod = self.player_mod(self.str)
            atkRoll = randint(0, 20) + mod + 2
        elif isinstance(activeWeapon, items.Range):
            mod = self.player_mod(self.dex)
            atkRoll = randint(0, 20) + mod + 2
        elif isinstance(activeWeapon, items.Spell):
            mod = self.spellMod
            atkRoll = randint(0, 20) + mod + 2
        if atkRoll >= enemy.ac:
            print("You hit the {} with a {}!".format(enemy.name, atkRoll))
            for x in range(0, activeWeapon.diceNum):
                damage += randint(1, activeWeapon.diceSide)
            if atkRoll == 20:
                print("You scored a critical hit!")
                damage *= 2
            enemy.hp -= damage + mod
            print("You hit the {} for {}! They have {} health remaining.".format(enemy.name, damage, enemy.hp))
        else:
            print("You missed!")


    def flee(self, tile):
        available_moves = tile.adjacent_moves()
        r = randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)


    @classmethod
    def stat_input(cls):
        while True:
            name = input("Enter Character name: ")
            name = name.strip()
            try:
                if any(i.isdigit() for i in name):
                    continue
                else:
                    break
            except ValueError:
                continue
        race = cls.get_race(name)
        charClass = cls.get_class()
        inventory = charClass.inventory
        stats = cls.get_stats(name)
        return cls(
            name,
            race,
            charClass,
            inventory,
            stats[0] + race.strMod,
            stats[1] + race.conMod,
            stats[2] + race.dexMod,
            stats[3] + race.wisMod,
            stats[4] + race.intMod,
            stats[5] + race.chaMod,)


    @classmethod
    def get_race(cls, name):
        raceDict = {'Human': races.human(), 'Elf': races.elf(), 'Dwarf': races.dwarf(),
                    'Gnome': races.gnome(), 'Tiefling': races.tiefling(), 'Half-Orc': races.halforc()}
        for choices in raceDict:
            print(raceDict[choices])
        while True:
            raceChoice = input("{}, please choose your race: ".format(name))
            raceChoice = raceChoice.strip()
            try:
                if raceChoice in raceDict:
                    break
                else:
                    continue
            except ValueError:
                continue
        return raceDict.get(raceChoice)


    @classmethod
    def get_class(cls):
        classDict = {'Wizard': classes.wizard(), }
        for choices in classDict:
            print(classDict[choices])
        classChoice = input("Please choose your Class: ")
        classChoice = classChoice.strip()
        while True:
            try:
                if classChoice in classDict:
                    break
                else:
                    continue
            except ValueError:
                continue
        return classDict.get(classChoice)


    @classmethod
    def get_stats(cls, name):
        rolledStats = []
        for i in range(1, 7):
            rolls = []
            for i in range(1, 5):
                roll = randint(1, 6)
                rolls.append(roll)
            rolledStats.append(sum(rolls) - min(rolls))
        assignedStats = []
        assignedStats.extend(cls.prompt_playerStats(name, rolledStats))
        return assignedStats


    def get_hp(self, charClass, con):
        conMod = self.player_mod(con)
        hp = charClass.hitDie + conMod
        for i in range(1, 4):
            hpRoll = randint(1, charClass.hitDie)
            hp += hpRoll + conMod
        return hp

    def get_spellMod(self, charClass):
        if charClass.name == 'Wizard':
            return self.player_mod(self.int)
        if charClass.name == 'Cleric':
            return self.player_mod(self.wis)
        if charClass.name == 'Ranger':
            return self.player_mod(self.wis)
        else:
            return None


    @classmethod
    def prompt_playerStats(cls, name, rolledStats):
        stats = ['STRENGTH', 'CONSTITUTION', 'DEXTERITY', 'WISDOM', 'INTELLIGENCE', 'CHARISMA']
        assignedStats = []
        rollSnapshot = rolledStats.copy()
        print("Welcome, {}! We're going to roll up some stats for you. Hope you're lucky!\n========".format(name))
        while len(rolledStats) != 0:
            for i in stats:
                print("Here are your available stats to choose from:\n{}\n========".format(rolledStats))
                while True:
                    try:
                        stat = int(input("Please choose the stat you would like to assign to your {} score: ".format(i)))
                        if stat in rolledStats:
                            rolledStats.remove(stat)
                            assignedStats.append(stat)
                            break
                        else:
                            continue
                    except ValueError:
                        continue
        print("========\nHere are your stats:\nSTR: {}\tCON: {}\tDEX: {}\nWIS: {}\tINT: {}\tCHA: {}\n========"\
              .format(assignedStats[0], assignedStats[1], assignedStats[2], assignedStats[3], assignedStats[4],
                      assignedStats[5]))
        while True:
            verify = input("Do you wish to continue with this stat assignment? (Y/N): ")
            if verify == "Y":
                break
            elif verify == "N":
                cls.prompt_playerStats(name, rollSnapshot)
                break
            else:
                continue
        return assignedStats


    def player_mod(self, stat):
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