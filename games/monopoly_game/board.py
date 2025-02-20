from typing import Any
from property import Property, Street, Railroad, Utility
from property import Old_Kent_Road, Whitechapel_Road, The_Angel_Islington, Euston_Road, Pentonville_Road, Pall_Mall, Whitehall, Northumberland_Avenue, Bow_Street
from property import Marlborough_Street, Vine_Street, Strand, Fleet_Street, Trafalgar_Square, Leicester_Square, Coventry_Street, Piccadilly, Regent_Street
from property import Oxford_Street, Bond_Street, Park_Lane, Mayfair
from property import King_Cross_Station, Marylebone_Station, Fenchurch_St_Station, Liverpool_St_Station
from property import Electric_Company, Water_Works

class Board:
    def __init__(self):
        self.spaces = [] * 40
        self.create_board()
        self.is_all_owned = False

    def create_board(self):
        # To set up a board, add a property at a certain space index
        # and append it to the spaces list
        self.add_to_board("To add", 0)
        self.add_to_board(Old_Kent_Road, 1)
        self.add_to_board("To add", 2)
        self.add_to_board(Whitechapel_Road, 3)
        self.add_to_board("To add", 4)
        self.add_to_board(King_Cross_Station, 5)
        self.add_to_board(The_Angel_Islington, 6)
        self.add_to_board("To add", 7)
        self.add_to_board(Euston_Road, 8)
        self.add_to_board(Pentonville_Road, 9)
        self.add_to_board("To add", 10)
        self.add_to_board(Pall_Mall, 11)
        self.add_to_board(Electric_Company, 12)
        self.add_to_board(Whitehall, 13)
        self.add_to_board(Northumberland_Avenue, 14)
        self.add_to_board(Marylebone_Station, 15)
        self.add_to_board(Bow_Street, 16)
        self.add_to_board("To add", 17)
        self.add_to_board(Marlborough_Street, 18)
        self.add_to_board(Vine_Street, 19)
        self.add_to_board("To add", 20)
        self.add_to_board(Strand, 21)
        self.add_to_board("To add", 22)
        self.add_to_board(Fleet_Street, 23)
        self.add_to_board(Trafalgar_Square, 24)
        self.add_to_board(Fenchurch_St_Station, 25)
        self.add_to_board(Leicester_Square, 26)
        self.add_to_board(Coventry_Street, 27)
        self.add_to_board("To add", 28)
        self.add_to_board(Piccadilly, 29)
        self.add_to_board("To add", 30)
        self.add_to_board(Regent_Street, 31)
        self.add_to_board(Oxford_Street, 32)
        self.add_to_board("To add", 33)
        self.add_to_board(Bond_Street, 34)
        self.add_to_board("To add", 35)
        self.add_to_board("To add", 36)
        self.add_to_board(Park_Lane, 37)
        self.add_to_board("To add", 38)
        self.add_to_board(Mayfair, 39)
        print("Board created!")
        print("Spaces and positions:")
        for i, space in enumerate(self.spaces):
            print(f"{i}: {space.name}")
        # Continue adding properties and other spaces...
        
    def add_to_board(self, space: Property, index: int):
        self.spaces.insert(index, space)

class CommunityChest:
    def __init__(self):
        self.name = "Community Chest"

    def draw_card(self, player: Any):
        # Implement card drawing logic
        pass

class Chance:
    def __init__(self):
        self.name = "Chance"

    def draw_card(self, player: Any):
        # Implement card drawing logic
        pass
