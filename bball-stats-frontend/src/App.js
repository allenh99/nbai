import React, { useState } from 'react';

function App() {
    const [formData, setFormData] = useState({
        player: '',
        ou: 'o', // Default to 'o' (Over)
        number: '',
        stat_type: 'rebounds', // Default to 'rebounds'
        opp: ''
    });
    const [finalDecision, setFinalDecision] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);
        setFinalDecision(null);

        try {
            const res = await fetch('http://127.0.0.1:5000/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });

            if (!res.ok) {
                throw new Error(`Error: ${res.statusText}`);
            }

            const data = await res.json();

            // Extract "final_decision" from the response
            if (data.final_decision) {
                setFinalDecision(data.final_decision);
            } else {
                setError("No final decision found in the response.");
            }
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ fontFamily: 'Arial, sans-serif', padding: '20px' }}>
            <h1>Player Stats Query</h1>
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

            {/* Response Output */}
            <div style={{ marginTop: '20px', padding: '10px', border: '1px solid #ddd', borderRadius: '5px', backgroundColor: '#f9f9f9' }}>
                {loading && <p>Loading...</p>}
                {error && <p style={{ color: 'red' }}>Error: {error}</p>}
                {finalDecision && <p><strong>Final Decision:</strong> {finalDecision}</p>}
            </div>
        </div>
    );
}

export default App;
