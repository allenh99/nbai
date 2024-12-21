from basketball_reference_web_scraper import client
from datetime import datetime

class PlayerStats():

    def __init__(self):
        return
    
    #Generate player ids
    def generate_player(self,name,year):
        for i in client.players_season_totals(season_end_year=year):
            if i['name'] == name:
                return i['slug']

    
    #Generate Box Scores for given player for a season - returns list of box scores (dictionaries)
    def player_box_scores_season(self,name,y):
        id = self.generate_player(name,y)
        return client.regular_season_player_box_scores(
            player_identifier=id, 
            season_end_year=y
        )
    
    #Generate Box Scores for a given player for a month
    def player_box_scores_1month(self,name,start):
        m,d,y = start.split("/")
        date_string = y + "-" + m + "-" + d
        end_year = int(y) if int(m) < 8 else int(y)+1
        scores = [i for i in self.player_box_scores_season(name,end_year) if (datetime.strptime(date_string, "%Y-%m-%d").date() - i['date']).days < 30 and (datetime.strptime(date_string, "%Y-%m-%d").date() - i['date']).days > -1]
        return scores




s = PlayerStats()
