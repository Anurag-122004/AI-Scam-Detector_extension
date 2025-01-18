chrome.runtime.onInstalled.addListener(async () => {
    console.log('Extension installed.');
    await updateRules();
});

chrome.runtime.onStartup.addListener(async () => {
    console.log('Extension started.');
    await updateRules();
});

async function updateRules() {
    const response = await fetch('http://localhost:8080/api/phishing_urls');
    const phishingUrls = await response.json();

    const rules = phishingUrls.map((url, index) => ({
        id: index + 1,
        priority: 1,
        action: { type: 'block' },
        condition: { urlFilter: url, resourceTypes: ['main_frame'] }
    }));

    chrome.declarativeNetRequest.updateDynamicRules({
        removeRuleIds: rules.map(rule => rule.id),
        addRules: rules
    });

    console.log('Rules updated:', rules);
}