from data import ITEM_DATA
import random
from lootsystem import loot_system
from colorama import Fore, Style
from inventory import Inventory
from items import Items
class shops:
    def shop_menu(self):
        self.loot = loot_system()
        self.inventory = Inventory()
        self.shop_restock()
        print("====== BLACKSMITH =====")
        print()
        for i, item in enumerate(self.stock, start=0):
            if item.item_type == "None":
                print(f"{i + 1}: {item.name}")
            elif not item.item_type == "Heal":
                print(f"{i + 1}: {item.name} + {item.value} {item.rarity.color}[{item.rarity.name}] {Style.RESET_ALL}")
            else:
                print(f"{i + 1}: {item.name} + {item.value}")
        choice = int(input("> "))
        self.inventory.inventory_add(self.stock[choice - 1])
        self.stock[choice - 1] = ITEM_DATA["None"]
        print()
    def shop_restock(self):
        self.stock = []
        self.stock.append(ITEM_DATA["Heal"])
        self.stock.append(ITEM_DATA["Heal"])
        for i in range(3):
            list = random.randint(1, 3)
            if list == 1:
                template = ITEM_DATA["Iron Armor"]
                item = Items(
                    template.name,
                    template.item_type,
                    template.value,
                    template.stackable,
                    template.rarity
                )
                self.loot.roll_rarity(item)
                self.stock.append(item)
            elif list == 2:
                template = ITEM_DATA["Iron Sword"]
                item = Items(
                    template.name,
                    template.item_type,
                    template.value,
                    template.stackable,
                    template.rarity
                )
                self.loot.roll_rarity(item)
                self.stock.append(item)
            elif  list == 3:
                template = ITEM_DATA["Steel Sword"]
                item = Items(
                    template.name,
                    template.item_type,
                    template.value,
                    template.stackable,
                    template.rarity
                )
                self.loot.roll_rarity(item)
                self.stock.append(item)

