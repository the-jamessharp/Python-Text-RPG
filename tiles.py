from random import randint
import items, enemies, npcs, actions, world

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        return moves


class Tavern(MapTile):
    def intro_text(self):
        return """
        This is a test to see if the program is running properly
        """

    def modify_player(self, player):
        # Room as no actions for player
        pass


class LootRoom(MapTile):
    def __init__(self, x, y, item, key):
        self.item = item
        self.key = key
        super().__init__(x, y)

    def add_loot(self, player, key):
        listofGlobals = globals()
        try:
            listofGlobals[key]
        except KeyError:
            listofGlobals.update({key: False})
        if not listofGlobals[key]:
            player.inventory.append(self.item)
            listofGlobals.update({key: True})

    def modify_player(self, player):
        self.add_loot(player, self.key)


class CombatRoom(MapTile):
    def __init__(self, x, y, enemy, **kwargs):
        self.enemy = enemy
        self.kwargs = kwargs
        super().__init__(x, y)

    def modify_player(self, player):
        if self.enemy.is_alive():
            initDict, initOrder = self.initiative(player, self.enemy)
            self.combat(initDict, initOrder, player)

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy), actions.ChangeWeapon()]
        else:
            return self.adjacent_moves()

    def initiative(self, the_player, *args):
        combatants = [the_player]
        for arg in args:
            combatants.append(arg)
        initDict = {}
        initOrder = []
        for mob in combatants:
            initRoll = randint(1, 20)
            if initRoll in initOrder:
                initRoll -= 1
            initDict.update({initRoll: mob})
            initOrder.append(initRoll)
        initOrder.sort(reverse=True)
        initStr = 'The Initiative Order is:'
        for x in range(0, len(initOrder)):
            initStr += '\n' + str(x) + '. ' + initDict.get(initOrder[x]).name + ' (' + str(initOrder[x]) + ')'
        print(initStr + '\n')
        return initDict, initOrder

    def combat(self, init, order, the_player):
        combatActive = True
        while combatActive:
            for turn in order:
                creature = init.get(turn)
                if isinstance(creature, enemies.Enemy):
                    print("Enemy turn")
                    enemyAtk = randint(1, 20) + self.enemy.atkMod
                    damage = 0
                    if enemyAtk >= the_player.ac:
                        print("The {} hit you with a {}!".format(self.enemy.name, enemyAtk))
                        for x in range(0, self.enemy.diceNum):
                            damage += randint(1, self.enemy.diceSide)
                        if enemyAtk == 20:
                            print("The {} scored a critical hit!".format(self.enemy.name))
                            damage *= 2
                        the_player.hp -= damage + self.enemy.dmgMod
                        print("The {} does {} damage. You have {} HP remaining.\n"
                              .format(self.enemy.name, damage, the_player.hp))
                    else:
                        print("The {} misses you with a {}!".format(self.enemy.name, enemyAtk))
                    if not the_player.is_alive():
                        combatActive = False
                        break
                else:
                    available_actions = self.available_actions()
                    for action in available_actions:
                        print(action)
                    action_input = input('Action: ').upper()
                    while True:
                        for action in available_actions:
                            if action_input == action.hotkey:
                                if action_input.upper() == 'F':
                                    enemyAtk = randint(1, 20) + self.enemy.atkMod
                                    damage = 0
                                    if enemyAtk >= the_player.ac:
                                        for x in range(1, self.enemy.diceNum):
                                            damage += randint(1, self.enemy.diceSide)
                                        if enemyAtk == 20:
                                            print("The {} scored a critical hit!".format(self.enemy.name))
                                            damage *= 2
                                        the_player.hp -= damage + self.enemy.dmgMod
                                        print("The {} does {} damage as you flee!. You have {} HP remaining.\n"
                                              .format(self.enemy.name, damage, the_player.hp))
                                    combatActive = False
                                the_player.do_action(action, **action.kwargs)
                                break
                            else:
                                continue
                        break
                    if not self.enemy.is_alive():
                        combatActive = False
                        break
                    if not combatActive:
                        break


class EmptyRoom(MapTile):
    def intro_text(self):
        return """
        There doesn't seem to be anything here...
        """

    def modify_player(self, player):
        # No actions
        pass

class BanditRoom(CombatRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.bandit())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            There is a bandit here.
            """
        else:
            return """
            The bandit is dead.
            """


class WolfRoom(CombatRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.wolf())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            There is a wolf here.
            """
        else:
            return """
            The wolf is dead.
            """


class SwordRoom(LootRoom):
    def __init__(self, x, y,):
        super().__init__(x, y, items.shortSword(), key='swordLoot')

    def intro_text(self):
        listofGlobals = globals()
        try:
            listofGlobals['swordLoot']
        except KeyError:
            return """
            You find a short sword on the ground.
            """
        else:
            return """
            There doesn't seem to be anything here
            """


class VictoryRoom(MapTile):
    def intro_text(self):
        return """
        You've won!
        """

    def modify_player(self, player):
        player.victory = True