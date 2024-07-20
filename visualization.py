import pandas as pd
import folium

def visualize_travel(filepath):
    data = pd.read_csv(filepath)
    map = folium.Map(location=[41.102458, 29.052961], zoom_start=6)
    for _, row in data.iterrows():
        folium.Marker(location=[row['lat'], row['lng']], popup=row['travel_type']).add_to(map)
    return map

if __name__ == "__main__":
    travel_analysis_path = '../data/processed/travel_analysis.csv'
    map = visualize_travel(travel_analysis_path)
    map.save('../visualizations/travel_patterns.html')
    print("Travel patterns map saved to 'travel_patterns.html'.")
