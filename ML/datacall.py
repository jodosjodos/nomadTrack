import requests
import pandas as pd

# Function to fetch data from the API
def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()  # Return JSON data
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return []
    except ValueError as e:
        print(f"JSON decode error: {e}")
        return []

# API endpoints
travels_url = 'http://localhost:8000/list/'
checklists_url = 'http://localhost:8000/checklist/list/'

# Fetch data from the endpoints
travels_data = fetch_data(travels_url)
checklists_data = fetch_data(checklists_url)

# Convert to Pandas DataFrames
travels_df = pd.DataFrame(travels_data)
checklists_df = pd.DataFrame(checklists_data)

# Forward fill null values
travels_df = travels_df.ffill().bfill()  # Fill missing values forward and backward
checklists_df = checklists_df.ffill().bfill()

# Print DataFrames
print("Travels DataFrame:")
print(travels_df.head())

print("\nChecklists DataFrame:")
print(checklists_df.head())

# Merge travels and checklists if they share a relationship (assuming 'id' and 'checklists' are related)
merged_df = pd.merge(
    travels_df,
    checklists_df,
    left_on='id',  # Adjust based on your models
    right_on='id',  # Adjust based on your models
    how='left'
)

# Print merged DataFrame
print("\nMerged DataFrame:")
print(merged_df.head())
