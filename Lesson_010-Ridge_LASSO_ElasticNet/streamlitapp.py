import streamlit as st
import pickle
import numpy as np

# Load model and scaler
ridge_model = pickle.load(open('ridge.pickle', 'rb'))
standard_scaler = pickle.load(open('scaler.pickle', 'rb'))

# Page config
st.set_page_config(page_title="Forest Fire Prediction", page_icon="🔥", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: orange;'>🔥 Forest Fire Prediction App</h1>", unsafe_allow_html=True)
st.write("This app predicts the **forest fire index** based on environmental factors. Fill the form below 👇")

# Input form
with st.form("fire_prediction_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        Temperature = st.number_input("🌡️ Temperature (°C)", value=25.0)
        RH = st.number_input("💧 Relative Humidity (%)", value=50.0)
        Ws = st.number_input("🌬️ Wind Speed (km/h)", value=5.0)

    with col2:
        Rain = st.number_input("🌧️ Rain (mm)", value=0.0)
        FFMC = st.number_input("🔥 FFMC Index", value=85.0)
        DMC = st.number_input("📊 DMC Index", value=20.0)

    with col3:
        ISI = st.number_input("⚡ ISI Index", value=5.0)
        Classes = st.number_input("🏷️ Classes", value=1.0)
        Region = st.number_input("🗺️ Region", value=1.0)

    # Submit button inside form
    submitted = st.form_submit_button("🚀 Predict")

# Prediction logic
if submitted:
    new_data_scaled = standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
    result = ridge_model.predict(new_data_scaled)

    st.markdown("---")
    st.subheader("✅ Prediction Result")
    st.success(f"🔥 Predicted Forest Fire Index: **{result[0]:.2f}**")
