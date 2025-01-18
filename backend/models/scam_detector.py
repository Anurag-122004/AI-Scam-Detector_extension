import joblib
import sys
import logging
import os

# Setup logging
logging.basicConfig(
    filename='scam_detector.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Log start of the script
logging.info("Starting scam_detector.py")

# Define paths relative to the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, '../../ai-model/scam_detector_model.pkl')
vectorizer_path = os.path.join(current_dir, '../../ai-model/vectorizer.pkl')
phishing_urls_path = os.path.join(current_dir, '../../ai-model/phishing_urls.pkl')

# Load the model, vectorizer, and phishing URLs
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)
phishing_urls = joblib.load(phishing_urls_path)

# Print the phishing URLs for debugging
# print("Phishing URLs:", phishing_urls)

def detect_scam(url):
    """Detect if the given URL is a scam."""
    # Check if the URL is in the list of phishing URLs
    if url in phishing_urls:
        return 1
    
    # If the URL is not in the phishing URLs list, classify it as legitimate
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scam_detector.py <url>")
        sys.exit(1)
    
    url = sys.argv[1]
    result = detect_scam(url)
    
    if result == 1:
        print(f"The URL '{url}' is likely a scam.")
    else:
        print(f"The URL '{url}' is likely legitimate.")
    
    # Log the result
    logging.info(f"URL: {url}, Prediction: {'Scam' if result == 1 else 'Legitimate'}")