from entity import Entity
from monster import Monster
class Battle:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster
    def monster_turn(self):
        if not self.monster.is_dead():
            self.monster.attack_target(self.player)
        self.player.combat_status()
    def player_turn(self):
        self.player.attack_target(self.monster)
        self.monster.combat_status()
        self.monster_turn()
    def start(self):
        if not self.player.is_dead() and not self.monster.is_dead():
            self.player_turn()
        if self.monster.is_dead():
            print(f"{self.player.name} killed {self.monster.name}!")
            self.player.gain_exp(self.monster.exp_drop)
