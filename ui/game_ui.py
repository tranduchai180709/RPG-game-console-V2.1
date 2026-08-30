from .player_ui import PlayerUI
from .monster_ui import MonsterUI
from .inventory_ui import InventoryUI
class Game_ui:
    def __init__(self):
        self.player_ui = PlayerUI()
        self.monster_ui = MonsterUI()
        self.inventory_ui = InventoryUI()
        self.menu = {
            "1": "Attack",
            "2": "Run",
            "3": "Player status",
            "4": "Inventory",
            "5": "Monster status",
            "6": "Shop",
            "7": "Save game",
            "8": "Load game"
        }
    def show_player_status(self, player):
        self.player_ui.show_status(player)
    def show_monster_combat_status(self, monster):
        self.monster_ui.combat_status(monster)
    def show_monster_status(self, monster):
        self.monster_ui.show_status(monster)
    def show_player_inventory(self, inventory, player):
        self.inventory_ui.show_inventory(inventory, player)
    def choice_inventory_ui(self):
        return self.inventory_ui.inventory_choice_ui()
    def game_over(self):
        print("GAME OVER")
    def menu_ui(self):
        for key, text in self.menu.items():
            print(f"{key}: {text}")
        return input("> ")
    def welcome(self):
        print("1: New Game")
        print("2: Continue")
        return input("> ")
    def get_player_name(self):
        return input("Enter your name: ")
    def action_ui(self):
        print("Invald action")
    def skill_cd(self):
        print("Skill in cooldown.")
    def player_equip(self, player, item):
        self.player_ui.equip_ui(player, item)
    def player_unequip(self, player, item):
        self.player_ui.unequip_ui(player, item)