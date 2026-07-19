from entity import Entity
from items import Items
class Player(Entity):
    def to_dict(self):
        return {
        "name" : self.name,
        "health": self.health,
        "max_health": self.max_health,
        "base_attack": self.base_attack,
        "base_defense": self.base_defense,
        "exp": self.exp,
        "max_exp": self.max_exp,
        "level": self.level,
        "weapon": self.weapon.to_dict() if self.weapon else None,
        "armor": self.armor.to_dict() if self.armor else None,
        "accessory": self.accessory.to_dict() if self.accessory else None,
        "crit_rate": self.crit_rate,
        "crit_damage": self.crit_damage,
        "dodge_rate": self.dodge_rate,
        "gold": self.gold
        }
    @classmethod
    def from_dict(cls, data):
        player = cls(data["name"])
        print("PLAYER DATA:", data)
        player.health = data["health"]
        player.max_health = data["max_health"]
        player.base_attack = data["base_attack"]
        player.base_defense = data["base_defense"]
        player.exp = data["exp"]
        player.max_exp = data["max_exp"]
        player.level = data["level"]
        player.weapon = (
            Items.from_dict(data["weapon"])
            if data["weapon"] else None
        )
        player.armor = (
            Items.from_dict(data["armor"])
            if data["armor"] else None
        )
        player.accessory = (
            Items.from_dict(data["accessory"])
            if data["accessory"] else None
        )
        player.crit_rate = data["crit_rate"]
        player.crit_damage = data["crit_damage"]
        player.dodge_rate = data["dodge_rate"]
        player.gold = data["gold"]
        player.dodge_rate = data["dodge_rate"]
        return player
        
    def __init__(self, name):
        super().__init__(name, 50, 50, 10, 0, 10, 120, 20, 0)
        self.weapon = None
        self.armor = None
        self.accessory = None
        self.exp = 0
        self.level = 1
        self.max_exp = 50
    def level_up(self):
        self.level += 1

        self.max_health += 20
        self.health = self.max_health

        self.base_attack += 2
        self.base_defense += 1

        if self.level % 10 == 0:
            self.crit_rate += 1

        if self.level % 15 == 0:
            self.dodge_rate += 1

        if self.level % 20 == 0:
            self.crit_damage += 10

        self.exp -= self.max_exp
        self.max_exp += self.level * 10 + 50
        self.gold += 10
        print(f"Level up! Now level {self.level}")
    def gain_exp(self, drop_exp):
        self.exp += drop_exp
        while (self.exp >= self.max_exp):
            self.level_up()
    def status(self, player):
        print("-----------------------------------")
        print(f"===== Player {player.name} =====")
        print(f"Level   : {player.level}")
        print()
        player.health_bar()
        if player.weapon:
            print(f"ATK     : {player.attack} ({player.attack - player.weapon.value} + {player.weapon.value})")
        else:
            print(f"ATK     : {player.attack}")
        if player.armor:
            print(f"DEF     : {player.defense} ({player.defense - player.armor.value} + {player.armor.value})")
        else:
            print(f"DEF     : {player.defense}")
        print()
        print(f"Crit    : {player.crit_rate}%")
        print(f"Crit DMG: {player.crit_damage}%")
        print(f"Dodge   : {player.dodge_rate}%")
        print()
        print(f"EXP     : {player.exp} / {player.max_exp}")
        print("-----------------------------------")
        
    @property
    def attack(self):
        atk = self.base_attack
        if self.weapon:
            atk += self.weapon.value
        return atk
    @property
    def defense(self):
        defense = self.base_defense
        if self.armor:
            defense += self.armor.value
        return defense

    def equip(self, item):
        if item.item_type == "Sword":
            self.equip_sword(item)
        elif item.item_type == "Armor":
            self.equip_armor(item)
        elif item.item_type == "Accessory":
            self.equip_accessory(item)


    def equip_sword(self, item):
        if self.weapon is item:
            print(f"{self.name} is already using {item.name}")
            return

        self.unequip_sword()
        self.weapon = item
        print(f"{self.name} equipped {item.name}")

    def equip_armor(self, item):
        if self.armor is item:
            print(f"{self.name} is already wearing {item.name}")
            return

        self.unequip_armor()
        self.armor = item
        print(f"{self.name} equipped {item.name}")

    def equip_accessory(self, item):
        if self.accessory is item:
            print(f"{self.name} is already using {item.name}")
        self.unequip_accessory()
        self.accessory = item
        print(f"{self.name} equipped {item.name}")
        print()

    def unequip_sword(self):
        if self.weapon:
            print(f"{self.name} Unequipped {self.weapon.name}")
            self.weapon = None
            print()

    def unequip_armor(self):
        if self.armor:
            print(f"{self.name} Unequipped {self.armor.name}")
            self.armor = None
            print()

    def unequip_accessory(self):
        if self.accessory:
            print(f"{self.name} Unequipped {self.accessory.name}")
            self.accessory = None
            print()


    def run(self):
        print(f"{self.name} ran away!")
        return True
    def add_gold(self,golds):
        self.gold += golds
