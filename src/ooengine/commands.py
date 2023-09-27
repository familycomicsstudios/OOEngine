"""Basic commands for OOEngine."""


class NoBallsError(Exception):
    """A sample error for no balls (used for checking if there is a ball in the room)."""


def get_items_in_room(self, room):
    """Get all items in the room given as a array of objects."""
    items = self.rooms[room].items
    new_items = []
    for item in items:
        new_items.append(self.items[item].__dict__)
    return new_items


def get_items_in_room_names(self, room):
    """Get the short names of all items in a room."""
    items = self.rooms[room].items
    new_items = {}
    for item in items:
        new_items[self.items[item].short[0]] = item
    return new_items


def get_items_in_inventory_names(self, room):
    """Get the short names of all items in the inventory."""
    items = room
    new_items = {}
    for item in items:
        new_items[self.items[item].short[0]] = item
    return new_items


def look(split, self):
    """Look at objects in the room. Called from main.py."""
    try:
        if len(split) == 1:
            print(self.rooms[self.player.room].description)
            for item in self.rooms[self.player.room].items:
                print(self.items[item].on_floor)
        elif len(split) == 2:
            giirn = get_items_in_room_names(self, self.player.room)
            if split[1] in giirn:
                print(self.items[giirn[split[1]]].long)
            else:
                print(self.rooms[self.player.room].looks[split[1]])
        else:
            print("Usage: look [where]")
    except IndexError:
        print("You can't look at that.")


def grab(split, self):
    """Grab an item in the room. Called from main.py."""
    try:
        if len(split) == 2:
            giirn = get_items_in_room_names(self, self.player.room)
            if split[1] in giirn:
                self.player.inventory.append(giirn[split[1]])
                self.rooms[self.player.room].items.remove(giirn[split[1]])
                self.items[self.player.inventory[giirn[split[1]]]].take()
                print("Okay.")
            else:
                print("You can't take that.")
        else:
            print("Usage: take [item]")
    except IndexError:
        print("You can't take that.")
    return self


def drop(split, self):
    """Drop an item in inventory. Called from main.py."""
    try:
        if len(split) == 2:
            giirn = get_items_in_inventory_names(self, self.player.inventory)
            if split[1] in giirn:
                self.player.inventory.remove(giirn[split[1]])
                self.rooms[self.player.room].items.append(giirn[split[1]])
                self.items[self.rooms[self.player.room].items[giirn[split[1]]]].drop()
                print("Okay.")
            else:
                print("You can't drop that.")
        else:
            print("Usage: drop [item]")
    except IndexError:
        print("You can't drop that.")
    return self


def eat(split, self):
    """Eat an item in your inventory. Called from main.py."""
    try:
        if len(split) == 2:
            giirn = get_items_in_inventory_names(self, self.player.inventory)
            if (
                split[1] in giirn
                and self.items[giirn[split[1]]].messages["eat"] is not None
            ):
                self.items[self.player.inventory[giirn[split[1]]]].eat()
                self.player.inventory.remove(giirn[split[1]])
                print("Okay.")
            else:
                print("You can't eat that.")
        else:
            print("Usage: eat [item]")
    except IndexError:
        print("You can't eat that.")
    return self


def inventory(self, split):
    """Print the player's inventory. Called from main.py."""
    if split is None:
        raise NoBallsError
    print("You have:")
    if len(self.player.inventory) == 0:
        print("Nothing!")
    for item in self.player.inventory:
        print(self.items[item].name)


# pylint: disable=C0103
