from battle import Battle
from player import Player
from data import MONSTER_DATA
from data import ITEM_DATA
from inventory import Inventory
from run import Run
from monster import Monster
from heal import Heal
from lootsystem import loot_system
class Game:
    def __init__(self):
        print("===== Welcome to my RPG Game V2.1 =====")
        print()
        self.player = Player(input("Enter your name: "))
        self.inventory = Inventory()
        self.runs = Run()
        self.heals = Heal()
        self.loot = loot_system()
    def creative_action(self):
        self.actions = {
        "1": (self.battles.start),
        "2": (self.runs),
        "3": (self.player.status),
        "4": (self.inventory.inventory_show),
        "5": (self.heal_action),
        "6": (self.monster.status),
        }
    def heal_action(self):
        self.heals.heal(self.player, ITEM_DATA["Heal"])
        self.battles.monster_turn()
    def Menu(self):
        self.menu = {
            "1": "attack",
            "2": "run",
            "3": "player_status",
            "4": "inventory",
            "5": "heal",
            "6": "monster_status",
        }
    def choice_monster(self):
        print("1: Dark knight")
        print("2: Goblin")
        print("3: Slime")
        choice = input("Enter your choice: ")
        while not choice in MONSTER_DATA:
            choice = input("Enter your choice: ")
        data = MONSTER_DATA[choice]
        level = int(input("Choice monster level: "))
        self.monster = Monster(data["Name"], data["health"], data["max health"], data["ATK"], data["DEF"], data["EXP"], level, data["crt rate"], data["crt dmg"], data["dodge rate"], data["lootable"])
        self.battles = Battle(self.player, self.monster)
        self.creative_action()
        self.Menu()
    def player_action(self):
        for key, text in self.menu.items():
            print(f"{key}: {text}")
        action = input("> ").lower()
        if action in self.actions:
            self.actions[action]()
        else:
            print("Invalid action.")
    def start(self):
        self.choice_monster()
        self.monster.status(full=False)
        while not self.player.is_dead():
            if not self.monster.is_dead():
                self.player_action()
            else:
                item = self.loot.roll(self.monster)
                for item_name in item:
                    self.inventory.inventory_add(ITEM_DATA[item_name])
                self.choice_monster()
                self.monster.status(full=False)
        if self.player.is_dead():
            print("GAME OVER!")
