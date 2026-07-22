from entity import Entity
class Battle:
    def monster_turn(self, player, monster, attack_multipler, defense_multipler):
        if not monster.is_dead():
            monster.attack_target(player, attack_multipler, defense_multipler)
            attack_multipler = 1
            defense_multipler = 1
        player.combat_status()
    def player_turn(self, player, monster, attack_multipler, defense_multipler):
        player.attack_target(monster, attack_multipler, defense_multipler)
        attack_multipler = 1
        monster.combat_status()
        self.monster_turn(player, monster, attack_multipler, defense_multipler)
        defense_multipler = 1
    def start(self, player, monster, attack_multipler, defense_multipler):
        if not player.is_dead() and not monster.is_dead():
            self.player_turn(player, monster, attack_multipler, defense_multipler)
        if monster.is_dead():
            print(f"{player.name} killed {monster.name}!")
            player.gain_exp(monster.exp_drop)
