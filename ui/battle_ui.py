class BattleUI:
    def attack(self, name, damage, target, crit):
        if damage == 0:
            print(f"{name} attacked! ")
            print()
            print(f"{target.name} Dodged the attack!")
            return
        if crit:
            print("Critical!!!")
        print(f"{name} dealt {damage} to {target.name}")
    def combat_status(self, target):
        print(f"===== {target.name} =====")
        self.health_bar(target)
        print("-------------------------")
    def health_bar(self, target):
        filled, empty, current, max_hp = target.health_bar_data()
        bar = "█" * filled + "-" * empty
        print(f"HP: [{bar}] {current} / {max_hp}")
