from typing import List, Any
from board import Board, CommunityChest, Chance
from property import Property, Street, Railroad, Utility
import time

class Game:
    def __init__(self, players: List[Any]):
        self.board = Board()
        self.players = players
        self.current_player_index = 0

    def play_turn(self):
        player = self.players[self.current_player_index]
        roll = self.roll_dice()
        player.move(roll)
        self.handle_space(player)
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        time.sleep(1)

    def roll_dice(self):
        import random
        res = random.randint(1, 6) + random.randint(1, 6)
        idx = self.current_player_index
        print(f"{self.players[idx].name} rolled {res}")
        return res

    def handle_space(self, player: Any):
        space = self.board.spaces[player.position]
        if isinstance(space, Property):
            if space.owner is None:
                space.purchase(player)
                print(f"{player.name} purchased {space.name}")
            elif space.owner != player:
                player.pay(space.rent)
                space.owner.receive(space.rent)
                print(f"{player.name} paid {space.rent} to {space.owner.name}")
        elif isinstance(space, CommunityChest) or isinstance(space, Chance):
            space.draw_card(player)
        if self.board.is_all_owned:
            print("All properties are owned!")
            # Add game-ending conditions

    def start(self):
        while True:
            self.play_turn()
            # Add game-ending conditions
