import React from 'react';

function ResultComponent({ loading, error, finalDecision }) {
    return (
        <div style={{ marginTop: '20px', padding: '10px', border: '1px solid #ddd', borderRadius: '5px', backgroundColor: '#f9f9f9' }}>
            {loading && <p>Loading...</p>}
            {error && <p style={{ color: 'red' }}>Error: {error}</p>}
            {finalDecision && <p><strong>Final Decision:</strong> {finalDecision}</p>}
        </div>
    );
}

export default ResultComponent;
