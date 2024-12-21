from basketball_reference_web_scraper import client
from datetime import datetime

class PlayerStats():
    values = {}

    def __init__(self):
        self.values = {"points":0.5,"assists":1,"rebounds":1,"turnovers":-1,"steals":2,"blocks":2,"3PM":0.5}
        return
    
    #Generate player ids
    def generate_player(self,name,year):
        for i in client.players_season_totals(season_end_year=year):
            if i['name'] == name:
                return i['slug']
    
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
        id = self.generate_player(name,y)
        return client.regular_season_player_box_scores(
            player_identifier=id, 
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


s = PlayerStats()
j3m = s.player_box_scores_3month("Josh Giddey","12/19/2024")
j1m = s.player_box_scores_1month("Josh Giddey","12/19/2024")
j1w = s.player_box_scores_1week("Josh Giddey","12/19/2024")
print(s.calculate_average_fantasy_points(j3m))
print(s.calculate_average_fantasy_points(j1m))
print(s.calculate_average_fantasy_points(j1w))
