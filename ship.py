from enum import Enum


class ShipClassHP(Enum):
    CARRIER = 5
    BATTLESHIP = 4
    CRUISER = 3
    SUBMARINE = 3
    DESTROYER = 2


class Orientation(Enum):
    NORTH = (0, 1)
    EAST = (1, 0)
    SOUTH = (0, -1)
    WEST = (-1, 0)


class Ship():
    def __init__(self, x, y, orientation, hp):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.hp = hp
        self.alive = True

    def get_hp(self):
        return self.hp

    def hit(self):
        self.hp -= 1

    def is_alive(self):
        return self.alive


class Carrier(Ship):
    def __init__(self, x, y, orientation):
        super(Carrier, self).__init__(
            x, y, orientation, ShipClassHP.CARRIER.value)


class Battleship(Ship):
    def __init__(self, x, y, orientation):
        super(Battleship, self).__init__(
            x, y, orientation, ShipClassHP.BATTLESHIP.value)


class Cuiser(Ship):
    def __init__(self, x, y, orientation):
        super(Cuiser, self).__init__(
            x, y, orientation, ShipClassHP.CRUISER.value)


class Submarine(Ship):
    def __init__(self, x, y, orientation):
        super(Submarine, self).__init__(
            x, y, orientation, ShipClassHP.SUBMARINE.value)


class Destroyer(Ship):
    def __init__(self, x, y, orientation):
        super(Destroyer, self).__init__(
            x, y, orientation, ShipClassHP.DESTROYER.value)
