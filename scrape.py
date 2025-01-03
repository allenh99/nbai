from agents.boxscore_agent import boxScoreAgent
from agents.opp_agent import oppAgent
from agents.manager_agent import managerAgent

#print(oppAgent({"player":"Josh Hart","o/u":"o","number":"8.5","stat_type":"rebounds","opp":"Miami Heat"}))
agents = {
    "box_score_agent": boxScoreAgent,
    "opp_agent": oppAgent
}
    
# Input data
data = {
    "player": "Josh Hart",
    "o/u": "o",
    "number": "8.5",
    "stat_type": "rebounds",
    "opp": "Washington Wizards"
}

# Run the manager agent
result = managerAgent(data, agents)
print(result)