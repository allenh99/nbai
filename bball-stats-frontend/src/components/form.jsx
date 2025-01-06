import React from 'react';

function FormComponent({ formData, handleChange, handleSubmit }) {
    return (
        <form onSubmit={handleSubmit} style={{ marginBottom: '20px' }}>
            {/* Player Name */}
            <div style={{ marginBottom: '10px' }}>
                <label>Player Name: </label>
                <input
                    type="text"
                    name="player"
                    value={formData.player}
                    onChange={handleChange}
                    required
                />
            </div>

            {/* Over/Under */}
            <div style={{ marginBottom: '10px' }}>
                <label>Over/Under (o/u): </label>
                <select
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
            <div style={{ marginBottom: '10px' }}>
                <label>Number: </label>
                <input
                    type="number"
                    name="number"
                    value={formData.number}
                    onChange={handleChange}
                    required
                />
            </div>

            {/* Stat Type */}
            <div style={{ marginBottom: '10px' }}>
                <label>Stat Type: </label>
                <select
                    name="stat_type"
                    value={formData.stat_type}
                    onChange={handleChange}
                    required
                >
                    <option value="rebounds">Rebounds</option>
                    <option value="points">Points</option>
                    <option value="assists">Assists</option>
                    <option value="steals">Steals</option>
                    <option value="blocks">Blocks</option>
                </select>
            </div>

            {/* Opposing Team */}
            <div style={{ marginBottom: '10px' }}>
                <label>Opposing Team: </label>
                <input
                    type="text"
                    name="opp"
                    value={formData.opp}
                    onChange={handleChange}
                    required
                />
            </div>

            <button type="submit" style={{ padding: '10px 20px', fontSize: '16px' }}>
                Submit
            </button>
        </form>
    );
}

export default FormComponent;
