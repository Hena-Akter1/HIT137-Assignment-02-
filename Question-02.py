import pandas as pd
import glob
import os

def load_data(folder_path):
    # Load all CSV files from the specified folder 
    file_paths = glob.glob(os.path.join(folder_path, '*.csv'))
    data_frames = []
    for file in file_paths:
        df = pd.read_csv(file)
        if not df.empty:
            data_frames.append(df)
    if data_frames:
        return pd.concat(data_frames, ignore_index=True)
    else:
        raise ValueError("No valid CSV files to process.")

def calculate_monthly_and_seasonal_averages(df):
    # Monthly columns specified in the given dataset
    monthly_columns = ['January', 'February', 'March', 'April', 'May', 'June', 
      'July', 'August', 'September', 'October', 'November', 'December']
    
    # Mapping months to seasons
    seasons = {
        'Winter': ['June', 'July', 'August'],
        'Spring': ['September', 'October', 'November'],
        'Summer': ['December', 'January', 'February'],
        'Autumn': ['March', 'April', 'May']
    }

    # Calculate seasonal averages & the average for each month
    seasonal_avg = pd.Series({season: df[months].mean().mean() for season, months in seasons.items()})
     
    monthly_avg = df[monthly_columns].mean()

    # Save the results in CSV & TXT files
    monthly_avg.to_csv('monthly_averages.csv', header=['Average Temperature'])
    seasonal_avg.to_csv('average_temp.txt', header=['Average Temperature'])

def main():
    folder_path = r"C:/Users/User/Downloads/HIT137 Assignment 2 SS 2024/temperature_data"
    df = load_data(folder_path)
    
    calculate_monthly_and_seasonal_averages(df)
    find_extreme_temperatures(df)
    print("Analysis completed. Results are saved to files.")

if _name_ == "_main_":
    main()
