import random
from colorama import Style, Fore
from data import ITEM_DATA
from rarity import COMMON,UNCOMMON,RARE,EPIC,LEGENDARY
from items import Items
class loot_system:
    def roll(self, monster):
        list_drop_item = []
        drop_item = []
        for i in monster.lootable:
            check = random.randint(1, 100)
            if check <= i[1]:
                list_drop_item.append(i[0])
            gold = monster.drop_gold()
        print()
        print(f"+{monster.exp_drop} EXP")
        print(f"+{gold} G")
        print()
        if list_drop_item:
            print("=========================")
            print("|         Loot          |")
            print("=========================")
            for item_name in list_drop_item:
                template = ITEM_DATA[item_name]
                item = Items(
                    template.name,
                    template.item_type,
                    template.value,
                    template.stackable,
                    template.rarity,
                    random.randint(template.base_price * template.rarity.multipler - 20, template.base_price * template.rarity.multipler - 20) 
                )
                self.roll_rarity(item)
                if item.stackable:
                    print(f"{item.name} x1")
                else:
                    print(
                f"{item.name:<10} "
                f"{item.value:+4} "
                f"{item.rarity.color}[{item.rarity.name}]{Style.RESET_ALL}"
            )
                drop_item.append(item)
            print("-------------------------")
            print()
        return drop_item 
    def roll_rarity(self, item):
        if not item.stackable:
            rarity_roll = random.randint(1,100)
            if rarity_roll <= 60:
                item.rarity = COMMON
            elif rarity_roll <= 85:
                item.rarity = UNCOMMON
            elif rarity_roll <= 95:
                item.rarity = RARE
            elif rarity_roll <= 99:
                item.rarity = EPIC
            else:
                item.rarity = LEGENDARY
            mul_item_value = item.value * item.rarity.multipler
            item.value = random.randint(int(mul_item_value) - 4, int(mul_item_value) + 4)