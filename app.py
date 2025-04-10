import streamlit as st
import pandas as pd
import joblib

#load model
model = joblib.load("SPACE_weather_model.pkl")

#streamlit UI
st.title("🚀 Space Weather Prediction App")
st.write("Enter space weather parameters to predict solar wind speed.")

#user input fields
density = st.number_input("Plasma Density(P/cm3)", min_value = 0.0, step = 0.1)
temperature = st.number_input("Plasma Temperature (K)", min_value = 0.0, step=100.0)
hour = st.slider("Hour of the Day", 0, 23, 12)
day = st.slider("Day of the Month", 1, 31, 15)

# Prepare input data
input_data = pd.DataFrame([[density, temperature, hour, day]], columns=["density", "temperature", "hour", "day"])

# Predict
if st.button("Predict"):
    predicted_speed = model.predict(input_data)
    st.success(f"🌬️ Predicted Solar Wind Speed: {predicted_speed[0]:.2f} km/s")

