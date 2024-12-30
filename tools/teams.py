from basketball_reference_web_scraper import client
from datetime import datetime, timedelta
from collections import defaultdict

class TeamStats:
    def __init__(self, season_end_year=2025):
        self.season_end_year = season_end_year
        self.team_stats = defaultdict(lambda: {
            "games_played": 0,
            "opponent_points": 0,
            "opponent_rebounds": 0,
            "opponent_assists": 0
        })
        self.team_ranks = {}

    def calculate_team_stats(self):
        # Determine season start and end dates (NBA season typically starts in October and ends in April)
        season_start = datetime(self.season_end_year - 1, 10, 1)
        season_end = datetime(self.season_end_year, 4, 30)

        current_date = season_start
        while current_date <= season_end:
            try:
                box_scores = client.team_box_scores(
                    day=current_date.day, month=current_date.month, year=current_date.year
                )
                for game in box_scores:
                    team_name = game['team'].value
                    opponent_points = game['points']
                    opponent_rebounds = game['offensive_rebounds'] + game['defensive_rebounds']
                    opponent_assists = game['assists']

                    self.team_stats[team_name]["games_played"] += 1
                    self.team_stats[team_name]["opponent_points"] += opponent_points
                    self.team_stats[team_name]["opponent_rebounds"] += opponent_rebounds
                    self.team_stats[team_name]["opponent_assists"] += opponent_assists

            except Exception as e:
                print(f"An error occurred on {current_date}: {e}")

            current_date += timedelta(days=1)

        # Calculate averages
        for team, stats in self.team_stats.items():
            games_played = stats["games_played"]
            if games_played > 0:
                stats["avg_points_allowed"] = stats["opponent_points"] / games_played
                stats["avg_rebounds_allowed"] = stats["opponent_rebounds"] / games_played
                stats["avg_assists_allowed"] = stats["opponent_assists"] / games_played

        self.rank_team_stats()

    def rank_teams_by_stat(self, stat_key, ascending=True):
        sorted_teams = sorted(self.team_stats.items(), key=lambda x: x[1].get(stat_key, 0), reverse=not ascending)
        return {team[0]: rank + 1 for rank, team in enumerate(sorted_teams)}

    def rank_team_stats(self):
        self.team_ranks = {
            "points": self.rank_teams_by_stat("avg_points_allowed"),
            "rebounds": self.rank_teams_by_stat("avg_rebounds_allowed"),
            "assists": self.rank_teams_by_stat("avg_assists_allowed")
        }

    def save_stats_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                file.write("Team,Avg Points Allowed,Avg Rebounds Allowed,Avg Assists Allowed\n")
                for team, stats in self.team_stats.items():
                    file.write(f"{team},{stats.get('avg_points_allowed', 0):.2f},{stats.get('avg_rebounds_allowed', 0):.2f},{stats.get('avg_assists_allowed', 0):.2f}\n")
            print(f"Defense stats successfully written to {filename}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_ranks_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                file.write("Team,Points Rank,Rebounds Rank,Assists Rank\n")
                for team in self.team_ranks["points"].keys():
                    file.write(f"{team},{self.team_ranks['points'][team]},{self.team_ranks['rebounds'][team]},{self.team_ranks['assists'][team]}\n")
            print(f"Defense ranks successfully written to {filename}")
        except Exception as e:
            print(f"An error occurred: {e}")