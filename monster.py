from entity import Entity
import random
class Monster(Entity):
    @classmethod
    def from_dict(cls, data):
        from data import MONSTER_DATA
        template = MONSTER_DATA[data["name"]]
        monster = Monster(
            template["Name"],
            template["health"],
            template["max health"],
            template["ATK"],
            template["DEF"],
            template["EXP"],
            template["level"],
            template["crt rate"],
            template["crt dmg"],
            template["dodge rate"],
            template["lootable"],
            template["gold"]
        )
        monster.name = data["name"]
        monster.health = data["health"]
        monster.max_health = data["max_health"]
        monster.base_attack = data["base_attack"]
        monster.base_defense = data["base_defense"]
        monster.exp_drop = data["exp_drop"]
        monster.level = data["level"]
        monster.crit_rate = data["crit_rate"]
        monster.crit_damage = data["crit_damage"]
        monster.dodge_rate = data["dodge_rate"]
        monster.lootable = data["lootable"]
        monster.gold = data["gold_drop"]
        return monster
    def __init__(self, name, health, max_health, base_attack, base_defense, exp_drop,level, crit_rate, crit_damage, dodge_rate, lootable, gold):
        super().__init__(name, health, max_health, base_attack, base_defense, crit_rate, crit_damage, dodge_rate, gold)
        self.level = level
        self.exp_drop = exp_drop
        self.base_attack = base_attack + (self.level - 1) * 2
        self.max_health = health + (self.level - 1) * 5
        self.health = self.max_health
        self.base_defense = base_defense + (self.level - 1)
        self.exp_drop = exp_drop + (self.level - 1) * 20
        self.crit_rate = crit_rate
        self.crit_damage = crit_damage
        self.dodge_rate = dodge_rate
        self.lootable = lootable
        self.gold = gold + (self.level - 1) * 10
    def status(self, full=True):
        print("-----------------------------------")
        print(f"===== {self.name} =====")
        if(full == True):
            print(f"Level   : {self.level}")
            print()
            self.health_bar()
            print(f"ATK     : {self.attack}")
            print(f"DEF     : {self.defense}")
            print()
            print(f"Crit    : {self.crit_rate}%")
            print(f"Crit DMG: {self.crit_damage}%")
            print(f"Dodge   : {self.dodge_rate}%")
        else:
            print(f"Level   : {self.level}")
            print()
            self.health_bar()
            print(f"ATK     : {self.attack}")
            print(f"DEF     : {self.defense}")
        print("-----------------------------------")
    def drop_gold(self):
        return random.randint(self.gold - 5, self.gold + 5 )