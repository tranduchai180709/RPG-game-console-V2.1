from entity import Entity
class Monster(Entity):
    def __init__(self, name, health, max_health, base_attack, base_defense, exp_drop,level, crit_rate, crit_damage, dodge_rate, lootable):
        super().__init__(name, health, max_health, base_attack, base_defense, crit_rate, crit_damage, dodge_rate)
        self.level = level
        self.exp_drop = exp_drop
        self.base_attack = base_attack + level * 2
        self.max_health = health + level * 5
        self.health = self.max_health
        self.base_defense = base_defense + level
        self.exp_drop = exp_drop + level * 20
        self.crit_rate = crit_rate
        self.crit_damage = crit_damage
        self.dodge_rate = dodge_rate
        self.lootable = lootable
    def status(self, full=True):
        print("-----------------------------------")
        print(f"===== {self.name} =====")
        if(full == True):
            print(f"Level   : {self.level}")
            print()
            print(f"Health  : {self.health_bar()}")
            print(f"ATK     : {self.attack}")
            print(f"DEF     : {self.defense}")
            print()
            print(f"Crit    : {self.crit_rate}")
            print(f"Crit DMG: {self.crit_damage}")
            print(f"Dodge   : {self.dodge_rate}")
        else:
            self.health_bar()
            print(f"ATK     : {self.attack}")
            print(f"DEF     : {self.defense}")
        print("-----------------------------------")