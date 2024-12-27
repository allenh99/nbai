from basketball_reference_web_scraper import client

class TeamStats():
    def __init__(self, season_end_year=2025):
        self.season_end_year = season_end_year
        self.team_stats = {}
        self.team_ranks = {}

    def calculate_team_stats(self):
        teams = client.teams_season_totals(season_end_year=self.season_end_year)
        
        for team in teams:
            team_name = team['name']
            games_played = team['games_played']

            points_allowed = team['opponent_points']
            rebounds_allowed = team['opponent_total_rebounds']
            assists_allowed = team['opponent_assists']

            avg_points_allowed = points_allowed / games_played
            avg_rebounds_allowed = rebounds_allowed / games_played
            avg_assists_allowed = assists_allowed / games_played

            self.team_stats[team_name] = {
                "avg_points_allowed": avg_points_allowed,
                "avg_rebounds_allowed": avg_rebounds_allowed,
                "avg_assists_allowed": avg_assists_allowed
            }

        self.rank_defense_stats()

    def rank_teams_by_stat(stat_key, ascending=True):
            sorted_teams = sorted(self.team_stats.items(), key=lambda x: x[1][stat_key], reverse=not ascending)
            return {team[0]: rank + 1 for rank, team in enumerate(sorted_teams)}

    def rank_team_stats(self):
        self.team_ranks = {
            "points": rank_teams_by_stat("avg_points_allowed"),
            "rebounds": rank_teams_by_stat("avg_rebounds_allowed"),
            "assists": rank_teams_by_stat("avg_assists_allowed")
        }

    def save_stats_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                file.write("Team,Avg Points Allowed,Avg Rebounds Allowed,Avg Assists Allowed\n")
                for team, stats in self.team_stats.items():
                    file.write(f"{team},{stats['avg_points_allowed']:.2f},{stats['avg_rebounds_allowed']:.2f},{stats['avg_assists_allowed']:.2f}\n")
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
