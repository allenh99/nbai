import './FormComponent.css';

function FormComponent({ formData, handleChange, handleSubmit }) {
    return (
        <form onSubmit={handleSubmit} className="form-container">
            <h2>Predict</h2>

            {/* Player Name */}
            <div className="form-group">
                <label htmlFor="player">Player Name</label>
                <input
                    type="text"
                    id="player"
                    name="player"
                    value={formData.player}
                    onChange={handleChange}
                    required
                    placeholder="Enter player name"
                />
            </div>

            {/* Over/Under */}
            <div className="form-group">
                <label htmlFor="ou">Over/Under (o/u)</label>
                <select
                    id="ou"
                    name="ou"
                    value={formData.ou}
                    onChange={handleChange}
                    required
                >
                    <option value="o">Over</option>
                    <option value="u">Under</option>
                </select>
            </div>

            {/* Number */}
            <div className="form-group">
                <label htmlFor="number">Number</label>
                <input
                    type="number"
                    id="number"
                    name="number"
                    value={formData.number}
                    onChange={handleChange}
                    required
                    placeholder="Enter a number"
                />
            </div>

            {/* Stat Type */}
            <div className="form-group">
                <label htmlFor="stat_type">Stat Type</label>
                <select
                    id="stat_type"
                    name="stat_type"
                    value={formData.stat_type}
                    onChange={handleChange}
                    required
                >
                    <option value="points">Points</option>
                    <option value="rebounds">Rebounds</option>
                    <option value="assists">Assists</option>
                    <option value="steals">Steals</option>
                    <option value="blocks">Blocks</option>
                </select>
            </div>

            {/* Opposing Team */}
            <div className="form-group">
                <label htmlFor="opp">Opposing Team</label>
                <input
                    type="text"
                    id="opp"
                    name="opp"
                    value={formData.opp}
                    onChange={handleChange}
                    required
                    placeholder="Enter opposing team name"
                />
            </div>

            {/* Submit Button */}
            <button type="submit" className="form-button">
                Submit
            </button>
        </form>
    );
}

export default FormComponent;
