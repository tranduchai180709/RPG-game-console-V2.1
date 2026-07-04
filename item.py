from data import ITEM_DATA
import random
class items:
    def item_ran_value(self, item):
        item.value = random.randint(item.value - 6, item.value + 6)
        return item