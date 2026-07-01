import random
class Entity:
    def __init__(self, name, health, max_health, attack, defense, crit_rate, crit_damage, dodge_rate):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.defense = defense
        self.crit_rate = crit_rate
        self.crit_damage = crit_damage
        self.dodge_rate = dodge_rate
    def is_dead(self):
        return self.health <= 0
    def attack_target(self, target):
        damage = random.randint(self.attack - 4,self.attack + 4)
        if random.randint(1,100) <= self.crit_rate:
            damage = damage * self.crit_damage / 100
            print("Critical!!!")
            print(f"{self.name} dealt {round(min(damage, target.health), 0)} to {target.name}")
            target.take_damage(damage)
        elif random.randint(1,100) <= self.dodge_rate:
            damage = 0
            print(f"{self.name} attacked! ")
            print()
            print(f"{target.name} Dodged the attack!")
        else:
            damage = max(1, damage - target.defense)
            print(f"{self.name} dealt {round(min(damage, target.health), 0)} to {target.name}")
            target.take_damage(damage)
        print()
    def take_damage(self, damage):
        self.health -= damage
    def health_bar(self):
        length = 20

        filled = int(max(0,self.health) / self.max_health * length)
        empty = length - filled

        bar = "█" * filled + "-" * empty

        print(f"HP: [{bar}] {max(0,self.health)} / {self.max_health}")
    def combat_status(self):
        print(f"===== {self.name} =====")
        self.health_bar()