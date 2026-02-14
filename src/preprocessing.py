import pandas as pd

def preprocess():
    # Load dataset
    data = pd.read_csv("data/health_data.csv")
    
    # Convert Date column to datetime
    data["Date"] = pd.to_datetime(data["Date"])
    
    # Create personalized baseline (average of first 30 days)
    baseline = data.iloc[:30].mean(numeric_only=True)
    
    # Create deviation features
    data["HR_dev"] = data["HeartRate"] - baseline["HeartRate"]
    data["Sleep_dev"] = data["SleepHours"] - baseline["SleepHours"]
    data["Steps_dev"] = data["Steps"] - baseline["Steps"]
    data["Stress_dev"] = data["StressLevel"] - baseline["StressLevel"]
    
    # Return processed data
    return data