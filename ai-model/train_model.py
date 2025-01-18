import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load preprocessed data
data = pd.read_csv('./datasets/cleaned_phishing_dataset.csv')

# Print columns for debugging
print("Columns in the dataset:", data.columns)

# Check if required columns exist
if 'url' not in data.columns or 'label' not in data.columns:
    raise KeyError("The required columns 'url' and 'label' are not present in the dataset.")

# Handle missing values
data = data.dropna(subset=['url', 'label'])

# Extract features and labels
X = data['url']
y = data['label']

# Save the list of phishing URLs
phishing_urls = set(data[data['label'] == 1]['url'])
joblib.dump(phishing_urls, 'phishing_urls.pkl')

# Vectorize URLs
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X.astype(str))

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy}")
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save model and vectorizer
joblib.dump(model, 'scam_detector_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Model trained and saved!")