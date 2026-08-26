class MonsterUI:
    def show_status(self, monster):
        data = monster.get_status()
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
        print("-----------------------------------")
    def combat_status(self, monster):
        data = monster.get_status()
        print("-----------------------------------")
        print(f'===== Monster {data['name']} =====')
        print(f'Health  : {data['health']} / {data['max_health']}')
        print(f'Level   : {data['level']}')
        print()
        print(f'ATK     : {data['ATK']}')
        print(f'DEF     : {data['DEF']}')
        print("-----------------------------------")

    