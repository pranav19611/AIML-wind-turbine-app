import streamlit as st
import pandas as pd
import joblib

# Load the Random Forest model
rf_model = joblib.load('random_forest_model_compressed.pkl')

# Streamlit UI for user inputs
st.title("Wind Turbine Power Prediction")
st.write("Enter the feature values to predict active power.")

# Create input fields for user inputs
wind_speed = st.number_input("Enter wind speed (m/s):", value=0.0)
ambient_temp = st.number_input("Enter ambient temperature (°C):", value=0.0)
generator_speed = st.number_input("Enter generator speed (RPM):", value=0.0)
nacelle_temp = st.number_input("Enter nacelle temperature (°C):", value=0.0)
wind_direction = st.number_input("Enter wind direction (°):", value=0.0)
wind_turbulence = st.number_input("Enter wind turbulence (%):", value=0.0)
efficiency = st.number_input("Enter efficiency (%):", value=0.0)

# When the user clicks the Predict button
if st.button("Predict"):
    # Create a DataFrame from the user inputs
    new_data = pd.DataFrame({
        'wind_speed_raw': [wind_speed],
        'ambient_temperature': [ambient_temp],
        'generator_speed': [generator_speed],
        'nacelle_temp': [nacelle_temp],
        'wind_direction_raw': [wind_direction],
        'wind_speed_turbulence': [wind_turbulence],
        'efficiency': [efficiency]
    })

    # Make the prediction
    prediction = rf_model.predict(new_data)

    # Display the prediction
    st.success(f"Predicted Active Power: {prediction[0]:.2f}")
