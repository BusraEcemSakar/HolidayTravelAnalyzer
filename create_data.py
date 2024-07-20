import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Parameters
num_records = 1000
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
lat_range = (35.0, 45.0)
lng_range = (-120.0, -70.0)

# Helper functions
def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

def random_coordinates(lat_range, lng_range):
    return round(random.uniform(*lat_range), 6), round(random.uniform(*lng_range), 6)

# Generate data
data = []
for i in range(num_records):
    session_id = f'S{i+1:03d}'
    user_id = random.randint(1, 500)
    timestamp = random_date(start_date, end_date)
    timestamp_date = timestamp.date()
    lat, lng = random_coordinates(lat_range, lng_range)

    data.append([session_id, user_id, timestamp, timestamp_date, lat, lng])

# Create DataFrame
columns = ['session_id', 'user_id', 'timestamp', 'timestamp_date', 'lat', 'lng']
location_data = pd.DataFrame(data, columns=columns)

# Save to CSV
location_data.to_csv('../data/raw/user_locations.csv', index=False)

print("Synthetic user location data created and saved as 'user_locations.csv'.")
