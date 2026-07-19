from entity import Entity
class Battle:
    def monster_turn(self, player, monster):
        if not monster.is_dead():
            monster.attack_target(player)
        player.combat_status()
    def player_turn(self, player, monster):
        player.attack_target(monster)
        monster.combat_status()
        self.monster_turn(player, monster)
    def start(self, player, monster):
        if not player.is_dead() and not monster.is_dead():
            self.player_turn(player, monster)
        if monster.is_dead():
            print(f"{player.name} killed {monster.name}!")
            player.gain_exp(monster.exp_drop)
