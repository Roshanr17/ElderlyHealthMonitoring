import pandas as pd
import numpy as np

def generate_data():
    np.random.seed(42)
    dates = pd.date_range(start="2025-01-01", periods=180)

    data = pd.DataFrame({
        "Date": dates,
        "HeartRate": np.random.normal(72, 5, 180),
        "SleepHours": np.random.normal(7, 0.8, 180),
        "Steps": np.random.normal(6000, 1000, 180),
        "StressLevel": np.random.normal(3, 0.5, 180)
    })

    # Add anomalies
    data.loc[50, "HeartRate"] = 115
    data.loc[120, "SleepHours"] = 3

    data.to_csv("data/health_data.csv", index=False)