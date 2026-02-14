import streamlit as st
import pickle
import numpy as np
import pandas as pd
from datetime import datetime

# ==============================
# PAGE SETTINGS
# ==============================
st.set_page_config(page_title="Elderly Health Monitoring", page_icon="🏥")

st.markdown("## 🏥 Smart Elderly Health Monitoring System")
st.markdown("---")

# ==============================
# SIMPLE LOGIN SYSTEM
# ==============================
st.sidebar.title("Login")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if username != "admin" or password != "1234":
    st.warning("Please login to continue")
    st.stop()

st.sidebar.success("Logged in successfully ✅")

# ==============================
# LOAD MODEL
# ==============================
model = pickle.load(open("model.pkl", "rb"))

st.write("### Enter Patient Health Details")

# ==============================
# USER INPUT FIELDS
# ==============================
heart_rate = st.number_input("Heart Rate (bpm)", 40, 180, 70)
temperature = st.number_input("Body Temperature (°F)", 95.0, 110.0, 98.6)
blood_pressure = st.number_input("Blood Pressure (mmHg)", 80, 200, 120)
oxygen = st.number_input("Oxygen Level (SpO2 %)", 70, 100, 98)
sugar = st.number_input("Blood Sugar Level", 70, 300, 120)

# ==============================
# PREDICTION INPUT
# ==============================
input_data = np.array([[heart_rate, temperature, blood_pressure, oxygen, sugar]])

# ==============================
# CHECK HEALTH BUTTON
# ==============================
if st.button("Check Health Status"):

    prediction = model.predict(input_data)

    # ==============================
    # RESULT DISPLAY
    # ==============================
    if prediction[0] == -1:
        st.error("🚨 Abnormal Health Condition Detected!")
        st.warning("⚠️ Alert sent to caretaker / doctor")

    else:
        st.success("✅ Patient condition is Normal & Stable")

    # ==============================
    # STORE DATA
    # ==============================
    record = pd.DataFrame({
        "Time": [datetime.now()],
        "Heart Rate": [heart_rate],
        "Temperature": [temperature],
        "Blood Pressure": [blood_pressure],
        "Oxygen": [oxygen],
        "Sugar": [sugar],
        "Result": ["Abnormal" if prediction[0] == -1 else "Normal"]
    })

    record.to_csv("health_records.csv", mode="a", header=False, index=False)

    st.success("📁 Record saved successfully")

    # ==============================
    # SHOW GRAPH
    # ==============================
    st.subheader("📊 Current Health Data")

    chart_data = pd.DataFrame({
        "Parameter": ["Heart Rate", "Temperature", "Blood Pressure", "Oxygen", "Sugar"],
        "Values": [heart_rate, temperature, blood_pressure, oxygen, sugar]
    })

    st.bar_chart(chart_data.set_index("Parameter"))

# ==============================
# SHOW PREVIOUS RECORDS
# ==============================
st.markdown("---")
st.subheader("📜 Patient History")

try:
    history = pd.read_csv("health_records.csv")
    st.dataframe(history.tail(10))
except:
    st.info("No records available yet.")