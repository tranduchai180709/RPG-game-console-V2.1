from player import Player
from inventory import Inventory
class Heal:
    def __init__(self):
        self.item_check = Inventory()
    def heal(self, player, item):
        if player.max_health == player.health:
            print("Your health already full.")
            print()
            return False
        elif item.value <= player.max_health - player.health:
            player.health += item.value
            print(f"{player.name} healed {item.value} hp")
            player.combat_status()
            print()
        elif item.value > player.max_health - player.health:
            heal_hp = item.value
            heal_hp = player.max_health - player.health
            player.health = player.max_health
            print(f"{player.name} healed {heal_hp} hp")
            player.combat_status()
            print()
        return True