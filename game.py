from battle import Battle
from player import Player
from data import MONSTER_DATA
from data import ITEM_DATA
from inventory import Inventory
from run import Run
from monster import Monster
from heal import Heal
class Game:
    def __init__(self):
        print("===== Welcome to my RPG Game V2.1 =====")
        print()
        self.player = None
        self.player = Player(input("Enter your name: "))
        self.inventory = Inventory()
        self.runs = Run()
        self.heals = Heal()
    def choice_monster(self):
        print("1: Dark knight")
        print("2: Goblin")
        print("3: Slime")
        choice = input("Enter your choice: ")
        while not choice in MONSTER_DATA:
            choice = input("Enter your choice: ")
        data = MONSTER_DATA[choice]
        level = int(input("Choice monster level: "))
        self.monster = Monster(data["Name"], data["health"], data["max health"], data["ATK"], data["DEF"], data["EXP"], level, data["crt rate"], data["crt dmg"], data["dodge rate"])
        self.battles = Battle(self.player, self.monster)
    def player_action(self):
        print("1: Attack")
        print("2: Run")
        print("3: Player status")
        print("4: Inventory")
        print("5: Heal")
        print("6: Monster status")
        action = input("> ")
        if action == "1":
            self.battles.start()
        elif action =="2":
            self.runs.run(self.player.name)
            print()
            self.choice_monster()
        elif action == "3":
            self.player.status()
        elif action == "4":
            self.inventory.inventory_show()
        elif action == "5":
            if(self.player.health == self.player.max_health):
                print("Your HP is already full.")
            else:
                self.heals.heal(self.player)
                self.battles.monster_turn()
        elif action == "6":
            self.monster.status()
        elif action == "7":
            self.inventory.inventory_add(ITEM_DATA["Heal"])
    def start(self):
        self.choice_monster()
        self.monster.status(full=False)
        while not self.player.is_dead():
            if not self.monster.is_dead():
                self.player_action()
            else:
                self.choice_monster()
                self.monster.status(full=False)
        if self.player.is_dead():
            print("GAME OVER!")
