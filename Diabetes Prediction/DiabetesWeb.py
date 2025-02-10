import streamlit as st
import numpy as np
import pickle

# Load Training Model...
model, scaler = pickle.load(open("Diabetes_model.pkl", "rb"))

st.title("Diabetes Prediction App")
st.write("Enter the following details to predict diabetes:")


# User input field...
Pregnancies = (st.number_input("Pregnancies",min_value=0, max_value=20, value=1))
Glucose = st.number_input("Glucose Level",min_value=0, max_value=300, value=120)
BloodPressure = st.number_input("Blood Pressure",min_value=0, max_value=200, value=70)
SkinThickness = st.number_input("Skin Thickness",min_value=0, max_value=100, value=20)
Insulin = st.number_input("Insulin Level",min_value=0, max_value=900, value=80)
BMI = st.number_input("BMI",min_value=0.0, max_value=100.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function",min_value=0.0, max_value=2.5, value=0.5)
Age = st.number_input("Age",min_value=0, max_value=120, value=30)

# Prediction button...
if st.button("Predict"):
    input_data = np.array([[Pregnancies,Glucose,BloodPressure,
                            SkinThickness,Insulin,BMI,dpf,Age]])
    input_data = scaler.transform(input_data)
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("The person is likely to have diabetes.")
    else:
        st.success("The person is unlikely to have diabetes.")





