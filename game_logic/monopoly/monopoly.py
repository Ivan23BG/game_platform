import random
from game_logic.monopoly.config import STARTING_MONEY, BOARD_SIZE, HOUSE_COST, HOTEL_COST

class Player:
    def __init__(self, name: str):
        self.name = name
        self.money = STARTING_MONEY
        self.properties = []

    def move(self, spaces: int):
        self.position = (self.position + spaces) % BOARD_SIZE

    def pay(self, amount: int) -> bool:
        if self.money >= amount:
            self.money -= amount
            self.show_money()
            return True
        return False

    def receive(self, amount: int):
        self.money += amount
        self.show_money()


    def show_properties(self):
        return [property.name for property in self.properties]


    def handle_properties(self):
        print(f"Properties owned by {self.name}:")
        for property in self.properties:
            print(property.name)
        print("Implement further house and trade handling here.")


    def trade_property(self, property, receiver):
        if property in self.properties:
            self.properties.remove(property)
            receiver.properties.append(property)
            property.owner = receiver
            return True
        return False

    
    def show_money(self):
        print(f"{self.name}: {self.money}")

class Property:
    def __init__(self, name: str, price: int, rent: int):
        self.name = name
        self.icon = None
        self.price = price
        self.rent = rent
        self.owner = None

    def purchase(self, player):
        if self.owner is None and player.money >= self.price:
            self.owner = player
            player.money -= self.price
            player.properties.append(self)
            player.show_money()
            return True
        return False

class Monopoly:
    def __init__(self, players, properties):
        self.players = players
        self.properties = properties
        self.current_player_index = 0

    def start_game(self):
        while True:
            self.play_turn()

    def play_turn(self):
        player = self.players[self.current_player_index]
        print(f"\n{player.name}'s turn!")
        
        choice = int(input("Press \n\
            1 to roll dice\n\
            2 to handle properties\n\
            3 to trade\n\
        "))
        while choice not in [1, 2, 3]:
            print("Invalid choice. Try again.")
            choice = int(input("Press \n\
                1 to roll dice\n\
                2 to handle properties\n\
                3 to trade\n\
            "))
            
        while choice != 1:
            print("Feature not implemented yet. Try again.")
            choice = int(input("Press \n\
                1 to roll dice\n\
                2 to handle properties\n\
                3 to trade\n\
            "))
        
        if choice == 1:
            roll = self.roll_dice()
            print(f"{player.name} rolled a {roll}.")
            player.move(roll)
            self.handle_space(player)
        elif choice == 2:
            player.handle_properties()
        elif choice == 3:
            self.trade(player)
        # elif choice == 2:
        #     player.handle_properties()
        # elif choice == 3:
        #     print("Trade functionality not implemented yet.")

        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def roll_dice(self):
        return random.randint(1, 6)

    def handle_space(self, player):
        property = self.properties[player.position]
        print(f"{player.name} landed on {property.name}.")
        if property.owner is None:
            choice = input(f"Do you want to buy {property.name} for ${property.price}? (y/n): ").strip().lower()
            if choice == 'y':
                if property.purchase(player):
                    print(f"{player.name} bought {property.name}!")
                else:
                    print(f"{player.name} does not have enough money to buy {property.name}.")
            else:
                print(f"{player.name} chose not to buy {property.name}.")
                print("It will be auctioned off.")
                self.auction_property(property)
        elif property.owner != player:
            print(f"{property.name} is owned by {property.owner.name}. Pay ${property.rent} rent.")
            if player.pay(property.rent):
                property.owner.receive(property.rent)
            else:
                print(f"{player.name} cannot afford the rent and goes bankrupt!")
                self.players.remove(player)
                if len(self.players) == 1:
                    print(f"{self.players[0].name} wins the game!")
                    exit()
    
    def trade(self, player):
        print(f"{player.name} wants to trade.")
        receiver = self.players[(self.current_player_index + 1) % len(self.players)]
        print(f"Available properties to trade from {player.name}: {player.show_properties()}")
        property_name = input("Enter the property name to trade: ")
        property = next((p for p in player.properties if p.name == property_name), None)
        if property and player.trade_property(property, receiver):
            print(f"{property.name} traded to {receiver.name}.")
        else:
            print("Trade failed.")
    
    
    def auction_property(self, property):
        pass

def main():
    # Create players
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    # Create properties
    properties = [
        Property("Property 1", 100, 50),
        Property("Property 2", 120, 60),
        Property("Property 3", 140, 70),
        Property("Property 4", 160, 80),
        Property("Property 5", 180, 90),
    ]

    # Initialize the game
    game = Monopoly([player1, player2], properties)
    game.start_game()

if __name__ == "__main__":
    main()
