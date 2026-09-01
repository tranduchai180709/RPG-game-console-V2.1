class BattleUI:
    def attack(self, name, damage, target, crit):
        if damage == 0:
            print(f"{name} attacked! ")
            print()
            print(f"{target.name} Dodged the attack!")
            return
        if crit == True:
            print("Critical!!!")
        print(f"{name} dealt {damage} to {target.name}")
    def combat_status(self, target):
        print(f"===== {target.name} =====")
        self.health_bar(target)
        print("-------------------------")
    def health_bar(self, target):
        length = 20
        if target.health <= 0:
            filled = 0
        else:
            filled = max(1,int(target.health / target.max_health * length))
        empty = length - filled

        bar = "█" * filled + "-" * empty

        print(f"HP: [{bar}] {round(max(0,target.health))} / {target.max_health}")
    