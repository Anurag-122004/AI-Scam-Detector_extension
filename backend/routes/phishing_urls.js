const express = require('express');
const router = express.Router();
const fs = require('fs');
const path = require('path');

// Load phishing URLs from the CSV file
const csvFilePath = path.join(__dirname, '../../ai-model/datasets/cleaned_phishing_dataset.csv');
const phishingUrls = [];

fs.readFileSync(csvFilePath, 'utf-8')
    .split('\n')
    .forEach(line => {
        const [url, label] = line.split(',');
        if (label && label.trim() === '1') {
            phishingUrls.push(url.trim());
        }
    });

// Endpoint to get phishing URLs
router.get('/phishing_urls', (req, res) => {
    res.json(phishingUrls);
});

module.exports = router;