document.getElementById('analyzeButton').addEventListener('click', async () => {
    const urlInput = document.getElementById('urlInput').value.trim();
    const resultDiv = document.getElementById('result');

    if (!urlInput) {
        resultDiv.textContent = 'Please enter a valid URL.';
        return;
    }

    resultDiv.textContent = 'Analyzing...';

    try {
        const response = await fetch('http://localhost:8080/api/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: urlInput }),
        });

        if (!response.ok) {
        throw new Error('Failed to analyze the URL.');
        }

        const data = await response.json();
        resultDiv.textContent = data.isScam
        ? '⚠️ Warning: This URL is likely a scam!'
        : '✅ Safe: No scam detected.';
    } catch (error) {
        resultDiv.textContent = `Error: ${error.message}`;
    }
    });
