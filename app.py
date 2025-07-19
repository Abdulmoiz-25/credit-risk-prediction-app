# app.py
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
model = pickle.load(open('credit_model.pkl', 'rb'))

st.title("💳 Credit Risk Prediction App")
st.markdown("Predict if a loan will be **approved** or **not approved** based on applicant data.")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.selectbox("Loan Amount Term", [360.0, 120.0, 180.0, 60.0, 240.0, 300.0, 84.0, 12.0])
credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Mapping inputs to model format
def encode_inputs():
    return np.array([[
        1 if gender == "Male" else 0,
        1 if married == "Yes" else 0,
        {"0": 0, "1": 1, "2": 2, "3+": 3}[dependents],
        1 if education == "Graduate" else 0,
        1 if self_employed == "Yes" else 0,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        credit_history,
        {"Urban": 2, "Semiurban": 1, "Rural": 0}[property_area]
    ]])

if st.button("Predict Loan Approval"):
    input_data = encode_inputs()
    result = model.predict(input_data)
    if result[0] == 1:
        st.success("✅ Loan is likely to be Approved!")
    else:
        st.error("❌ Loan is likely to be Rejected.")
