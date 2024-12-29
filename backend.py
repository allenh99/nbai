from flask import Flask, jsonify, request
from flask_cors import CORS
from tools.playstats import PlayerStats
from tools.roster import RosterStats
from agents.manager_agent import managerAgent
from agents.boxscore_agent import boxScoreAgent

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests for frontend integration

# Initialize PlayerStats
player_stats = PlayerStats('players.txt')

@app.route('/')
def home():
    data = {"player":"Josh Hart","o/u":"o","number":"8.5","stat_type":"rebounds","opp":"Washington Wizards"}

    return jsonify(managerAgent(data,[boxScoreAgent]))


# Endpoint: Get average fantasy points for a roster
@app.route('/roster/average', methods=['GET'])
def get_roster_average():
    filename = request.args.get('filename')
    season = int(request.args.get('season', 2025))
    try:
        roster_stats = RosterStats(filename)
        average_stats = roster_stats.getRosterAverageFPTSseason()
        return jsonify(average_stats)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint: Get total fantasy points for a roster
@app.route('/roster/total', methods=['GET'])
def get_roster_total():
    filename = request.args.get('filename')
    season = int(request.args.get('season', 2025))
    try:
        roster_stats = RosterStats(filename)
        total_stats = roster_stats.getRosterTotalFPTSseason()
        return jsonify(total_stats)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint: Fetch box scores for a player in a season
@app.route('/player/box_scores', methods=['GET'])
def get_player_box_scores():
    name = request.args.get('name')
    season = int(request.args.get('season'))
    try:
        scores = player_stats.player_box_scores_season(name, season)
        return jsonify(scores)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
