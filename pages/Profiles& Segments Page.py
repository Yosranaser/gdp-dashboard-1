import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
df = pd.read_csv("Mall_Customers.csv")

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
profile_section(df)


# Function to take user input and predict the cluster
def user_input_features():
    st.sidebar.header('Enter Customer Information')
    
    # Taking input from user
    genre = st.sidebar.selectbox('Gender', ('Male', 'Female'))
    age = st.sidebar.number_input('Age', min_value=18, max_value=100, value=25)
    annual_income = st.sidebar.number_input('Annual Income (k$)', min_value=15, max_value=150, value=60)
    spending_score = st.sidebar.number_input('Spending Score (1-100)', min_value=1, max_value=100, value=50)

    # Creating a dataframe from the inputs
    data = {'Genre': genre,
            'Age': age,
            'Annual Income (k$)': annual_income,
            'Spending Score (1-100)': spending_score}
    
    features = pd.DataFrame([data])
    
    return features

# Load and preprocess data for fitting K-means
def load_and_preprocess_data():
    # Loading the dataset
    df = pd.read_csv('Mall_Customers.csv')
    
    # Preprocessing: Encode Genre, scale Age, Annual Income, and Spending Score
    df['Genre'] = LabelEncoder().fit_transform(df['Genre'])
    X = df[['Genre', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']]
    
    # Standardizing the numerical features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, scaler

# Function to preprocess user input the same way the dataset was preprocessed
def preprocess_user_input(input_data, scaler):
    # Encode 'Genre'
    input_data['Genre'] = LabelEncoder().fit_transform(input_data['Genre'])

    # Standardize the features
    input_scaled = scaler.transform(input_data)
    
    return input_scaled

# Function to predict cluster using the K-means model
def predict_cluster(model, input_scaled):
    cluster_label = model.predict(input_scaled)
    return cluster_label

# Main app function
def main():
    st.title("Customer Segmentation using K-Means")

    # Load and preprocess the dataset for training the K-means model
    X_scaled, scaler = load_and_preprocess_data()
    
    # Train the K-means model (assuming 5 clusters as an example)
    kmeans_model = KMeans(n_clusters=5, random_state=42)
    kmeans_model.fit(X_scaled)

    # Take user input
    user_data = user_input_features()
    
    # Preprocess user input for the model
    input_scaled = preprocess_user_input(user_data, scaler)
    
    # Predict the cluster for the user's input
    cluster = predict_cluster(kmeans_model, input_scaled)

    # Display the predicted cluster
    st.write(f"The customer belongs to Cluster: {cluster[0]}")

if __name__ == "__main__":
    main()
