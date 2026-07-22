class Skill:
    def to_dict(self):
        return {
            SKILLS
        }
    @classmethod
    def from_dict(self):
        pass
    def menu(self):
        self.menus = {
            "1": ("Attack"),
            "2": ("Skill")
        }
        for index, choice in self.menus.items():
            print(f"{index}: {choice}")
    def menu_skill(self, player):
        for index in player.skill:
            print(f"{index}: {player.skill[index]["name"]}",end=" ")
            if not player.skill[index]["current_cd"] == 0:
                print(f"(CD {player.skill[index]["current_cd"]})", end=" ")
            else:
                if player.skill[index]["attack_multiplier"] > 1:
                    print(f"x{player.skill[index]["attack_multiplier"]} ATK", end=" ")
                if player.skill[index]["defense_multiplier"] > 1:
                    print(f"x{player.skill[index]["defense_multiplier"]} DEF", end=" ")
                
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
