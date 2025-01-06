import React, { useState } from 'react';
import FormComponent from './components/form';
import ResultComponent from './components/result';

function App() {
    const [formData, setFormData] = useState({
        player: '',
        ou: 'o',
        number: '',
        stat_type: 'rebounds',
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

            if (data.final_decision) {
                setFinalDecision(data.final_decision);
            } else {
                setError('No final decision found in the response.');
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
            <FormComponent formData={formData} handleChange={handleChange} handleSubmit={handleSubmit} />
            <ResultComponent loading={loading} error={error} finalDecision={finalDecision} />
        </div>
    );
}

export default App;
