import pandas as pd
from datetime import datetime
import csv

# List to store weather data
weather_data = []
# Set to keep track of unique dates
recorded_dates = set()

# Function to validate date format
def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Function to add weather data
def add_weather_data():
    date = input("Enter date (YYYY-MM-DD): ")
    if not validate_date(date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    if date in recorded_dates:
        print("This date has already been recorded.")
        return

    try:
        temperature = float(input("Enter temperature (°C): "))
    except ValueError:
        print("Invalid temperature input.")
        return

    condition = input("Enter weather condition (e.g., Sunny, Rainy, Cloudy): ")
    
    weather_data.append({
        'Date': date,
        'Temperature': temperature,
        'Condition': condition
    })
    recorded_dates.add(date)
    print("Weather data added successfully.")

# Function to view data
def view_data():
    if not weather_data:
        print("No data recorded yet.")
        return
    df = pd.DataFrame(weather_data)
    print("\nRecorded Weather Data:")
    print(df)

# Function to summarize and export data
def summarize_and_export():
    if not weather_data:
        print("No data to summarize or export.")
        return

    df = pd.DataFrame(weather_data)
    avg_temp = df['Temperature'].mean()
    condition_counts = df['Condition'].value_counts()

    print("\nSummary:")
    print(f"Average Temperature: {avg_temp:.2f}°C")
    print("Weather Condition Counts:")
    print(condition_counts)

    # Export to CSV
    df.to_csv('weather_report.csv', index=False)
    print("Data exported to 'weather_report.csv'.")

# Menu system
def main():
    while True:
        print("\n---- Weather Data Recorder ----")
        print("1. Add Weather Data")
        print("2. View Recorded Data")
        print("3. Summarize & Export to CSV")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_weather_data()
        elif choice == '2':
            view_data()
        elif choice == '3':
            summarize_and_export()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
