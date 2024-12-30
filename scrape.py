from agents.boxscore_agent import boxScoreAgent

# boxScoreAgent({"player":"Josh Hart","o/u":"o","number":"8.5","stat_type":"rebounds","opp":"Washington Wizards"})

from basketball_reference_web_scraper import client
print(client.team_box_scores(day=28,month=12,year=2024))