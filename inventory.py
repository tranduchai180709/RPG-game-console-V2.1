class Inventory:
    def __init__(self):
        self.equipment = []
        self.stackable_items = {}
        self.item = None
    def inventory_show(self, player):
        self.display_item = []
        if not self.equipment and not self.stackable_items:
            print("Your inventory is empty")
            return 
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
                print(f"{index}. {item.name}{equipped}")
        else:
            print("None")
        print()
    def inventory_add(self, item):
        if item.stackable:
            if item.name in self.stackable_items:
                self.stackable_items[item] += 1
            else:
                self.stackable_items[item] = 1
            print(f"You looted {item.name}.")
            print(f"Current amount: {self.stackable_items[item]}")
        else:
            self.equipment.append(item) 
            print(f"You looted {item.name}")
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
