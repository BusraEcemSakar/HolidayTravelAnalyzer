import pandas as pd

def analyze_travel(filepath):
    data = pd.read_csv(filepath)
    # Further analysis based on SQL output
    return data

if __name__ == "__main__":
    sql_output_path = '../data/processed/location_analysis.csv'
    analysis_output_path = '../data/processed/travel_analysis.csv'
    data = analyze_travel(sql_output_path)
    data.to_csv(analysis_output_path, index=False)
    print("Travel analysis saved to 'travel_analysis.csv'.")
