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
        data = player.equip(item)
        old_data = player.get_equipment()
        for items in old_data.items():
            print(items)
            if items == data:
                self.unequip_ui(player, old_data)
        if data:
            print(f"{player.name} equipped {item.name}")
        else:
            print(f"{player.name} already equipped this item")
    def unequip_ui(self, player, item):
        data = player.unequip(item)
        if data:
            print(f"{player.name} Unequipped {data.name}")