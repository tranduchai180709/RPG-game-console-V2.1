from entity import Entity
class Player(Entity):
    def __init__(self, name):
        super().__init__(name, 50, 50, 10, 0, 10, 120, 20)
        self.weapon = None
        self.armor = None
        self.accessory = None
        self.base_defense = 0
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
        self.base_defense += 1

        self.heal_health += 2

        if self.level % 10 == 0:
            self.crit_rate += 1

        if self.level % 15 == 0:
            self.dodge_rate += 1

        if self.level % 20 == 0:
            self.crit_damage += 10

        self.exp -= self.max_exp
        self.max_exp += self.level * 10 + 50

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
            print(f"ATK     : {self.attack} ({self.attack - self.weapon.value} + {self.weapon.value})")
        else:
            print(f"ATK     : {self.attack}")
        if self.armor:
            print(f"DEF     : {self.defense} ({self.defense - self.armor.value} + {self.armor.value})")
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
            atk += self.weapon.value
        return atk
    @property
    def defense(self):
        defense = self.base_defense
        if self.armor:
            defense += self.armor.value
        return defense

    def equip(self, item):
        if not self.weapon is item:
            if item.item_type == "Sword":
                self.equip_sword(item)
            elif item.item_type == "Armor":
                self.equip_armor(item)
            elif item.item_type == "Accessory":
                self.equip_accessory(item)
        elif self.weapon is item:
            print(f"{self.name} is already equipped!")


    def equip_sword(self, item):
        self.unequip_sword()

        self.weapon = item
        print(f"{self.name} Equipped {item.name}")
        print()

    def equip_armor(self, item):
        self.unequip_armor()

        self.armor = item
        print(f"{self.name} Equipped {item.name}")
        print()

    def equip_accessory(self, item):
        self.unequip_accessory()
        self.accessory = item
        print(f"{self.name} Equipped {item.name}")
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
