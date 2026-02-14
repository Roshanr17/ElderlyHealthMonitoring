import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("Elderly Health Monitoring System")

st.write("Enter patient health details:")

# 👇 USER INPUT FIELDS
heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=180, value=70)
temperature = st.number_input("Body Temperature (°F)", min_value=95.0, max_value=110.0, value=98.6)
blood_pressure = st.number_input("Blood Pressure (mmHg)", min_value=80, max_value=200, value=120)

# Convert to array for prediction
input_data = np.array([[heart_rate, temperature, blood_pressure]])

# Button to check health
if st.button("Check Health Status"):
    prediction = model.predict(input_data)

    if prediction[0] == -1:
        st.error("⚠️ Abnormal Health Condition Detected!")
    else:
        st.success("✅ Health is Normal")