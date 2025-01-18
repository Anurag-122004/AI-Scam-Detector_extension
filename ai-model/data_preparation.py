import pandas as pd
import os

# Step 1: Read the .lst file
file_path = '../datasets/ALL-phishing-links.lst'
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Step 2: Parse the contents
data = []
for line in lines:
    url = line.strip()
    label = 1  # Assign a default label for phishing
    data.append((url, label))

# Step 3: Convert to a DataFrame
df = pd.DataFrame(data, columns=['url', 'label'])

# Step 4: Handle missing values
# Check for missing values
missing_values = df.isnull().sum().sum()
print("Missing values:\n", df.isnull().sum())

# Drop rows with missing values (if few) or fill them
if missing_values > 0:  # Check if there are any missing values
    print("Dropping rows with missing values...")
    df = df.dropna()  # Drop rows with missing values
else:
    print("No missing values found!")

# Step 5: Standardize column names
# Convert column names to lowercase, replace spaces with underscores, and strip extra whitespace
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_', regex=False)
print("Standardized column names:", df.columns)

# Step 6: Save the cleaned dataset
output_dir = './datasets'
output_file = os.path.join(output_dir, 'cleaned_phishing_dataset.csv')

# Ensure the directory exists before saving
os.makedirs(output_dir, exist_ok=True)

df.to_csv(output_file, index=False)
print(f"Cleaned dataset saved to {output_file}")

# Final dataset preview
print("Preview of the cleaned dataset:")
print(df.head())