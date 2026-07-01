from player import Player
class Items:
    def __init__(self, name, item_type, value, stackable):
        self.name = name
        self.item_type = item_type
        self.value = value
        self.stackable = stackable