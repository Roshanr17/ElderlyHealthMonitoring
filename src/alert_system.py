def generate_alerts(data, model):
    features = data[["HR_dev", "Sleep_dev", "Steps_dev", "Stress_dev"]]
    data["Anomaly"] = model.predict(features)

    def alert(row):
        if row["Anomaly"] == -1:
            return "Emergency"
        elif abs(row["HR_dev"]) > 10:
            return "Warning"
        else:
            return "Normal"

    data["Alert"] = data.apply(alert, axis=1)
    return data