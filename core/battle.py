from .entity import Entity
class Battle:
    def monster_turn(self, player, monster, attack_multipler, defense_multipler):
        if not monster.is_dead():
            name, damage, target, crit = monster.attack_target(player, attack_multipler, defense_multipler)
            attack_multipler = 1
            defense_multipler = 1
        return name, damage, target, crit
    def player_turn(self, player, monster, attack_multipler, defense_multipler, skill):
        if not skill == True:
            player.cd()
        name, damage, target, crit = player.attack_target(monster, attack_multipler, defense_multipler)
        attack_multipler = 1
        defense_multipler = 1
        return name, damage, target, crit
    def start(self, player, monster, attack_multipler, defense_multipler, skill):
        if not player.is_dead() and not monster.is_dead():
            self.player_turn(player, monster, attack_multipler, defense_multipler)
        if monster.is_dead():
            player.gain_exp(monster.exp_drop)
