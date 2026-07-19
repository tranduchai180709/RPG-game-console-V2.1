from colorama import Fore, Style
class Rarity:
    def __init__(self, name, multipler, color):
        self.name = name
        self.multipler = multipler
        self.color = color
COMMON = Rarity("Common", 1, Fore.WHITE)
UNCOMMON = Rarity("Uncommon", 1.2, Fore.GREEN)
RARE = Rarity("Rare", 2, Fore.LIGHTBLUE_EX)
EPIC = Rarity("Epic", 3.0, Fore.MAGENTA)
LEGENDARY = Rarity("Legendary", 5.0, Fore.YELLOW)
RARITY_DATA = {
    "Common": COMMON,
    "Uncommon": UNCOMMON,
    "Rare": RARE,
    "Epic": EPIC,
    "Legendary": LEGENDARY
}