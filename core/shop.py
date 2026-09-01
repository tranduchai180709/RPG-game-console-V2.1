from .data import ITEM_DATA
import random
from .lootsystem import loot_system
from colorama import Fore, Style
from .items import Items
class shops:
    def to_dict(self):
        return{
            "items": [item.to_dict() for item in self.stock]
        }
    @classmethod
    def from_dict(cls, data):
        shop = cls()
        shop.stock = [
            Items.from_dict(item_data)
            for item_data in data["items"]
        ]
        return shop
    def __init__(self):
        self.loot = loot_system()
    def shop_restock(self):
        equipment = [
    "Iron Armor",
    "Iron Sword",
    "Steel Sword",
    "Health Ring"
]
        self.stock = []
        self.stock.append(ITEM_DATA["Heal"])
        for i in range(2):
            item_name = random.choice(equipment)
            template = ITEM_DATA[item_name]
            item = Items(
                    template.name,
                    template.item_type,
                    template.value,
                    template.stackable,
                    template.rarity,
                    random.randint(template.base_price * template.rarity.multipler - 20, template.base_price * template.rarity.multipler - 20) 
                )
            self.loot.roll_rarity(item)
            item.base_price = random.randint(template.base_price * template.rarity.multipler + int(item.value * item.rarity.multipler) - 20, template.base_price * template.rarity.multipler + int(item.value * item.rarity.multipler) - 20)
            self.stock.append(item)
    def get_items(self):
        return self.stock
    def shop_choice_buy(self, player, inventory, choice):
            item = self.stock[choice - 1]
            if (player.gold >= item.base_price):
                player.gold -= item.base_price
                self.stock.remove(item)
                return item
            else:
                return None
    def shop_choice_sell(self, item, choice, player, inventory):
        item_price = int(item.base_price * 0.7)
        if choice == "1":
            inventory.inventory_remove(item)
            player.gold += item_price
            return item_price
        return None