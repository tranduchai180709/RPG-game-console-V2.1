class skill:
    def slash(self, player, monster, battle):
        damage = player.base_attack
        player.base_attack = int(player.base_attack * 1.2)
        battle.start(player, monster)
        player.base_attack = damage
    def heavy_strike(self, player, monster, battle):
        damage = player.base_attack
        player.base_attack = int(player.base_attack * 2.2)
        battle.start(player, monster)
        player.base_attack = damage
    def menu(self):
        self.menus = {
            "1": ("Attack"),
            "2": ("Skill")
        }
        for index, choice in self.menus.items():
            print(f"{index}: {choice}")
    def menu_skill(self):
        self.skill_menu = {
            "1": "Slash",
            "2": "Heavy Strike"
        }
        for index, choice in self.skill_menu.items():
            print(f"{index}: {choice}")