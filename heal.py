from player import Player
from inventory import Inventory
class Heal:
    def __init__(self):
        self.item_check = Inventory()
    def heal(self, player, item):
        if self.item_check.stackable_items_check():
            if item.value <= player.max_health - player.health:
                player.health += item.value
                print(f"{player.name} healed {item.value} hp")
                player.combat_status()
                print()
            else:
                item.value = player.max_health - player.health
                player.health = player.max_health
                print(f"{player.name} healed {item.value} hp")
                player.combat_status()
                print()
        else:
            print("You dont have heal item")
            return