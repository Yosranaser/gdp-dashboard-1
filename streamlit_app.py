import streamlit as st
import pandas as pd
import math
from pathlib import Path
import pickle

# Streamlit app title
st.title("Model Testing")

# Input fields
engine_size = st.number_input('engine_size', min_value=0, max_value=10, value=1)
cylinder = st.number_input('cylinder', min_value=0, max_value=10, value=1)
fuel_computation = st.number_input('fuel_computation', min_value=0, max_value=10, value=1)

# Load the model
with open('model (1).pkl', 'rb') as file:
    model = pickle.load(file)

# Predict using the model
output = model.predict([[engine_size, cylinder, fuel_computation]])

# Display the result
st.write("Car CO2 emission is", output[0])

