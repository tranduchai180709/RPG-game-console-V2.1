from colorama import Fore, Style
from items import Items
class Inventory:
    def to_dict(self):
        return{
            "equipment": [item.to_dict() for item in self.equipment],
            "consumables": {
                item.name:count
                for item, count in self.stackable_items.items()
            }
        }
    @classmethod
    def from_dict(cls, data):
        inventory = cls()
        for item_data in data["equipment"]:
            item = Items.from_dict(item_data)
            inventory.equipment.append(item)
        for entry in data["consumables"]:
            item = Items.from_dict(entry["item"])
            inventory.stackable_items[item] = entry["count"]
        return inventory
    def __init__(self):
        self.equipment = []
        self.stackable_items = {}
    def inventory_show(self, player):
        self.display_item = []
        if not self.equipment and not self.stackable_items:
            print(f"Gold: {player.gold:,}")
            print()
            print("Your inventory is empty")
            print()
            return False
        print("==== YOUR INVENTORY ====")
        print()
        print(f"Gold: {player.gold:,}")
        print()
        print("Consumables")
        print("------------------------")
        self.i = 0
        if self.stackable_items:
            for index, item in enumerate(self.stackable_items, start=1):
                self.display_item.append(item)
                print(f"{index}: {item.name} x{self.stackable_items[item]}")
                self.i += 1
        else:
            print("None")
        print()
        print("Equipment")
        print("------------------------")
        if self.equipment:
            for index, item in enumerate(self.equipment, start= self.i + 1):
                self.display_item.append(item)
                equipped = "[ ]"

                if player.weapon is item:
                    equipped = "[W]"

                elif player.armor is item:
                    equipped = "[A]"

                elif player.accessory is item:
                    equipped = "[R]"
                print(
        f"{equipped}"
        f"{index:>2}. "
        f"{item.name:<15} "
        f"{item.value:+4} "
        f"{item.rarity.color}[{item.rarity.name}]{Style.RESET_ALL}"
    )
        else:
            print("None")
        print()
        print("0: cancel")
        print()
        return True
    def inventory_add(self, item):
        if item.stackable:
            for old_item in self.stackable_items:
                if old_item.name == item.name:
                    self.stackable_items[old_item] += 1
                    print(f"{old_item.name} amount: {self.stackable_items[old_item]}")
                    print()
                    return
            self.stackable_items[item] = 1
            print(f"{item.name} amount: 1")
            print()
        else:
            self.equipment.append(item) 
    def inventory_remove(self, item):
        if item.stackable:
            self.stackable_items[item] -= 1
            if(self.stackable_items[item] == 0):
                del self.stackable_items[item]
        else:
            self.equipment.remove(item)
    def inventory_choice(self):
        choice = int(input("> ")) - 1
        if 0 <= choice < len(self.display_item):
            return self.display_item[choice]
        elif choice == -1:
            return
