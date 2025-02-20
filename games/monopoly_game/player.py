# from typing import List

class Player:
    def __init__(self, name: str):
        self.name = name     # Bob
        self.money = 1500    # Starting money
        self.position = 0    # Starting position
        self.properties = [] # No starting properties
        self.in_jail = False # Not in jail
        self.jail_cards = 0  # No Get Out of Jail Free cards

    def move(self, spaces: int):
        self.position = (self.position + spaces) % 7 # Example board size of 7

    def pay(self, amount: int) -> bool:
        if self.money >= amount:
            self.money -= amount
            return True
        return False

    def receive(self, amount: int):
        self.money += amount
