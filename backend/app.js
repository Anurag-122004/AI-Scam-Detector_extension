const express = require('express');
const bodyParser = require('body-parser');
const analysisRouter = require('./routes/analysis');
const phishingUrlsRouter = require('./routes/phishing_urls');

const app = express();
const port = process.env.PORT || 8080;

// Middleware
app.use(bodyParser.json());

// Routes
app.use('/api', analysisRouter);
app.use('/api', phishingUrlsRouter);

// Start the server
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});