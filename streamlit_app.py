import streamlit as st

# Page setup
st.set_page_config(page_title="Customer Segmentation - K-means", layout="centered")

# Introduction
st.title("Customer Segmentation using K-means")
st.subheader("Welcome to the Customer Segmentation Web Application")

# Abstract
st.markdown("""
### Abstract:
This web application helps you explore customer segmentation using the K-means clustering algorithm. 
Customer segmentation is the practice of dividing customers into groups based on common characteristics 
such as age, salary, spending score, and gender. This model helps businesses understand customer behavior 
and target different customer segments effectively.

In this application, users can input their personal information (age, salary, gender, and spending score) 
and the K-means model will analyze the data to place the user into one of the predefined customer segments.
""")

# User Data Input
st.sidebar.header("Enter Your Information")
age = st.sidebar.number_input("Enter your Age:", min_value=1, max_value=100, value=25, step=1)
annual_income = st.sidebar.number_input("Enter your Annual Income (k$):", min_value=10, max_value=150, value=50, step=1)
spending_score = st.sidebar.slider("Enter your Spending Score (1-100):", min_value=1, max_value=100, value=50)
gender = st.sidebar.radio("Select your Gender:", options=["Male", "Female"])

# Display user input
st.write("### User Information:")
st.write(f"Age: {age}")
st.write(f"Annual Income: {annual_income}k$")
st.write(f"Spending Score: {spending_score}")
st.write(f"Gender: {gender}")

# Placeholder for K-means clustering result
st.write("The K-means model will place you into a customer segment based on the information you have provided.")
