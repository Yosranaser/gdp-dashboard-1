import streamlit as st
import pandas as pd
import math
from pathlib import Path
import pickle
st.title("model testing")
engine_size=st.number_input('engine_size',min_value=0,max_value=10,value=1)
clylinder=st.number_input('clylinder',min_value=0,max_value=10,value=1)
fuelcompution=st.number_input('fuelcompution',min_value=0,max_value=10,value=1)
with open('model (1).pkl', 'rb') as file:
model = pickle.load(file)
model.predict([[engine_size,clylinder,fuelcompution]])
st.write("car of co2 is",output[0][0])
