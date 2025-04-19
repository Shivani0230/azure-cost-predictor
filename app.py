import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('models/cost_predictor.joblib')

st.title("Simulated Azure Cost Predictor")

# User inputs
day = st.slider("Day", 1, 31, 15)
month = st.slider("Month", 1, 12, 4)
dow = st.slider("Day of Week (0 = Monday)", 0, 6, 3)
lag1 = st.number_input("Yesterday's Cost", value=50.0)
lag7 = st.number_input("Cost 7 Days Ago", value=48.0)

# Predict button
if st.button("Predict Cost"):
    X = pd.DataFrame([[day, month, dow, lag1, lag7]], columns=['day', 'month', 'dayofweek', 'cost_lag1', 'cost_lag7'])
    prediction = model.predict(X)[0]
    st.success(f"Predicted Cost: ${prediction:.2f}")
