from flask import Flask, jsonify, request
from flask_cors import CORS
from tools.playstats import PlayerStats
from tools.roster import RosterStats
from agents.manager_agent import managerAgent
from agents.boxscore_agent import boxScoreAgent
from agents.opp_agent import oppAgent

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests for frontend integration

# Initialize PlayerStats
player_stats = PlayerStats('players.txt')

@app.route('/', methods=['POST'])
def home():
    data = request.json

    if not data:
        return jsonify({"error": "No data provided"}), 400
    print(data)
    agents = {
        "box_score_agent": boxScoreAgent,
        "opp_agent": oppAgent
    }

    return jsonify(managerAgent(data,agents))

if __name__ == '__main__':
    app.run(debug=True)
