import streamlit as st

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
