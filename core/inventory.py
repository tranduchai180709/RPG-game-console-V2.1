from .items import Items
from .data import ITEM_DATA
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
        for item_name, count in data["consumables"].items():
            item = ITEM_DATA[item_name]
            inventory.stackable_items[item] = count
        return inventory
    def __init__(self):
        self.equipment = []
        self.stackable_items = {}
    def get_inventory_item(self):
        return self.equipment, self.stackable_items
    def inventory_check(self):
        self.display_item = []
        self.i = 0

        if not self.equipment and not self.stackable_items:
            return False
        
        if self.stackable_items:
            for index, item in enumerate(self.stackable_items, start=1):
                self.display_item.append(item)
                self.i += 1
        
        if self.equipment:
            for index, item in enumerate(self.equipment, start= self.i + 1):
                self.display_item.append(item)
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
    def inventory_choice(self, choice):
        if 0 <= choice < len(self.display_item):
            return self.display_item[choice]
        elif choice == -1:
            return
