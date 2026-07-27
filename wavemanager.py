import random
from monster import Monster
from data import MONSTER_DATA
class wave:
    def to_dict(self):
        return {
            "Wave": self.wave,
            "difficulty": self.choice,
            "monster": {
            "name" : self.monster.name,
            "health": self.monster.health,
            "max_health": self.monster.max_health,
            "base_attack": self.monster.base_attack,
            "base_defense": self.monster.base_defense,
            "exp_drop": self.monster.exp_drop,
            "level": self.monster.level,
            "crit_rate": self.monster.crit_rate,
            "crit_damage": self.monster.crit_damage,
            "dodge_rate": self.monster.dodge_rate,
            "lootable": self.monster.lootable,
            "gold_drop": self.monster.gold,
            "is_boss": self.is_boss if self.is_boss else None
            }
        }
    @classmethod
    def from_dict(cls, data):
        from data import MONSTER_DATA
        waves = cls()
        waves.wave = data["Wave"]
        waves.choice = data["difficulty"]
        waves.monster = Monster.from_dict(data["monster"])
        return waves
    def __init__(self):
        self.wave = 0
        self.is_boss = False
        self.choice = 0
    def next_wave(self):
        self.wave += 1
        self.choice += self.wave - 5
        self.choice = max(0, self.choice)
        print(f"========= Wave {self.wave} =========")
        self.monster = self.create_monster()
        return self.monster
    def create_monster(self):
        monster_choice = random.randint(1,100)
        if self.wave > 5:
            if 25 + 2 * self.choice < monster_choice:
                data = MONSTER_DATA["Slime"]
                monster = Monster(data["Name"], data["health"], data["max health"], data["ATK"], data["DEF"], data["EXP"], data["level"], data["crt rate"], data["crt dmg"], data["dodge rate"], data["lootable"], data["gold"])
                monster.level = max(1,random.randint(self.wave - 4, self.wave + 2))
            elif 10 + 2 * self.choice < monster_choice < 25 + 2 * self.choice:
                data = MONSTER_DATA["Goblin"]
                monster = Monster(data["Name"], data["health"], data["max health"], data["ATK"], data["DEF"], data["EXP"], data["level"], data["crt rate"], data["crt dmg"], data["dodge rate"], data["lootable"], data["gold"])
                self.choice = max(0, self.wave - 5)
                self.choice = min(self.choice, 100)
                monster.level = max(1,random.randint(self.wave - 4, self.wave + 2))
            else:
                data = MONSTER_DATA["Dark knight"]
                monster = Monster(data["Name"], data["health"], data["max health"], data["ATK"], data["DEF"], data["EXP"], data["level"], data["crt rate"], data["crt dmg"], data["dodge rate"], data["lootable"], data["gold"])
                self.choice = max(0, self.wave - 10)
                self.choice = min(self.choice, 100)
                monster.level = max(1,random.randint(self.wave - 4, self.wave + 2))
            ms = self.scale_monster(monster)
            return ms
        elif self.wave <= 5:
            data = MONSTER_DATA["Slime"]
            monster = Monster(data["Name"], data["health"], data["max health"], data["ATK"], data["DEF"], data["EXP"], data["level"], data["crt rate"], data["crt dmg"], data["dodge rate"], data["lootable"], data["gold"])
            monster.level = 1
            ms = self.scale_monster(monster)
            return ms
        if self.wave % 10 == 0:
            ms = self.scale_monster_boss(monster)
            return ms
    def scale_monster(self, monster):
            level_multipler = monster.level - 1
            monster.crit_rate += (level_multipler / 5)
            monster.crit_damage += 2 * level_multipler 
            monster.exp_drop += level_multipler * 10
            monster.base_attack += level_multipler * 2
            monster.max_health += level_multipler * 5
            monster.health = monster.max_health
            monster.base_defense += int(level_multipler / 2)
            monster.dodge_rate = int (monster.dodge_rate + level_multipler / 10)
            monster.gold += level_multipler * 10
            return monster
    def scale_monster_boss(self, monster):
            monster.level += 5
            monster.max_health = int(monster.max_health * random.uniform(self.wave / 5 , self.wave / 2))
            monster.health = monster.max_health
            monster.base_attack = int(monster.base_attack * random.uniform(self.wave / 2, self.wave / 5))
            monster.base_defense = int(monster.base_defense * random.uniform(self.wave, self.wave /5))
            monster.crit_rate += (monster.level / 5)
            monster.crit_damage += 2 * monster.level 
            return monster