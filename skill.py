class Skill:
    def menu(self):
        self.menus = {
            "1": ("Normal attack"),
            "2": ("Skill")
        }
        for index, choice in self.menus.items():
            print(f"{index}: {choice}")
    def menu_skill(self, player):
        for index in player.skills:
            print(f"{index}: {player.skills[index]["name"]}",end=" ")
            if not player.skills[index]["current_cd"] == 0:
                print(f"(CD {player.skills[index]["current_cd"]})", end=" ")
            else:
                if player.skills[index]["attack_multiplier"] > 1:
                    print(f"x{player.skills[index]["attack_multiplier"]} ATK", end=" ")
                if player.skills[index]["defense_multiplier"] > 1:
                    print(f"x{player.skills[index]["defense_multiplier"]} DEF", end=" ")
            print()
        print("0 cancel")
        print()
SKILLS = {
    "1": {
        "name": "Slash",
        "attack_multiplier": 1.2,
        "defense_multiplier": 1,
        "cooldown": 2,
    },
    "2": {
        "name": "Heavy Strike",
        "attack_multiplier": 2.2,
        "defense_multiplier": 1,
        "cooldown": 3,
    },
}
