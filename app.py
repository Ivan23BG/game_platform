from flask import Flask, render_template, jsonify, request
from game_logic.monopoly.monopoly import Monopoly, Player, Property
from game_logic.monopoly.config import STARTING_MONEY, BOARD_SIZE

app = Flask(__name__, template_folder="./game_ui/templates")

# Initialize game state
players = [Player("Player 1"), Player("Player 2")]
properties = [
    Property("Property 1", 100, 50),
    Property("Property 2", 120, 60),
    Property("Property 3", 140, 70),
    Property("Property 4", 160, 80),
    Property("Property 5", 180, 90),
]
game = Monopoly(players, properties)

@app.route('/')
def home():
    return render_template('game1.html')

@app.route('/game-state')
def game_state():
    state = {
        "players": [{"name": p.name, "money": p.money, "position": p.position, "properties": [prop.name for prop in p.properties]} for p in game.players],
        "properties": [{"name": p.name, "owner": p.owner.name if p.owner else None} for p in game.properties],
        "current_player": game.players[game.current_player_index].name
    }
    return jsonify(state)

@app.route('/roll-dice', methods=['POST'])
def roll_dice():
    roll = game.roll_dice()
    player = game.players[game.current_player_index]
    player.move(roll)
    game.handle_space(player)
    game.current_player_index = (game.current_player_index + 1) % len(game.players)
    return jsonify({"roll": roll})

@app.route('/trade', methods=['POST'])
def trade():
    data = request.json
    player = game.players[game.current_player_index]
    receiver = game.players[(game.current_player_index + 1) % len(game.players)]
    property_name = data.get('property')
    property = next((p for p in player.properties if p.name == property_name), None)
    if property and player.trade_property(property, receiver):
        return jsonify({"success": True})
    return jsonify({"success": False})

if __name__ == '__main__':
    app.run(debug=True)
