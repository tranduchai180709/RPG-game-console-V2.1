import json
from player import Player
from inventory import Inventory
SAVE_FILE = "save.json"
def save_game(player, inventory):
    save_data = {
        "player": player.to_dict(),
        "inventory": inventory.to_dict()
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(save_data, f, indent=4)

        print("Saved Game!")

def load_game():
    try:
        with open(SAVE_FILE, "r") as f:
            save_data = json.load(f)
        
        player = Player.from_dict(save_data["player"])
        inventory = Inventory.from_dict(save_data["inventory"])
        print("Loaded game!")
        return player, inventory
    except FileNotFoundError:
        print("You dont have any save file.")
        return None, None