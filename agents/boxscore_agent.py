#different agents - historical player data, opponent
from playstats import PlayerStats,PlayerIDGenerator
import json
from datetime import datetime

current_date = datetime.now()
formatted_date = current_date.strftime("%m/%d/%Y")

def boxScoreAgent(data):
    player = data["player"]
    ou = data["o/u"]
    number = data["number"]
    stat_type = data["stat_type"]

    generator = PlayerIDGenerator(2025)
    generator.generate_player_ids('players.txt')

    stats = PlayerStats()
    stats.player_box_scores_season(name,2025)
    stats.player_box_scores_3month(name,formatted_date)
    stats.player_box_scores_1month(name,formatted_date)

