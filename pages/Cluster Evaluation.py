import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Function to load CSV data from user input
def load_data():
    st.title("Upload Your Dataset")
    uploaded_file = st.file_uploader("Upload your CSV file", type="csv")
    
    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file)
        except UnicodeDecodeError:
            data = pd.read_csv(uploaded_file, encoding='ISO-8859-1')
        except Exception as e:
            st.error(f"Error reading the file: {e}")
            return None
            
        st.write("Dataset preview:")
        st.write(data.head())
        st.write("Column names in the dataset:")
        st.write(data.columns.tolist())  # Display column names for debugging
        return data
    else:
        st.warning("Please upload a CSV file.")
        return None

# Preprocessing function to prepare the dataset for K-means
def preprocess_data(data):
    # Display the column names
    st.write("Column names in the dataset:")
    st.write(data.columns.tolist())
    
    # Strip any leading/trailing spaces from column names
    data.columns = data.columns.str.strip()
    
    # Adjust these feature names according to your actual dataset
    try:
        features = data[['Quantity', 'UnitPrice', 'CustomerID']]
    except KeyError as e:
        st.error(f"KeyError: {e}. Please check the column names in your dataset.")
        return None
    
    # Standardize the features
    scaler = StandardScaler()
    X = scaler.fit_transform(features)
    
    return X

# Cluster evaluation function (your previous implementation)
def cluster_evaluation(X):
    st.title("Cluster Evaluation")
    # [Your cluster evaluation code goes here]

# Main function
def main():
    # Sidebar navigation
    page = st.sidebar.selectbox("Choose a page", ["User Input", "Dashboard", "Model Overview", "Cluster Evaluation"])
    
    if page == "Cluster Evaluation":
        data = load_data()  # Get user input
        if data is not None:
            X = preprocess_data(data)
            if X is not None:
                cluster_evaluation(X)

if __name__ == "__main__":
    main()
