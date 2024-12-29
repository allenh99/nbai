from tools.playstats import PlayerStats

class Roster:

    def __init__(self, filename=None):
        self.roster = []
        if filename:
            self.load_roster(filename)

    def load_roster(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    player_name = line.strip()
                    if player_name:
                        self.roster.append(player_name)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def getRoster(self):
        return self.roster

    def addToRoster(self,player):
        self.roster.append(player)
        return

#RosterStats(roster filename) - calculates roster statistics
class RosterStats():
    stats = PlayerStats('players.txt')

    def __init__(self,filename):
        self.season = 2025
        self.roster = Roster(filename)

    def getRosterAverageFPTSseason(self):
        average_rosters = {}
        for player in self.roster.getRoster():
            scores = self.stats.player_box_scores_season(player,self.season)
            player_fpts = self.stats.calculate_average_fantasy_points(scores)
            average_rosters[player] = player_fpts
        return average_rosters

    def getRosterTotalFPTSseason(self):
        total_rosters = {}
        for player in self.roster.getRoster():
            scores = self.stats.player_box_scores_season(player,self.season)
            player_fpts = self.stats.calculate_total_fantasy_points(scores)
            total_rosters[player] = player_fpts
        return total_rosters