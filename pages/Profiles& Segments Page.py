import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle


def profile_section(data):
    st.title("Customer Profile")
    
    # Basic Statistics
    st.subheader("Basic Statistics")
    st.write(data.describe())
    
    # Gender distribution (assuming there's a 'Gender' column)
    if 'Gender' in data.columns:
        gender_counts = data['Genre'].value_counts()
        st.subheader("Gender Distribution")
        st.bar_chart(gender_counts)
    
    # Spending distribution
    if 'TotalSpent' in data.columns:
        st.subheader("Spending Distribution")
        plt.figure(figsize=(10, 5))
        plt.hist(data['TotalSpent'], bins=30)
        st.pyplot(plt)

