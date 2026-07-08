import random
from data import ITEM_DATA
from items import Items
class loot_system:
    def roll(self, monster):
        list_drop_item = []
        drop_item = []
        for i in monster.lootable:
            check = random.randint(1, 100)
            if check <= i[1]:
                list_drop_item.append(i[0])
        for item_name in list_drop_item:
            template = ITEM_DATA[item_name]
            item = Items(
                template.name,
                template.item_type,
                template.value,
                template.stackable
            )
            if not item.stackable:
                item.value = random.randint(template.value - 4, template.value + 4)
            drop_item.append(item)
        return drop_item 