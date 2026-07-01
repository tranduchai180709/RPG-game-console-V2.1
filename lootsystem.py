import random
class loot_system:
    def roll(self, monster):
        list_drop_item = []
        for i in monster.lootable:
            check = random.randint(1, 100)
            if check <= i[1]:
                list_drop_item.append(i[0])
        return list_drop_item