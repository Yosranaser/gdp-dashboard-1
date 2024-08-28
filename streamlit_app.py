import streamlit as st
import pandas as pd
import pickle

# Streamlit app title
st.title("Diabetes Prediction App")

# Introduction text
st.markdown("""
Welcome to the Diabetes Prediction App. This tool uses a machine learning model to predict the likelihood of diabetes 
based on diagnostic measurements. Simply fill in the required fields and click the 'Predict' button to see the result.
""")

# Sidebar for input fields
st.sidebar.header('User Input Features')
st.sidebar.markdown("""
Please input the following parameters:
""")

# Input fields in the sidebar
Pregnancies = st.sidebar.number_input('Pregnancies', min_value=0, max_value=17, value=1)
Glucose = st.sidebar.number_input('Glucose', min_value=0, max_value=200, value=1)
BloodPressure = st.sidebar.number_input('BloodPressure', min_value=0, max_value=122, value=1)
SkinThickness = st.sidebar.number_input('SkinThickness', min_value=0, max_value=99, value=1)
Insulin = st.sidebar.number_input('Insulin', min_value=0, max_value=846, value=1)
BMI = st.sidebar.number_input('BMI', min_value=0, max_value=67, value=1)
DiabetesPedigreeFunction = st.sidebar.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.42, value=0.1)
Age = st.sidebar.number_input('Age', min_value=21, max_value=81, value=21)

# Load the model
# model_path = 'model.pkl'  # Ensure this is the correct path to your model
try:
    with open('model (2)', 'rb') as file:
        model = pickle.load(file)
    
    # Button for prediction
    if st.sidebar.button('Predict'):
        # Predict using the model
        prediction = model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        result = "Diabetic" if prediction[0] == 1 else "Non-diabetic"
        
        # Display the result
        st.success(f"The model predicts that the patient is: *{result}*")
except FileNotFoundError:
    st.error(f"Model file not found: {model_path}")
except Exception as e:
    st.error(f"An error occurred: {e}")

# Footer
st.markdown("""
---
Developed by [Your Name](https://github.com/your-profile). For more information, visit the [project repository](https://github.com/your-repo).
""")
