import sys
from agents.manager_agent import managerAgent

player = sys.argv[1]
ou = "o" if sys.argv[2].lower() == "over" else "u"
number = sys.argv[3]
stat_type = sys.argv[4]
opp = sys.argv[5]

#{'player': 'Josh Hart', 'ou': 'o', 'number': '8.5', 'stat_type': 'rebounds', 'opp': 'Toronto Raptors'}

run_data = {
    'player':player,
    'ou':ou,
    'number':number,
    'stat_type':stat_type,
    'opp':opp
}

managerAgent()