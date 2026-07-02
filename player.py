from entity import Entity
class Player(Entity):
    def __init__(self, name):
        super().__init__(name, 50, 50, 10, 0, 10, 120, 20)
        self.weapon = None
        self.armor = None
        self.accessory = None
        self.base_attack = 10
        self.exp = 0
        self.level = 1
        self.max_exp = 50
        self.heal_health = 10
        self.max_health = 50
        self.crit_rate = 10
        self.crit_damage = 120
        self.dodge_rate = 20
    def level_up(self):
        self.level += 1

        self.max_health += 20
        self.health = self.max_health

        self.base_attack += 2
        self.defense += 1

        self.heal_health += 2

        if self.level % 10 == 0:
            self.crit_rate += 1

        if self.level % 15 == 0:
            self.dodge_rate += 1

        if self.level % 20 == 0:
            self.crit_damage += 10

        self.exp -= self.max_exp
        self.max_exp += 100

        print(f"Level up! Now level {self.level}")
    def gain_exp(self, drop_exp):
        self.exp += drop_exp
        while (self.exp >= self.max_exp):
            self.level_up()
    def status(self):
        print("-----------------------------------")
        print(f"===== Player {self.name} =====")
        print(f"Level   : {self.level}")
        print()
        self.health_bar()
        if self.weapon:
            print(f"ATK     : {self.attack} ({self.attack - self.weapon_atk_value} + {self.weapon_atk_value})")
        else:
            print(f"ATK     : {self.attack}")
        print(f"DEF     : {self.defense}")
        print()
        print(f"Crit    : {self.crit_rate}%")
        print(f"Crit DMG: {self.crit_damage}%")
        print(f"Dodge   : {self.dodge_rate}%")
        print()
        print(f"EXP     : {self.exp} / {self.max_exp}")
        print("-----------------------------------")
    @property
    def attack(self):
        atk = self.base_attack
        if self.weapon:
            atk += self.weapon_atk_value
        return atk
    def equip(self, item):
        if not self.weapon is item:
            if item.item_type == "Sword":
                self.weapon_atk_value = item.value
                self.weapon = item
                print(f"{self.name} Equipepd {item.name}")
                print()
        elif self.weapon is item:
            print(f"{self.name} is already equipped!")
    def unequip(self, item):
        if self.weapon is item:
            if item.item_type == "Sword":
                self.weapon_atk_value = 0
                self.weapon = None
                print(f"{self.name} Unequipped {item.name}")
    def run(self):
        print(f"{self.name} ran away!")
        return True
