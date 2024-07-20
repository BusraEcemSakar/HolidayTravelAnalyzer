# HolidayTravelAnalyzer
# User Location Analysis Project

This project aims to analyze user location data to identify travel patterns, specifically to determine whether users are going on holiday or returning home. The project involves generating synthetic data, cleaning it, performing SQL-based analysis, and visualizing the results.


### Generate Synthetic Data

Run the script to create synthetic user location data:

python src/create_data.py
This will generate a CSV file with synthetic data in data/raw/user_locations.csv.


### Clean Data

Clean the generated data:

python src/data_preparation.py
This will produce a cleaned CSV file in data/processed/clean_user_locations.csv.


### Analyze Location Data

Perform SQL-based analysis to identify travel patterns:

python src/location_analysis.py
The analysis results will be saved to data/processed/location_analysis.csv.


### Analyze Travel

Further analyze the SQL output to determine travel types:

python src/travel_analysis.py
The travel analysis will be saved to data/processed/travel_analysis.csv.


### Visualize Results

Visualize the travel patterns using Folium:

python src/visualization.py
The visualization will be saved to visualizations/travel_patterns.html.


### Project Components

Data Generation
The script create_data.py generates synthetic user location data with random timestamps, latitude, and longitude values.

Data Cleaning
The script data_preparation.py cleans the generated data by removing any rows with missing or zero values for latitude and longitude.

SQL Analysis
The script location_analysis.py performs SQL-based analysis on the cleaned data to calculate the distance traveled and identify travel patterns. It uses an in-memory SQLite database to execute the queries.

Travel Analysis
The script travel_analysis.py further analyzes the SQL output to classify travel types such as 'back from holiday' or 'going to holiday'.

Visualization
The script visualization.py creates a map visualization of the travel patterns using Folium.

Results
The project results include:

Cleaned user location data (data/processed/clean_user_locations.csv)
Location analysis results (data/processed/location_analysis.csv)
Travel analysis results (data/processed/travel_analysis.csv)
Travel patterns map (visualizations/travel_patterns.html)
