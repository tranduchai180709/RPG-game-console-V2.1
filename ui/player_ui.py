class PlayerUI:
    def show_status(self, player):
        data = player.get_status()
        print("-----------------------------------")
        print(f'===== Player {data['name']} =====')
        print(f'Health  : {data['health']} / {data['max_health']}')
        print(f'Level   : {data['level']}')
        print()
        print(f'ATK     : {data['ATK']}')
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

    