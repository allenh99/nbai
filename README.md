# NBAi 🏀

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-18.0%2B-61DAFB)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey)](https://flask.palletsprojects.com/)

NBAi is an intelligent sports analytics platform that leverages NBA APIs and LLM agents to predict player performance over/under statistics. The platform consists of a modern web interface and a powerful backend prediction system.

## ✨ Features

- **Intuitive User Interface**: Clean and responsive form for easy player data input
- **Real-Time Predictions**: Instant over/under predictions powered by advanced analytics
- **Dual-Agent System**:
  - Boxscore Agent: Analyzes player historical performance across multiple timeframes
  - Opponent Agent: Evaluates opponent team statistics and defensive metrics

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Node.js and npm
- NBA API credentials

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/nbai.git
cd nbai
```

2. Install backend dependencies:
```bash
pip install -r requirements.txt
```

3. Install frontend dependencies:
```bash
cd bball-stats-frontend
npm install
```

### Running the Application

#### Frontend
```bash
npm start --prefix bball-stats-frontend
```

#### Backend
```bash
python backend.py
```

### Command Line Usage

You can also use the prediction system directly from the command line:

```bash
python run_agents.py {Player Name} {o/u} {number} {stat type} {opposing team}
```

Example:
```bash
python run_agents.py Josh Hart o 8.5 rebounds Toronto Raptors
```

## 🛠️ Technology Stack

### Backend
- **Flask**: Lightweight web framework for Python
- **Flask-CORS**: Cross-origin resource sharing support
- **nba_api**: Official NBA statistics API wrapper
- **basketball_reference_web_scraper**: Basketball Reference data extraction

### Frontend
- **React**: Modern UI library for building interactive interfaces
- **Bootstrap**: Responsive CSS framework for consistent styling

## 📚 APIs used

- [NBA API Documentation](https://github.com/swar/nba_api)
- [Basketball Reference Web Scraper](https://github.com/jaebradley/basketball_reference_web_scraper)