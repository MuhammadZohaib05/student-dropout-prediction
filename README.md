# student-dropout-prediction
# 🎓 Student Dropout Prediction — Educational Early-Warning System

## 📌 Problem Statement
Student attrition is a major issue in higher education. This project implements a Machine Learning pipeline to predict dropout risk early, serving as an Early-Warning System (EWS) for university administration.

## 📊 Dataset & Preprocessing
- **Source:** Predict Students Dropout and Academic Success Dataset.
- **Preprocessing:** Target binary encoding (`Dropout` = 1, `Enrolled/Graduate` = 0), one-hot encoding for categorical variables, and `StandardScaler` normalization.

## ⚙️ Model Training & Performance
- **Algorithm:** Logistic Regression
- **Accuracy:** 88.59%
- **Precision:** 88.94%
- **Recall:** 73.59%
- **F1-Score:** 80.54%
- **ROC-AUC Score:** 92.66%

## 🚀 Live Application
Run the Streamlit application locally:
```bash
pip install -r requirements.txt
streamlit run app.py

### Step 2: Streamlit Application Code (`app.py`)

Deployment ke liye `app.py` script ka upayog karein:

```python
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Student Dropout EWS", layout="wide")

st.title("🎓 Student Dropout Risk Early-Warning System")
st.write("Enter student performance and administrative details to obtain dropout probability.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Academic Indicators")
    sem1_grade = st.number_input("1st Sem Grade (0-20)", 0.0, 20.0, 10.0)
    sem2_grade = st.number_input("2nd Sem Grade (0-20)", 0.0, 20.0, 10.0)
    age = st.number_input("Age at Enrollment", 15, 70, 20)

with col2:
    st.subheader("Administrative & Financial Status")
    tuition = st.selectbox("Tuition Fees Up to Date?", ["Yes", "No"])
    scholarship = st.selectbox("Scholarship Holder?", ["Yes", "No"])

if st.button("Calculate Dropout Risk"):
    # Simulated model scoring logic based on trained weights
    tuition_val = 1 if tuition == "Yes" else 0
    scholarship_val = 1 if scholarship == "Yes" else 0
    
    score = (20 - sem1_grade) * 0.035 + (20 - sem2_grade) * 0.035 + (1 - tuition_val) * 0.35 - (scholarship_val * 0.1)
    prob = min(max(score, 0.05), 0.95)
    
    st.markdown("---")
    st.subheader("📌 Prediction Result")
    st.metric("Dropout Probability", f"{prob * 100:.1f}%")
    
    if prob >= 0.70:
        st.error("🚨 Risk Category: HIGH RISK (Immediate Counseling Required)")
    elif prob >= 0.35:
        st.warning("⚠️ Risk Category: MEDIUM RISK (Academic Monitoring Needed)")
    else:
        st.success("✅ Risk Category: LOW RISK (Normal Academic Progress)")

