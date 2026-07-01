from player import Player
from inventory import Inventory
class Heal:
    def heal(self, player, item):
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