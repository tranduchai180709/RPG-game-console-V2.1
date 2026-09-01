from colorama import Style, Fore
class ShopUI:
    def shop_menu(self, shop, player):
        data = shop.get_items()
        print("====== BLACKSMITH =====")
        print()
        print(f"{player.gold:,} G")
        print()
        for i, item in enumerate(data, start=1):
            if item.stackable == True:
                print(f"{i}: {item.name} {item.base_price} G")
            else:
                print(f"{i}: {item.name} +{item.value} {item.rarity.color}[{item.rarity.name}] {Style.RESET_ALL} {item.base_price} G")
        print()
        print("0: Exit")
        print()
        return int(input("> "))
    def shop_choice(self):
        print("1: Buy")
        print("2: Sell")
        print("0: Exit")
        print()
        return input("> ")
    def sold_out(self, shop):
        data = shop.get_items()
        if data:
            print("The shop is sold out.")
            print()
            print("0: Exit")
            print()
            return int(input("> "))
    def choice_invaild(self):
        pass
    def choice_buy(self, item):
        if item:
            print()
            print(f"You bought {item.name}.")
            print()
        else:
            print()
            print(f"you dont have enough gold for {item.name}")
            print()
    def choice_sell(self, item):
        item_price = int(item.base_price * 0.7)
        print(f"Sell {item.name} for {item_price} G?")
        print("1:Yes")
        print("2:No")
        print()
        return input("> ")
    def choice_sell_yes(self, item, gold):
        item_price = int(item.base_price * 0.7)
        print(f"Sold {item.name}")
        print(f"+{item_price} G")
        print(f"Gold: {gold}")
        print()
    def choice_sell_no(self):
        return

