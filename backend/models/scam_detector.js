const { exec } = require('child_process');
const path = require('path');
const fs = require('fs');

// Function to log messages to a dedicated log file
const logMessage = (message) => {
    const logFilePath = path.resolve(__dirname, './scam_detector.log');
    const timestamp = new Date().toISOString();
    const logEntry = `${timestamp} - ${message}\n`;

    // Append the log entry to the log file
    fs.appendFile(logFilePath, logEntry, (err) => {
        if (err) {
            console.error('Error writing to log file:', err);
        }
    });
};

const analyzeURL = async (url) => {
    const scriptPath = path.resolve(__dirname, './scam_detector.py');
    return new Promise((resolve, reject) => {
        // Log the incoming URL for analysis
        logMessage(`Received URL for analysis: ${url}`);

        // Execute the Python script with the provided URL
        exec(`python ${scriptPath} ${url}`, (error, stdout, stderr) => {
            if (error) {
                const errorMessage = `Execution error: ${error.message}`;
                logMessage(errorMessage);
                reject(new Error(errorMessage));
            } else if (stderr) {
                const stderrMessage = `Python script error: ${stderr}`;
                logMessage(stderrMessage);
                reject(new Error(stderrMessage));
            } else {
                const result = stdout.trim();
                logMessage(`Python script result for '${url}': ${result}`);
                resolve(result === 'The URL \'' + url + '\' is likely a scam.');
            }
        });
    });
};

module.exports = { analyzeURL };