const express = require('express');
const router = express.Router();
const { analyzeURL } = require('../models/scam_detector');

// Analyze URL
router.post('/analyze', async (req, res) => {
    try {
        const { url } = req.body;
        // console.log(url);
        if (!url) {
            return res.status(400).json({ error: 'URL is required' });
        }
        console.log(url);
        const isScam = await analyzeURL(url);
        res.json({ isScam });
        console.log(isScam);
    } catch (error) {
        console.error('Error in /analyze route:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

module.exports = router;
