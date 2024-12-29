#different agents - historical player data, opponent
from tools.playstats import PlayerIDGenerator,PlayerStats
from datetime import datetime

current_date = datetime.now()
formatted_date = current_date.strftime("%m/%d/%Y")

def boxScoreAgent(data):
    player = data["player"]
    ou = data["o/u"]
    number = float(data["number"])
    stat_type = data["stat_type"]

    generator = PlayerIDGenerator(2025)
    generator.generate_player_ids('players.txt')

    stats = PlayerStats()
    averages = stats.calculate_stat_averages(player,formatted_date)
    periods = ["1week", "1month", "3month"]

    performance_comparison = {}

    for period in periods:
        period_average = averages[period][stat_type]["average"]
        season_average = averages["season"][stat_type]["average"]

        if period_average > season_average:
            performance_comparison[period] = "better"
        elif period_average < season_average:
            performance_comparison[period] = "worse"
        else:
            performance_comparison[period] = "same"

    recent_form_average = averages["1week"][stat_type]["average"]
    if ou == "o":
        score = recent_form_average >= number
    else:
        score = recent_form_average <= number

    ret = 'over' if score else 'under'
    message = "Based on the last week, " + ret + " " + str(number) + " for " + stat_type + " is expected."

    return {
        "data": performance_comparison, 
        "message": [message], 
        "signal": ret
    }