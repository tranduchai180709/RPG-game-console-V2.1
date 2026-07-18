from data import ITEM_DATA
import random
from lootsystem import loot_system
from colorama import Fore, Style
from items import Items
class shops:
    def __init__(self):
        self.loot = loot_system()
    def shop_menu(self, player):
        print("====== BLACKSMITH =====")
        print()
        print(f"{player.gold:,} G")
        print()
        for i, item in enumerate(self.stock, start=1):
            if item.stackable == True:
                print(f"{i}: {item.name} {item.base_price} G")
            else:
                print(f"{i}: {item.name} +{item.value} {item.rarity.color}[{item.rarity.name}] {Style.RESET_ALL} {item.base_price} G")
        print()
        print("0: Exit")
        print()
    def shop_restock(self):
        equipment = [
    "Iron Armor",
    "Iron Sword",
    "Steel Sword"
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
            self.stock.append(item)
    def shop_choice(self, player):
        while True:
            print("1: Buy")
            print("2: Sell")
            print("0: Exit")
            print()
            player_choice = input("> ")
            if(player_choice == "1"):
                if self.stock:
                    self.shop_menu(player)
                else:
                    print("The shop is sold out.")
                    print()
                    print("0: Exit")
                    print()
                choice = int(input("> "))
                if choice == 0:
                    return    
                elif choice == -1:
                    self.shop_choice(player)
                elif choice not in [1, 2, 3]:
                    print("Invaild command")
                    continue
                item = self.stock[choice - 1]
                if (player.gold >= item.base_price):
                    player.gold -= item.base_price
                    print()
                    print(f"You bought {item.name}.")
                    self.stock.remove(item)
                    print()
                    return item
                else:
                    print()
                    print(f"you dont have enough gold for {item.name}")
                    print()
                    return None            
            elif(player_choice == "2"):
                return None
            elif(player_choice == "0"):
                return None
            else:
                print("Invaild command")
                print()
                self.shop_choice(player)