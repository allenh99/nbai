from playstats import PlayerStats,PlayerIDGenerator
from roster import RosterStats

generator = PlayerIDGenerator(2025)
generator.generate_player_ids('players.txt')

s = RosterStats("roster.txt")
print(s.roster.getRoster())
print(s.getRosterAverageFPTSseason())