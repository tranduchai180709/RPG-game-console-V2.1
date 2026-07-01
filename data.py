from monster import Monster
from items import Items
MONSTER_DATA = {
    "1":{
        "Name": "Dark knight",
        "health": 100,
        "max health": 100,
        "ATK": 10,
        "DEF": 5,
        "EXP": 50,
        "crt rate": 0,
        "crt dmg": 200,
        "dodge rate": 10,
        "lootable": [
        ("Potion",40),
        ("Iron Armor",5)
        ]
    },
    "2":{
        "Name": "Goblin",
        "health": 20,
        "max health": 20,
        "ATK": 20,
        "DEF": 10,
        "EXP": 30 ,
        "crt rate": 0,
        "crt dmg": 200,
        "dodge rate": 15,
        "lootable": [
        ("Potion",20),
        ("Iron Sword",10)
        ]
    },
    "3":{
        "Name": "Slime",
        "health": 20,
        "max health": 20,
        "ATK": 5,
        "DEF": 0,
        "EXP":10,
        "crt rate": 0,
        "crt dmg": 200,
        "dodge rate": 30,
        "lootable": [
        ("Potion",10),
        ("Iron Sword",3),
        ("Iron Armor",2)
        ]
    }
}
ITEM_DATA = {
    "Heal": Items("Heal","heal",30, True),
    "Iron Sword": Items("Iron Sword","Sword",5, False),
    "Iron Armor": Items("Iron Armor","Armor",1, False)
}