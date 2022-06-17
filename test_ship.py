import ship


def test_carrier():
    carrier = ship.Carrier(0, 0, ship.Orientation.NORTH)
    assert carrier.get_hp() == 5


def test_battleship():
    battleship = ship.Battleship(0, 0, ship.Orientation.NORTH)
    assert battleship.get_hp() == 4


def test_cruiser():
    cruiser = ship.Cuiser(0, 0, ship.Orientation.NORTH)
    assert cruiser.get_hp() == 3


def test_submarine():
    submarine = ship.Submarine(0, 0, ship.Orientation.NORTH)
    assert submarine.get_hp() == 3


def test_destroyer():
    destroyer = ship.Destroyer(0, 0, ship.Orientation.NORTH)
    assert destroyer.get_hp() == 2
