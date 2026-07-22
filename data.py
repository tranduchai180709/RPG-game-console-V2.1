from items import Items
from rarity import COMMON,UNCOMMON,RARE,EPIC,LEGENDARY
import random
MONSTER_DATA = {
    "1":{
        "Name": "Dark knight",
        "health": 100,
        "max health": 100,
        "ATK": 10,
        "DEF": 5,
        "EXP": 50,
        "level": 1,
        "crt rate": 0,
        "crt dmg": 200,
        "dodge rate": 10,
        "lootable": [
        ("Heal",40),
        ("Steel Sword",5),
        ("Iron Armor",10),
        ("Health Ring",15)
        ],
        "gold": 50
    },
    "2":{
        "Name": "Goblin",
        "health": 10,
        "max health": 10,
        "ATK": 20,
        "DEF": 1,
        "EXP": 30 ,
        "level": 1,
        "crt rate": 0,
        "crt dmg": 200,
        "dodge rate": 15,
        "lootable": [
        ("Heal",20),
        ("Iron Sword",10),
        ("Health Ring", 5)
        ],
        "gold": 30
    },
    "3":{
        "Name": "Slime",
        "health": 30,
        "max health": 30,
        "ATK": 5,
        "DEF": 0,
        "EXP": 20,
        "level": 1,
        "crt rate": 0,
        "crt dmg": 200,
        "dodge rate": 5,
        "lootable": [
        ("Heal",10),
        ("Iron Sword",5),
        ("Iron Armor",2),
        ("Health Ring", 1)
        ],
        "gold": 15
    }
}
ITEM_DATA = {
    "Heal": Items("Heal","heal",30, True, COMMON, 30),
    "Iron Sword": Items("Iron Sword","Sword",5, False, COMMON, 100),
    "Iron Armor": Items("Iron Armor","Armor",5, False, COMMON, 120),
    "Steel Sword": Items("Steel Sword", "Sword", 10, False, COMMON, 150),
    "Health Ring": Items("Health Ring", "Accessory", 10, False, COMMON, 90)
}
class Menu:
    def __init__(self):
        self.menus = {
            "1": "attack",
            "2": "run",
            "3": "player_status",
            "4": "inventory",
            "5": "heal",
            "6": "monster_status",
        }