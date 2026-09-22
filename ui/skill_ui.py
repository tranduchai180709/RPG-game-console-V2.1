class SkillUI:
    def skill_menu(self):
        self.menus = {
            "1": ("Normal attack"),
            "2": ("Skill")
        }
    def skill_menu_skill(self, player):
        for index, skill in self.menus.items():
            print(f"{index}: {skill}")
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
        return
    def skill_choice(self):
        return input("> ")