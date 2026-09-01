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
        atk = self.base_attack
        return self.base_attack
    @property
    def defense(self):
        defense = self.base_defense
        return self.base_defense
    def attack_target(self, target, attack_multipler, defense_multipler):
        damage = random.randint(int(self.attack * attack_multipler) - 4,int(self.attack *attack_multipler) + 4)
        if random.randint(1,100) <= self.crit_rate:
            damage = damage * self.crit_damage / 100
            damage = max(1, damage - target.defense * defense_multipler)
            damage = round(min(damage, target.health))
            target.take_damage(damage)
            return self.name, damage, target, True

        elif random.randint(1,100) <= self.dodge_rate:
            damage = 0
            return self.name, damage, target, False

        else:
            damage = max(1, damage - target.defense)
            damage = round(min(damage, target.health))
            target.take_damage(damage)
            return self.name, damage, target, False
        print()
    def take_damage(self, damage):
        self.health -= damage
    def health_bar(self):
        length = 20
        if self.health <= 0:
            filled = 0
        else:
            filled = max(1,int(self.health / self.max_health * length))
        empty = length - filled

        bar = "█" * filled + "-" * empty

        print(f"HP: [{bar}] {round(max(0,self.health))} / {self.max_health}")