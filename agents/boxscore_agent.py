#different agents - historical player data, opponent
from tools.playstats import PlayerIDGenerator,PlayerStats
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
    averages = stats.calculate_stat_averages()
    print(averages)

boxScoreAgent({"player":"Josh Hart","o/u":"o","number":"8.5","stat_type":"rebounds","opp":"Washington Wizards"})
