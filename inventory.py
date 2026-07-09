from colorama import Fore, Style
class Inventory:
    def __init__(self):
        self.equipment = []
        self.stackable_items = {}
    def inventory_show(self, player):
        self.display_item = []
        if not self.equipment and not self.stackable_items:
            print("Your inventory is empty")
            return False
        print("==== YOUR INVENTORY ====")
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
                equipped = ""

                if player.weapon is item:
                    equipped = " [E]"

                elif player.armor is item:
                    equipped = " [E]"

                elif player.accessory is item:
                    equipped = " [E]"
                print(f"{equipped} {index}. {item.name} +{item.value} {item.rarity.color}[{item.rarity.name}] {Style.RESET_ALL}")
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
                    print(f"You looted {item.name}.")
                    print(f"Current amount: {self.stackable_items[old_item]}")
                    print()
                    return
            self.stackable_items[item] = 1
            print(f"You looted {item.name}.")
            print(f"Current amount: 1")
            print()
        else:
            self.equipment.append(item) 
            print(f"You looted {item.name}")
            print()
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
