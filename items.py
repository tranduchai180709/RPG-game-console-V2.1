from rarity import Rarity, RARITY_DATA
class Items:
    def to_dict(self):
        return {
            "name": self.name,
            "value": self.value,
            "rarity": self.rarity.name
        }
    @classmethod
    def from_dict(cls, data):
        from data import ITEM_DATA
        template = ITEM_DATA[data["name"]]
        item = Items(
            data["name"],
            template.item_type,
            data["value"],
            template.stackable,
            RARITY_DATA[data["rarity"]],
            template.base_price
        )
        return item
    def __init__(self, name, item_type, value, stackable, rarity, base_price):
        self.name = name
        self.item_type = item_type
        self.value = value
        self.stackable = stackable
        self.rarity = rarity
        self.base_price = base_price