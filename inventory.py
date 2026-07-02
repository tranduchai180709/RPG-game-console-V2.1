class Inventory:
    def __init__(self):
        self.equipment = []
        self.stackable_items = {}
        self.item = None
    def inventory_show(self, player):
        if not self.equipment and not self.stackable_items:
            print("Your inventory is empty")
            return 
        print("==== YOUR INVENTORY ====")
        print("Consumables")
        print("------------------------")
        if self.stackable_items:
            for name in self.stackable_items:
                print(f"{name} x{self.stackable_items[name]}")
        else:
            print("None")
        print()
        print("Equipment")
        print("------------------------")
        if self.equipment:
            for index, item in enumerate(self.equipment, start=1):
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
                self.stackable_items[item.name] += 1
            else:
                self.stackable_items[item.name] = 1
            print(f"You looted {item.name}.")
            print(f"Current amount: {self.stackable_items[item.name]}")
        else:
            self.equipment.append(item) 
            print(f"You looted {item.name}")
    def inventory_remove(self, item):
        if item.stackable:
            self.stackable_items[item.name] -= 1
            if(self.stackable_items[item.name] == 0):
                del self.stackable_items[item.name]
        else:
            self.equipment.remove(item)
    def inventory_choice(self, player):
        self.inventory_show(player)
        if self.equipment:
            choice = int(input("> ")) - 1
            if 0 <= choice < len(self.equipment):
                self.item = self.equipment[choice]
                player.equip(self.item)
        else:
            print("No equipment available.")