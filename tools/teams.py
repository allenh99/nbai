from nba_api.stats.endpoints import leaguedashteamstats
from collections import defaultdict

class TeamStatsNBAAPI:
    def __init__(self, season="2023-24"):
        self.season = season
        self.team_stats = {}
        self.team_ranks = {}

    def fetch_team_stats(self):
        # Fetch team stats from nba_api
        response = leaguedashteamstats.LeagueDashTeamStats(
            season=self.season,
            measure_type_detailed_defense="Advanced"  # Advanced stats
        ).get_normalized_dict()

        stats = response['LeagueDashTeamStats']

        # Process team stats
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
