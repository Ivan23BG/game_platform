from typing import Any

class Property:
    def __init__(self, name: str, price: int, rent: int):
        self.name = name   # Mayfair
        self.price = price # 400
        self.rent = rent   # 50
        self.owner = None  # None or Player object

    def purchase(self, player: Any) -> bool:
        if self.owner is None and player.money >= self.price:
            self.owner = player
            player.money -= self.price
            player.properties.append(self)
            return True
        return False

class Street(Property):
    def __init__(self, name: str, price: int, rent: int, color: Any):
        super().__init__(name, price, rent)
        self.color = color
        self.houses = 0
        self.hotels = 0

    def build_house(self, player: Any):
        if self.owner == player and self.houses < 4:
            self.houses += 1
            player.money -= 50  # Example cost to build a house

    def build_hotel(self, player: Any):
        if self.owner == player and self.houses == 4:
            self.hotels += 1
            self.houses = 0
            player.money -= 50  # Example cost to build a hotel

class Railroad(Property):
    def __init__(self, name: str, price: int):
        super().__init__(name, price, rent=25)

class Utility(Property):
    def __init__(self, name: str, price: int):
        super().__init__(name, price, rent=4 * 4)  # Example rent calculation


# Brown properties
Old_Kent_Road = Street("Old Kent Road", 60, 2, "Brown")
Whitechapel_Road = Street("Whitechapel Road", 60, 4, "Brown")

# Light blue properties
The_Angel_Islington = Street("The Angel Islington", 100, 6, "Light Blue")
Euston_Road = Street("Euston Road", 100, 6, "Light Blue")
Pentonville_Road = Street("Pentonville Road", 120, 8, "Light Blue")

# Pink properties
Pall_Mall = Street("Pall Mall", 140, 10, "Pink")
Whitehall = Street("Whitehall", 140, 10, "Pink")
Northumberland_Avenue = Street("Northumberland Avenue", 160, 12, "Pink")

# Orange properties
Bow_Street = Street("Bow Street", 180, 14, "Orange")
Marlborough_Street = Street("Marlborough Street", 180, 14, "Orange")
Vine_Street = Street("Vine Street", 200, 16, "Orange")

# Red properties
Strand = Street("Strand", 220, 18, "Red")
Fleet_Street = Street("Fleet Street", 220, 18, "Red")
Trafalgar_Square = Street("Trafalgar Square", 240, 20, "Red")

# Yellow properties
Leicester_Square = Street("Leicester Square", 260, 22, "Yellow")
Coventry_Street = Street("Coventry Street", 260, 22, "Yellow")
Piccadilly = Street("Piccadilly", 280, 24, "Yellow")

# Green properties
Regent_Street = Street("Regent Street", 300, 26, "Green")
Oxford_Street = Street("Oxford Street", 300, 26, "Green")
Bond_Street = Street("Bond Street", 320, 28, "Green")

# Dark blue properties
Park_Lane = Street("Park Lane", 350, 35, "Dark Blue")
Mayfair = Street("Mayfair", 400, 50, "Dark Blue")

# Railroads
Kings_Cross_Station = Railroad("Kings Cross Station", 200)
Marylebone_Station = Railroad("Marylebone Station", 200)
Fenchurch_St_Station = Railroad("Fenchurch St Station", 200)
Liverpool_St_Station = Railroad("Liverpool St Station", 200)

# Utilities
Electric_Company = Utility("Electric Company", 150)
Water_Works = Utility("Water Works", 150)