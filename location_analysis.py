import pandas as pd
from sqlalchemy import create_engine

def analyze_location_data(filepath):
    # Create a database connection
    engine = create_engine('sqlite:///:memory:')
    data = pd.read_csv(filepath)
    data.to_sql('user_locations', engine, index=False)

    query = """
    WITH dailyavg AS (
        SELECT session_id, timestamp_date, AVG(lat) AS lat, AVG(lng) AS lng
        FROM user_locations
        GROUP BY session_id, timestamp_date
    )
    SELECT 
        session_id,
        timestamp_date,
        lat,
        lng,
        LAG(lat, 1) OVER (PARTITION BY session_id ORDER BY session_id, timestamp_date) AS lag_lat,
        LAG(lng, 1) OVER (PARTITION BY session_id ORDER BY session_id, timestamp_date) AS lag_lng,
        f_great_circle_distance(lat, lng, lag_lat, lag_lng) / 1000.0 AS distance_traveled_km,
        f_great_circle_distance(lat, lng, 41.102458, 29.052961) / 1000.0 AS distancetoist,
        CASE
            WHEN distance_traveled_km >= 150 THEN 'travel'
            WHEN distance_traveled_km < 150 THEN 'nontravel'
        END AS activity_type,
        CASE
            WHEN activity_type='travel' AND distancetoist <= 100 THEN 'backfromholiday'
            WHEN activity_type='travel' AND distancetoist > 100 THEN 'gotoholiday'
        END AS travel_type
    FROM dailyavg
    ORDER BY session_id, timestamp_date;
    """

    result = pd.read_sql(query, engine)
    return result

if __name__ == "__main__":
    clean_data_path = '../data/processed/clean_user_locations.csv'
    analysis_output_path = '../data/processed/location_analysis.csv'
    analyzed_data = analyze_location_data(clean_data_path)
    analyzed_data.to_csv(analysis_output_path, index=False)
    print("Location analysis saved to 'location_analysis.csv'.")
