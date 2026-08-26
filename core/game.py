from .battle import Battle
from .player import Player
from .data import MONSTER_DATA
from .data import ITEM_DATA
from .inventory import Inventory
from .monster import Monster
from .heal import Heal
from .lootsystem import loot_system
from .shop import shops
from .saveload import save_game, load_game
from .wavemanager import wave
from .skill import Skill, SKILLS
class Game:
    def __init__(self, ui):
        self.ui = ui
        self.player = Player("player")
        self.inventory = Inventory()
        self.heals = Heal()
        self.loot = loot_system()
        self.shop = shops()
        self.wave = wave()
        self.skill = Skill()
        self.battles = Battle()
    def welcome(self):
        choice = self.ui.welcome()
        if choice == "2":
            self.player, self.inventory, self.wave, self.shop = load_game()
            return self.wave.monster
        elif choice == "1":
            self.player.name = self.ui.get_player_name()
            return 
        while choice not in ("2", "1"):
            choice = self.ui.welcome()
    def run_action(self):
        self.player.run()
        self.choice_monster()
        self.ui.show_monster_combat_status(self.monster)
    def inventory_open(self):
        if self.inventory.inventory_show(self.player):
            item = self.inventory.inventory_choice()
            if item:
                self.use_item(item)
    def use_item(self, item):
        if item.item_type == "Sword":
            self.player.equip_sword(item)

        elif item.item_type == "Armor":
            self.player.equip_armor(item)

        elif item.item_type == "heal":
            if self.heals.heal(self.player, item):
                self.inventory.inventory_remove(item)
                self.battles.monster_turn(self.player, self.monster)
    def shops(self):
        shop_item = self.shop.shop_choice(self.player,self.inventory)
        if shop_item:
            self.inventory.inventory_add(shop_item)
            self.shops()
        else:
            return
    def save_action(self):
        save_game(self.player, self.inventory, self.wave, self.shop)
    def battle_start(self):
        self.battles.start(self.player, self.monster, 1, 1, False)
    def load_action(self):
        self.player, self.inventory, self.wave, self.shop = load_game()
    def status_player(self):
        self.ui.show_player_status(self.player)
    def status_monster(self):
        self.ui.show_monster_status(self.monster)
    def attack_skill(self):
        self.skill.menu()
        choice = input("> ")
        if choice == "1":
            self.battle_start()
            return
        elif choice == "2":
            self.skill.menu_skill(self.player)
            choice = input("> ")
            if not choice == "0":
                skills = SKILLS[choice]
                for index in self.player.skills:
                    if skills["name"] == self.player.skills[index]["name"]:
                        if self.player.skills[index]["current_cd"] == 0:
                            self.player.skills[index]["current_cd"] = skills["cooldown"]
                            self.battles.start(self.player, self.monster, skills["attack_multiplier"], skills["defense_multiplier"], skill=True)
                        else:
                            self.ui.skill_cd()
            elif choice == "0":
                return
    def creative_action(self):
        self.actions = {
        "1": (self.attack_skill),
        "2": (self.run_action),
        "3": (self.status_player),
        "4": (self.inventory_open),
        "5": (self.status_monster),
        "6": (self.shops),
        "7": (self.save_action),
        "8": (self.load_action)
        }
    def choice_monster(self):
        self.monster = self.wave.next_wave()
    def player_action(self):
        action = self.ui.menu_ui()
        if action in self.actions:
            self.actions[action]()
        else:
            self.ui.action_ui()
    def start(self):
        monster = self.welcome()
        if not monster:
            self.choice_monster()    
            self.shop.shop_restock()
        else:
            self.monster = monster
        self.creative_action()
        self.ui.show_monster_combat_status(self.monster)
        while not self.player.is_dead():
            if not self.monster.is_dead():
                self.player_action()
            elif self.monster.is_dead():
                self.heals.heal(self.player, ITEM_DATA["Heal"])
                gold = self.monster.drop_gold()
                self.player.add_gold(gold)
                item = self.loot.roll(self.monster)
                for items in item:
                    self.inventory.inventory_add(items)
                self.choice_monster()
                self.shop.shop_restock()
                self.ui.show_monster_combat_status(self.monster)
        if self.player.is_dead():
            print("GAME OVER!")
