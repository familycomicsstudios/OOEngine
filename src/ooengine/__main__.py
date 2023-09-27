"""A sample game for OOEngine."""
## Start Imports
try:
    from main import Game, Room, Item
    import usernamelib
except ImportError:
    from .main import Game, Room, Item
    from . import usernamelib

## End Imports

## Start Game
game = Game()
## End Game

## Start Rooms
game.rooms.append(
    Room(
        [1],
        "You are in an empty room. There is a door to the north.",
        "Empty Room",
        {"n": 1},
        {"door": "The door is made out of white rock, with a obisidan door handle."},
    )
)
game.rooms.append(
    Room(
        [],
        "You are in another empty room. There is a door to the south and a " \
        "locked door to the north.",
        "Empty Room 2",
        {"s": 0},
    )
)

game.rooms[1].key = 1
game.rooms[1].locked = {"n": 2}
game.rooms[1].unlocked_desc = "You are in another empty room. " \
"There is a door to the south and a unlocked door to the north."


game.rooms.append(
    Room(
        [],
        "You are in third empty room. There is a door to the south.",
        "Empty Room 3",
        {"s": 1},
    )
)

## End Rooms

## Start Items
game.items.append(
    Item(
        "A small ball", "There is a ball here.", ["ball"], "A small red ball lies here."
    )
)
game.items.append(
    Item(
        "A small red key",
        "There is a small red key here.",
        ["key"],
        "A small red key lies here, with the end a open circle.",
    )
)
game.items[0].messages["take"] = '"Thanks for picking me up!", the ball says.'


def __item_smack(self, split):
    print(f'"No {split[0]}ing!" the ball says.')
    return self


game.items[0].smack = __item_smack
# Item commands: set command name as command of item.
# game.items[0].smack = __item_smack
## End Items

## Custom Commands
game = usernamelib.load_mod(game)
## End Custom Commands

## Start Game
game.start()
# pylint: disable=C0103
