import streamlit as st
from src.preprocessing import preprocess
from src.model import train_model
from src.alert_system import generate_alerts

# Title
st.title("Elderly Health Monitoring System")

# Load and process data
data = preprocess()

# Train model
model = train_model(data)

# Generate alerts
data = generate_alerts(data, model)

# Show latest data
st.subheader("Latest Health Records")
st.write(data.tail(20))

# Show anomalies only
st.subheader("Detected Health Alerts")
alerts = data[data["Alert"] != "Normal"]
st.write(alerts)