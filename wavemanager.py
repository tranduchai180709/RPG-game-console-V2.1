import random
from monster import Monster
from data import MONSTER_DATA
class wave:
    def __init__(self):
        self.wave = 0
        self.is_boss = False
        self.choice = 0
    def next_wave(self):
        self.wave += 1
        self.choice += self.wave - 5
        print(f"========= Wave {self.wave} =========")
        monster = self.create_monster()
        return monster
    def create_monster(self):
        monster_choice = random.randint(1,100)
        if 25 + 2 * self.choice < monster_choice:
            data = MONSTER_DATA["3"]
            monster = Monster(data["Name"], data["health"], data["max health"], data["ATK"], data["DEF"], data["EXP"], data["level"], data["crt rate"], data["crt dmg"], data["dodge rate"], data["lootable"], data["gold"])
            monster.level = max(1,random.randint(self.wave - 4, self.wave + 2))
        elif 10 + 2 * self.choice < monster_choice < 25 + 2 * self.choice:
            data = MONSTER_DATA["2"]
            monster = Monster(data["Name"], data["health"], data["max health"], data["ATK"], data["DEF"], data["EXP"], data["level"], data["crt rate"], data["crt dmg"], data["dodge rate"], data["lootable"], data["gold"])
            self.choice = max(0, self.wave - 5)
            self.choice = min(self.choice, 100)
            monster.level = max(1,random.randint(self.wave - 4, self.wave + 2))
        else:
            data = MONSTER_DATA["1"]
            monster = Monster(data["Name"], data["health"], data["max health"], data["ATK"], data["DEF"], data["EXP"], data["level"], data["crt rate"], data["crt dmg"], data["dodge rate"], data["lootable"], data["gold"])
            self.choice = max(0, self.wave - 10)
            self.choice = min(self.choice, 100)
            monster.level = max(1,random.randint(self.wave - 4, self.wave + 2))
        if self.wave % 10 == 0:
            self.is_boss = True
            monster.level = self.wave * 2
            monster.max_health = int(monster.max_health * random.uniform(self.wave / 5 , self.wave / 2))
            monster.health = monster.max_health
            monster.base_attack = int(monster.base_attack * random.uniform(self.wave / 2, self.wave / 5))
            monster.base_defense = int(monster.base_defense * random.uniform(self.wave, self.wave /5))
            monster.crit_rate += (monster.level / 5)
            monster.crit_damage += 2 * monster.level 
        else:
            self.is_boss = False
            monster.level = self.wave
            monster.crit_rate += (monster.level / 5)
            monster.crit_damage += 2 * monster.level 
            monster.exp_drop += monster.level * 10
            monster.base_attack += monster.level * 2
            monster.max_health += monster.level * 5
            monster.health = monster.max_health
            monster.base_defense += monster.level
            monster.exp_drop += monster.level * 20
            monster.dodge_rate = int (monster.dodge_rate + monster.level / 10)
            monster.gold += (monster.level - 1) * 10
        return monster
        