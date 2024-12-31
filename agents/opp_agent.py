from tools.teams import TeamStats

def oppAgent(data):
    """
    Analyze the opponent's team ratings with priority given to the specified stat type.
    
    Parameters:
        data (dict): Contains "opp" (opposing team name), "stat_type" (statistic type), and other relevant information.

    Returns:
        dict: Analysis of the opponent's team stats with a signal based on the prioritized stat type.
    """

    opponent_team = data["opp"]
    stat_type = data["stat_type"]  # e.g., "points", "rebounds", "assists"
    thresholds = {
        "points": {"def_rating_rank": 15},   # Prioritize defensive rating for points
        "rebounds": {"reb_percent_rank": 15},  # Prioritize rebound percentage for rebounds
        "assists": {"ast_ratio_rank": 15},   # Prioritize assist ratio for assists
    }

    if not opponent_team or not stat_type:
        return {"data": data, "message": ["Missing opponent or stat type information."], "signal": "unknown"}

    team_stats = TeamStats(season="2023-24")
    team_stats.fetch_team_stats()
    opp_data = team_stats.get_team_data(opponent_team)

    if not opp_data:
        return {"data": data, "message": [f"No data available for {opponent_team}"], "signal": "unknown"}

    stats = opp_data["stats"]
    ranks = opp_data["ranks"]
    stat_thresholds = thresholds.get(stat_type, {})
    messages = []
    signal = "neutral"

    for stat_key, threshold in stat_thresholds.items():
        rank = ranks.get(stat_key)
        if rank:
            if rank < threshold:
                messages.append(f"{opponent_team} excels in {stat_key.replace('_rank', '').replace('_', ' ')} (ranked {rank}).")
                if stat_type == "points":
                    signal = "under"  # strong defensive teams for points signal "under"
                elif stat_type == "rebounds":
                    signal = "under"  # strong rebounding teams signal "under"
            elif rank > threshold:
                messages.append(f"{opponent_team} struggles in {stat_key.replace('_rank', '').replace('_', ' ')} (ranked {rank}).")
                signal = "over"  # weak teams in key areas signal "over"

    # Default message if no insights are generated
    if not messages:
        messages.append(f"No specific strengths or weaknesses identified for {opponent_team} in {stat_type}.")

    return {
        "data": data,
        "message": messages,
        "signal": signal
    }