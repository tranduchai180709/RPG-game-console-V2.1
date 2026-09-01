class PlayerUI:
    def show_status(self, player):
        data = player.get_status()
        print("-----------------------------------")
        print(f'===== Player {data['name']} =====')
        print(f'Health  : {data['health']} / {data['max_health']}')
        print(f'Level   : {data['level']}')
        print()
        if player.weapon:
            print(f'ATK     : {data['ATK']} ({data['base_attack']} + {data['weapon']})')
        else:
            print(f'ATK     : {data['ATK']}')
        if player.armor:
            print(f'DEF     : {data['DEF']} ({data['base_defense']} + {data['armor']})')
        else:
            print(f'DEF     : {data['DEF']}')
        print()
        print(f'Crit    : {data['crit']}%')
        print(f'Crit DMG: {data['crit_DMG']}%')
        print(f'Dodge   : {data['dodge']}%')
        print()
        print(f'EXP     : {data['exp']} / {data['max_exp']}')
        print("-----------------------------------")
    def level_up_ui(self, player):
        data = player.get_level()
        print(f"Your level: {data}")

    def equip_ui(self, player, item):
        data = player.get_equipment()
        if data:
            for index, items in data.items():
                if items:
                    if items.item_type == item.item_type:
                        self.unequip_ui(player, items)
            print(f"{player.name} equipped {item.name}")
    def unequip_ui(self, player, item):
        print(f"{player.name} Unequipped {item.name}")
        print()