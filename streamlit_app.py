import streamlit as st
import pandas as pd
import math
from pathlib import Path
import pickle

# Streamlit app title
st.title("predicting based on diagnostic measurements whether you have diabetes.")

# Input fields
Pregnancies = st.number_input('Pregnancies', min_value=0, max_value=10, value=1)
Glucose = st.number_input('Glucose', min_value=0, max_value=10, value=1)
BloodPressure = st.number_input('BloodPressure', min_value=0, max_value=10, value=1)
SkinThickness = st.number_input('SkinThickness', min_value=0, max_value=10, value=1)
Insulin = st.number_input('Insulin', min_value=0, max_value=10, value=1)
BMI = st.number_input('BMI', min_value=0, max_value=10, value=1)
DiabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction', min_value=0, max_value=10, value=1)
Age = st.number_input('Age', min_value=0, max_value=10, value=1)
# Load the model
with open('model (2).pkl', 'rb') as file:
    model = pickle.load(file)

# Predict using the model
output = model.predict([[Pregnancies, Glucose, BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

# Display the result
st.write("prediction is", output)

