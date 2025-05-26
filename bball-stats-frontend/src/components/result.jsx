import React from 'react';
import './FormComponent.css';

function ResultComponent({ loading, error, finalDecision }) {
    // Split the final decision into two parts: "Final Signal" and "Reasoning"
    const [finalSignal, reasoning] = finalDecision
        ? finalDecision.split('Reasoning:')
        : [null, null];

    return (
        <div className="result-container fade-in">
            <h2>Prediction Results</h2>

            {/* Show loading message */}
            {loading && (
                <div className="loading-message">
                    <div className="loading-spinner"></div>
                    <p>Analyzing player statistics...</p>
                </div>
            )}

            {/* Show error message */}
            {error && (
                <div className="error-message">
                    <p>⚠️ {error}</p>
                </div>
            )}

            {/* Show final decision */}
            {finalSignal && (
                <div className="final-decision">
                    <div className="signal-section">
                        <h3>Final Signal</h3>
                        <p className="signal">{finalSignal.trim()}</p>
                    </div>
                    <div className="reasoning-section">
                        <h3>Analysis</h3>
                        <p>{reasoning.trim()}</p>
                    </div>
                </div>
            )}

            {/* Show placeholder if no result */}
            {!loading && !error && !finalDecision && (
                <div className="no-result">
                    <p>Enter player details above to get started</p>
                </div>
            )}
        </div>
    );
}

export default ResultComponent;



