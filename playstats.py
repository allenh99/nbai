from basketball_reference_web_scraper import client
from datetime import datetime

#PlayerIDGenerator(year) - used to produce player id map
class PlayerIDGenerator:
    def __init__(self, season_end_year):
        self.season_end_year = season_end_year

    def generate_player_ids(self, output_file):
        try:
            print(self.season_end_year)
            players = client.players_season_totals(season_end_year=self.season_end_year)
            with open(output_file, 'w') as file:
                for player in players:
                    name = player['name']
                    slug = player['slug']
                    file.write(f"{name},{slug}\n")
            print(f"Player IDs successfully written to {output_file}")
        except Exception as e:
            print(f"An error occurred: {e}")


#PlayerStats(fpt values,player id map) - gets player stats
class PlayerStats():

    def __init__(self,input_file='players.txt',values=None):
        default_values = {
            "points": 0.5,
            "assists": 1,
            "rebounds": 1,
            "turnovers": -1,
            "steals": 2,
            "blocks": 2,
            "3PM": 0.5,
        }
        self.player_ids = {}
        with open(input_file, 'r') as file:
            for line in file:
                name, slug = line.strip().split(",")  # Split by comma
                self.player_ids[name] = slug
        self.values = values if values else default_values
        
    #Calculate a players total FPTS given a box score
    def calculate_fantasy_points(self,box_score):
        return box_score['points_scored'] * self.values['points'] + \
        (box_score['offensive_rebounds'] + box_score['defensive_rebounds']) * self.values['rebounds'] + \
        box_score['assists'] * self.values['assists'] + \
        box_score['turnovers'] * self.values['turnovers'] + \
        box_score['steals'] * self.values['steals'] + \
        box_score['blocks'] * self.values['blocks'] + \
        box_score['made_three_point_field_goals'] * self.values['3PM']
    
    #Calculate total FPTS for a set of box scores
    def calculate_total_fantasy_points(self,box_scores):
        return sum([self.calculate_fantasy_points(i) for i in box_scores])

    #Calculate average FPTS for a set of box scores
    def calculate_average_fantasy_points(self,box_scores):
        return self.calculate_total_fantasy_points(box_scores=box_scores)/len(box_scores)
    
    #Generate Box Scores for given player for a season - returns list of box scores (dictionaries)
    def player_box_scores_season(self,name,y):
        return client.regular_season_player_box_scores(
            player_identifier=self.player_ids[name], 
            season_end_year=y
        )

    #Generate Box Scores for a given player for the last 90 days - returns list of box scores
    def player_box_scores_3month(self,name,start):
        m,d,y = start.split("/")
        date_string = y + "-" + m + "-" + d
        end_year = int(y) if int(m) < 8 else int(y)+1
        scores = [i for i in self.player_box_scores_season(name,end_year) if (datetime.strptime(date_string, "%Y-%m-%d").date() - i['date']).days <= 90 and (datetime.strptime(date_string, "%Y-%m-%d").date() - i['date']).days > -1]
        return scores
    
    #Generate Box Scores for a given player for a month span - returns list of box scores
    def player_box_scores_1month(self,name,start):
        m,d,y = start.split("/")
        date_string = y + "-" + m + "-" + d
        end_year = int(y) if int(m) < 8 else int(y)+1
        scores = [i for i in self.player_box_scores_season(name,end_year) if (datetime.strptime(date_string, "%Y-%m-%d").date() - i['date']).days <= 30 and (datetime.strptime(date_string, "%Y-%m-%d").date() - i['date']).days > -1]
        return scores

    #Generate Box Scores for a given player for the last 7 days - returns list of box scores
    def player_box_scores_1week(self,name,start):
        m,d,y = start.split("/")
        date_string = y + "-" + m + "-" + d
        end_year = int(y) if int(m) < 8 else int(y)+1
        scores = [i for i in self.player_box_scores_season(name,end_year) if (datetime.strptime(date_string, "%Y-%m-%d").date() - i['date']).days <= 7 and (datetime.strptime(date_string, "%Y-%m-%d").date() - i['date']).days > -1]
        return scores