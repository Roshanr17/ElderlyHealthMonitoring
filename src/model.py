from sklearn.ensemble import IsolationForest
import joblib

def train_model(data):
    features = data[["HR_dev", "Sleep_dev", "Steps_dev", "Stress_dev"]]

    model = IsolationForest(contamination=0.05)
    model.fit(features)

    joblib.dump(model, "model.pkl")
    return model