# app.py  (drop‑in replacement)
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

st.set_page_config(page_title="Credit Risk Prediction", page_icon="💳")

# ------------------------------------------------------------------------------
# 1. Load the trained model (try both possible filenames)
# ------------------------------------------------------------------------------
MODEL_CANDIDATES = ["credit_model.pkl", "credit_model .pkl"]
model = None
for fname in MODEL_CANDIDATES:
    if os.path.exists(fname):
        with open(fname, "rb") as f:
            model = pickle.load(f)
        break

if model is None:
    st.error(
        "❌ **Model file not found!**\n\n"
        "Make sure either `credit_model.pkl` or `credit_model .pkl` is in the "
        "same folder as `app.py`, then redeploy / rerun the app."
    )
    st.stop()

# ------------------------------------------------------------------------------
# 2. App title & description
# ------------------------------------------------------------------------------
st.title("💳 Credit Risk Prediction")
st.markdown(
    """
    Enter applicant details to predict whether a loan is **likely to be approved**.
    """
)

# ------------------------------------------------------------------------------
# 3. User input widgets
# ------------------------------------------------------------------------------
gender            = st.selectbox("Gender",           ["Male", "Female"])
married           = st.selectbox("Married",          ["Yes", "No"])
dependents        = st.selectbox("Dependents",       ["0", "1", "2", "3+"])
education         = st.selectbox("Education",        ["Graduate", "Not Graduate"])
self_employed     = st.selectbox("Self‑Employed",    ["Yes", "No"])
applicant_income  = st.number_input("Applicant Income",  min_value=0)
coapplicant_income= st.number_input("Co‑applicant Income", min_value=0)
loan_amount       = st.number_input("Loan Amount",       min_value=0)
loan_term         = st.selectbox("Loan Amount Term (months)",
                                 [360.0, 300.0, 240.0, 180.0, 120.0, 84.0, 60.0, 12.0])
credit_history    = st.selectbox("Credit History (1 = good, 0 = bad)", [1.0, 0.0])
property_area     = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# ------------------------------------------------------------------------------
# 4. Encode inputs exactly as during training
#    (LabelEncoder sorted categories alphabetically)
# ------------------------------------------------------------------------------
encoded_row = np.array([[
    1 if gender   == "Male"       else 0,             # Gender
    1 if married  == "Yes"        else 0,             # Married
    {"0": 0, "1": 1, "2": 2, "3+": 3}[dependents],    # Dependents
    1 if education == "Graduate"  else 0,             # Education
    1 if self_employed == "Yes"   else 0,             # Self_Employed
    applicant_income,                                 # ApplicantIncome
    coapplicant_income,                               # CoapplicantIncome
    loan_amount,                                      # LoanAmount
    loan_term,                                        # Loan_Amount_Term
    credit_history,                                   # Credit_History
    {"Rural": 0, "Semiurban": 1, "Urban": 2}[property_area]  # Property_Area
]])

# Put into DataFrame with correct column order
columns = [
    "Gender", "Married", "Dependents", "Education", "Self_Employed",
    "ApplicantIncome", "CoapplicantIncome", "LoanAmount",
    "Loan_Amount_Term", "Credit_History", "Property_Area"
]
input_df = pd.DataFrame(encoded_row, columns=columns)

# ------------------------------------------------------------------------------
# 5. Predict on button click
# ------------------------------------------------------------------------------
if st.button("Predict Loan Approval"):
    prediction = model.predict(input_df)[0]   # 0 or 1
    if prediction == 1:
        st.success("✅ Loan is **likely to be Approved!**")
    else:
        st.error("❌ Loan is **likely to be Rejected.**")
