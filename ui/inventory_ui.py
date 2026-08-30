from colorama import Fore, Style
class InventoryUI:
    def show_inventory(self, inventory, player):
        equipment, stackable = inventory.get_inventory_item()
        self.display_item = []
        if not equipment and not stackable:
            print(f"Gold: {player.gold:,}")
            print()
            print("Your inventory is empty")
            print()
            return False
        print("==== YOUR INVENTORY ====")
        print()
        print(f"Gold: {player.gold:,}")
        print()
        self.i = 0
        if stackable:
            print("Consumables")
            print("------------------------")
            for index, item in enumerate(stackable, start=1):
                self.display_item.append(item)
                print(f"{index}: {item.name} x{stackable[item]}")
                self.i += 1
            print("------------------------")
        if equipment:
            print()
            print("Equipment")
            for index, item in enumerate(equipment, start= self.i + 1):
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
    def inventory_choice_ui(self):
        return int(input("> ")) - 1