from .player import Player
from .inventory import Inventory
class Heal:
    def __init__(self):
        self.item_check = Inventory()
    def heal(self, player, item):
        if player.max_health == player.health:
            return None
        elif item.value <= player.max_health - player.health:
            player.health += item.value
            return item.value
        elif item.value > player.max_health - player.health:
            heal_hp = player.max_health - player.health
            player.health = player.max_health
            return heal_hp