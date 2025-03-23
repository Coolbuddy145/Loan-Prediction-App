

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
model_file = "loan_eligibility_model.pkl"
with open(model_file, "rb") as file:
    model = pickle.load(file)

st.title("🏦 Loan Eligibility Prediction")

# Input fields for user data
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0, step=500)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0, step=500)
loan_amount = st.number_input("Loan Amount", min_value=0, step=5000)
loan_amount_term = st.selectbox("Loan Amount Term (Months)", [12, 36, 60, 120, 180, 240, 300, 360])
credit_history = st.selectbox("Credit History", [1, 0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Convert inputs to a DataFrame for prediction
input_data = pd.DataFrame({
    "Gender": [1 if gender == "Male" else 0],
    "Married": [1 if married == "Yes" else 0],
    "Dependents": [int(dependents) if dependents != "3+" else 3],
    "Education": [1 if education == "Graduate" else 0],
    "Self_Employed": [1 if self_employed == "Yes" else 0],
    "Applicant_Income": [applicant_income],
    "Coapplicant_Income": [coapplicant_income],
    "Loan_Amount": [loan_amount],
    "Loan_Amount_Term": [loan_amount_term],
    "Credit_History": [credit_history],
    "Property_Area": [0 if property_area == "Urban" else (1 if property_area == "Semiurban" else 2)]
})

# Predict loan eligibility
if st.button("Check Eligibility"):
    prediction = model.predict(input_data)
    result = "Approved ✅" if prediction[0] == 1 else "Rejected ❌"
    st.subheader(f"Loan Status: {result}")

