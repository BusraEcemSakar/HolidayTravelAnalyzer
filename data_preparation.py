import pandas as pd

def clean_data(filepath):
    data = pd.read_csv(filepath)
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data = data.dropna(subset=['lat', 'lng'])
    data = data[(data['lat'] != 0) & (data['lng'] != 0)]
    return data

if __name__ == "__main__":
    raw_data_path = '../data/raw/user_locations.csv'
    clean_data_path = '../data/processed/clean_user_locations.csv'
    data = clean_data(raw_data_path)
    data.to_csv(clean_data_path, index=False)
    print("Cleaned data saved to 'clean_user_locations.csv'.")
