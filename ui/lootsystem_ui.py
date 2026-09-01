from colorama import Style, Fore
class LootsystemUI:
    def loot_ui(self, gold, exp, item_list):
        print()
        print(f"+{exp} EXP")
        print(f"+{gold} G")
        print()
        if item_list:
            print("=========================")
            print("|         Loot          |")
            print("=========================")
            for item in item_list:
                if item.stackable:
                    print(f"{item.name} x1")
                else:
                    print(
                f"{item.name:<10} "
                f"{item.value:+4} "
                f"{item.rarity.color}[{item.rarity.name}]{Style.RESET_ALL}"
            )
            print("-------------------------")
            print()
