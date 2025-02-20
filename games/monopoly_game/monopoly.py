from game import Game
from player import Player

def main():
    default_players = [Player("Player 1"), Player("Player 2")]
    players = default_players
    game = Game(players)
    game.start()

if __name__ == "__main__":
    main()
