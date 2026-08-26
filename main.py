from core.game import Game
from ui.game_ui import Game_ui
def main():
    ui = Game_ui()
    game = Game(ui)

    game.start()
if __name__ == "__main__":
    main()