from nba_api.stats.endpoints import leaguedashteamstats
from collections import defaultdict

class TeamStats:
    def __init__(self, season="2023-24"):
        self.season = season
        self.team_stats = {}
        self.team_ranks = {}

    def fetch_team_stats(self):
        response = leaguedashteamstats.LeagueDashTeamStats(
            season=self.season,
            measure_type_detailed_defense="Advanced"  # Advanced stats
        ).get_normalized_dict()

        stats = response['LeagueDashTeamStats']

        for team in stats:
            team_name = team['TEAM_NAME']
            self.team_stats[team_name] = {
                "off_rating": team['OFF_RATING'],    # Offensive Rating
                "def_rating": team['DEF_RATING'],    # Defensive Rating
                "net_rating": team['NET_RATING'],    # Net Rating
                "reb_percent": team['REB_PCT'],      # Rebound Percentage
                "ast_ratio": team['AST_RATIO']       # Assist Ratio
            }

        self.rank_team_stats()

    def rank_teams_by_stat(self, stat_key, ascending=True):
        sorted_teams = sorted(self.team_stats.items(), key=lambda x: x[1][stat_key], reverse=not ascending)
        return {team[0]: rank + 1 for rank, team in enumerate(sorted_teams)}

    def rank_team_stats(self):
        self.team_ranks = {
            "off_rating": self.rank_teams_by_stat("off_rating", ascending=False),
            "def_rating": self.rank_teams_by_stat("def_rating"),
            "net_rating": self.rank_teams_by_stat("net_rating", ascending=False),
            "reb_percent": self.rank_teams_by_stat("reb_percent", ascending=False),
            "ast_ratio": self.rank_teams_by_stat("ast_ratio", ascending=False),
        }

    def save_stats_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                file.write("Team,Offensive Rating,Defensive Rating,Net Rating,Rebound %,Assist Ratio\n")
                for team, stats in self.team_stats.items():
                    file.write(f"{team},{stats['off_rating']:.2f},{stats['def_rating']:.2f},{stats['net_rating']:.2f},{stats['reb_percent']:.2f},{stats['ast_ratio']:.2f}\n")
            print(f"Advanced stats successfully written to {filename}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_ranks_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                file.write("Team,Offensive Rating Rank,Defensive Rating Rank,Net Rating Rank,Rebound % Rank,Assist Ratio Rank\n")
                for team in self.team_ranks["off_rating"].keys():
                    file.write(
                        f"{team},{self.team_ranks['off_rating'][team]},{self.team_ranks['def_rating'][team]},{self.team_ranks['net_rating'][team]},{self.team_ranks['reb_percent'][team]},{self.team_ranks['ast_ratio'][team]}\n"
                    )
            print(f"Ranks successfully written to {filename}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_team_data(self, team_name):
        if team_name in self.team_stats:
            team_data = self.team_stats[team_name]
            team_ranks = {
                "off_rating_rank": self.team_ranks['off_rating'].get(team_name, None),
                "def_rating_rank": self.team_ranks['def_rating'].get(team_name, None),
                "net_rating_rank": self.team_ranks['net_rating'].get(team_name, None),
                "reb_percent_rank": self.team_ranks['reb_percent'].get(team_name, None),
                "ast_ratio_rank": self.team_ranks['ast_ratio'].get(team_name, None),
            }
            return {"stats": team_data, "ranks": team_ranks}
        else:
            return None