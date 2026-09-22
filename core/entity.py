import random
class Entity:
    def __init__(self, name, health, max_health, base_attack, base_defense, crit_rate, crit_damage, dodge_rate, gold):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.base_attack = base_attack
        self.base_defense = base_defense
        self.crit_rate = crit_rate
        self.crit_damage = crit_damage
        self.dodge_rate = dodge_rate
        self.gold = gold
    def is_dead(self):
        return self.health <= 0
    @property
    def attack(self):
        return self.base_attack
    @property
    def defense(self):
        return self.base_defense
    def attack_target(self, target, attack_multipler, defense_multipler):
        base_damage = random.randint(
            int(self.attack * attack_multipler) - 4,
            int(self.attack * attack_multipler) + 4
        )
        is_crit = random.randint(1, 100) <= self.crit_rate
        is_dodge = (not is_crit) and random.randint(1, 100) <= self.dodge_rate

        if is_dodge:
            return self.name, 0, target, False

        damage = base_damage
        if is_crit:
            damage = damage * self.crit_damage / 100
        damage = max(1, damage - target.defense * defense_multipler)
        damage = round(min(damage, target.health))
        target.take_damage(damage)
        return self.name, damage, target, is_crit
    def take_damage(self, damage):
        self.health -= damage
    def health_bar_data(self, length=20):
        if self.health <= 0:
            filled = 0
        else:
            filled = max(1, int(self.health / self.max_health * length))
        empty = length - filled
        return filled, empty, round(max(0, self.health)), self.max_health
