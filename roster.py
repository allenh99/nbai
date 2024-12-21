class Roster:

    def __init__(self, filename=None):
        self.roster = []
        self.players = []
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
    