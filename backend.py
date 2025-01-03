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

@app.route('/')
def home():
    data = {
        "player":"Josh Hart",
        "o/u":"o",
        "number":"8.5",
        "stat_type":"rebounds",
        "opp":"Washington Wizards"
    }
    agents = {
        "box_score_agent": boxScoreAgent,
        "opp_agent": oppAgent
    }

    return jsonify(managerAgent(data,agent))

if __name__ == '__main__':
    app.run(debug=True)
