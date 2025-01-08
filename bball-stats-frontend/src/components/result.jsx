import React from 'react';
import './FormComponent.css';

function ResultComponent({ loading, error, finalDecision }) {
    // Split the final decision into two parts: "Final Signal" and "Reasoning"
    const [finalSignal, reasoning] = finalDecision
        ? finalDecision.split('Reasoning:')
        : [null, null];

    return (
        <div className="container result-container">
            <h2>Results</h2>

            {/* Show loading message */}
            {loading && <p className="loading-message">Loading...</p>}

            {/* Show error message */}
            {error && <p className="error-message">Error: {error}</p>}

            {/* Show final decision */}
            {finalSignal && (
                <div className="final-decision">
                    <p>
                        <strong>Final Signal:</strong> {finalSignal.trim()}
                    </p>
                    <p>
                        <strong>Reasoning:</strong> {reasoning.trim()}
                    </p>
                </div>
            )}

            {/* Show placeholder if no result */}
            {!loading && !error && !finalDecision && (
                <p className="no-result">No result to display yet.</p>
            )}
        </div>
    );
}

export default ResultComponent;



