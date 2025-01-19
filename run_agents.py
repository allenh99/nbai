import sys
from agents.manager_agent import managerAgent
from agents.boxscore_agent import boxScoreAgent
from agents.opp_agent import oppAgent



player = sys.argv[1] + " " + sys.argv[2]
ou = "o" if sys.argv[3].lower() == "over" else "u"
number = float(sys.argv[4])
stat_type = sys.argv[5]
opp = sys.argv[6] + " " + sys.argv[7]

#{'player': 'Josh Hart', 'ou': 'o', 'number': '8.5', 'stat_type': 'rebounds', 'opp': 'Toronto Raptors'}

run_data = {
    'player':player,
    'ou':ou,
    'number':number,
    'stat_type':stat_type,
    'opp':opp
}

agents = {
    "box_score_agent": boxScoreAgent,
    "opp_agent": oppAgent
}

res = managerAgent(run_data,agents)