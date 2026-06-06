
import streamlit as st
import pandas as pd
import joblib
from huggingface_hub import hf_hub_download

model_path = hf_hub_download(
    repo_id="Yadukrish10/tourism-package-model",
    filename="best_model.pkl"
)

model = joblib.load(model_path)

# Load model
model = joblib.load("best_model.pkl")

st.title("Wellness Tourism Package Prediction")

age = st.number_input("Age", min_value=18, max_value=100, value=30)
monthly_income = st.number_input("Monthly Income", value=30000)
number_of_trips = st.number_input("Number Of Trips", value=2)
pitch_satisfaction_score = st.number_input("Pitch Satisfaction Score", value=3)

if st.button("Predict"):

    input_df = pd.DataFrame({
        "Age":[age],
        "MonthlyIncome":[monthly_income],
        "NumberOfTrips":[number_of_trips],
        "PitchSatisfactionScore":[pitch_satisfaction_score]
    })

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.success("Customer is likely to purchase the package")
    else:
        st.error("Customer is unlikely to purchase the package")
