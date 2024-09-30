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


# Placeholder for K-means clustering result
st.write("The K-means model will place you into a customer segment based on the information you have provided.")
