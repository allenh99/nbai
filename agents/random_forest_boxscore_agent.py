from tools.playstats import PlayerIDGenerator, PlayerStats
from datetime import datetime
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

class BoxScorePredictor:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()
        self.is_trained = False
    
    def prepare_features(self, averages, stat_type):
        features = []
        for period in ["1week", "1month", "3month"]:
            period_avg = averages[period][stat_type]["average"]
            season_avg = averages["season"][stat_type]["average"]
            features.extend([period_avg, season_avg, period_avg - season_avg])
        return np.array(features).reshape(1, -1)
    
    def train(self, historical_data):
        X = []
        y = []
        for data in historical_data:
            features = self.prepare_features(data["averages"], data["stat_type"])
            X.append(features[0])
            y.append(1 if data["actual"] >= data["number"] else 0)
        
        X = np.array(X)
        X = self.scaler.fit_transform(X)
        self.model.fit(X, y)
        self.is_trained = True
    
    def predict(self, averages, stat_type, number):
        if not self.is_trained:
            raise ValueError("Model must be trained before making predictions")
        
        features = self.prepare_features(averages, stat_type)
        features = self.scaler.transform(features)
        probability = self.model.predict_proba(features)[0][1]
        return probability >= 0.5

current_date = datetime.now()
formatted_date = current_date.strftime("%m/%d/%Y")

# Initialize the predictor
predictor = BoxScorePredictor()

def mlBoxScoreAgent(data):
    """
    Machine Learning based boxscore prediction agent.
    Uses Random Forest to predict whether a player will go over or under a given stat line.
    
    Args:
        data (dict): Dictionary containing:
            - player: Player name
            - ou: "o" for over or "u" for under
            - number: Target number
            - stat_type: Type of stat to predict
    
    Returns:
        dict: Prediction results including performance comparison, message, and signal
    """
    player = data["player"]
    ou = data["ou"]
    number = float(data["number"])
    stat_type = data["stat_type"]

    generator = PlayerIDGenerator(2025)
    generator.generate_player_ids('players.txt')

    stats = PlayerStats()
    averages = stats.calculate_stat_averages(player, formatted_date)
    periods = ["1week", "1month", "3month"]

    performance_comparison = {}

    for period in periods:
        period_average = averages[period][stat_type]["average"]
        season_average = averages["season"][stat_type]["average"]

        if period_average > season_average:
            performance_comparison[period] = "better"
        elif period_average < season_average:
            performance_comparison[period] = "worse"
        else:
            performance_comparison[period] = "same"

    # Get prediction from Random Forest model
    score = predictor.predict(averages, stat_type, number)
    
    # Adjust prediction based on over/under
    if ou == "u":
        score = not score

    ret = 'over' if score else 'under'
    message = f"Based on Random Forest prediction, {ret} {number} for {stat_type} is expected."

    return {
        "data": performance_comparison, 
        "message": [message], 
        "signal": ret
    } 