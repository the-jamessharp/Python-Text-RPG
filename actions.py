import player

class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.name = name
        self.hotkey = hotkey.upper()
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)


class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=player.Player.move_north, name='Move north', hotkey='N')


class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=player.Player.move_south, name='Move south', hotkey='S')


class MoveEast(Action):
    def __init__(self):
        super().__init__(method=player.Player.move_east, name='Move east', hotkey='E')


class MoveWest(Action):
    def __init__(self):
        super().__init__(method=player.Player.move_west, name='Move west', hotkey='W')


class ViewInventory(Action):
    def __init__(self):
        super().__init__(method=player.Player.print_inventory, name='View inventory', hotkey='I')


class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=player.Player.attack, name='Attack', hotkey='A', enemy=enemy)


class Flee(Action):
    def __init__(self, tile):
        super().__init__(method=player.Player.flee, name="Flee", hotkey="F", tile=tile)


class ChangeWeapon(Action):
    def __init__(self):
        super().__init__(method=player.Player.changeWeapon, name="Change Weapon", hotkey="C")