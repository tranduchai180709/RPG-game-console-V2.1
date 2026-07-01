from player import Player
class Heal:
    def heal(self, player):
        if player.heal_health <= player.max_health - player.health:
            player.health += player.heal_health
            print(f"{player.name} healed {player.heal_health} hp")
            player.combat_status()
            print()
        else:
            player.heal_health - player.max_health - player.health
            player.health = player.max_health
            print(f"{player.name} healed {player.heal_health} hp")
            player.combat_status()
            print()