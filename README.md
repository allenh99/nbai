# NBAi

This Sports Statline Agent leverages NBA APIs and LLM agents for predicting players over/under. Contains a frontend and backend app for predicting the over/under.

## Features

User-Friendly Interface: A simple and clean form where users can input player information.

Real-Time Predictions: Fetches the final decision from the Flask backend based on the provided data.

Currently uses two agents:\
Boxscore Agent: analyzes players historical data in different timeframes\
Opponent Agent: analyzes opponent season statistics

## Usage

To Start Frontend:

```console
npm start --prefix bball-stats-frontend
```

To Start Backend:

```console
python backend.py
```

## Technologies Used
Flask: Lightweight web framework for Python.\
Flask-CORS: Handles cross-origin requests.

React: Frontend library for building user interfaces.\
Bootstrap: CSS framework for responsive styling.

nba_api: https://github.com/swar/nba_api \
bbasketball_reference_web_scraper: https://github.com/jaebradley/basketball_reference_web_scraper