class Inventory:
    def __init__(self):
        self.equipment = []
        self.stackable_items = {}
    def inventory_show(self):
        if not self.equipment and not self.stackable_items:
            print("Your inventory is empty")
            return 
        print("==== YOUR INVENTORY ====")
        if self.stackable_items:
                print("Consumables")
                print("------------------------")
        for name in self.stackable_items:
            print(f"{name} x{self.stackable_items[name]}")
        print()
        if self.equipment:
            print("Equipment")
            print("------------------------")
        for i in self.equipment:
                print(i.name)
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