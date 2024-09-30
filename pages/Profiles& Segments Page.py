import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans

# Initialize the LabelEncoder globally to encode 'Genre' only once
encoder = LabelEncoder()

# Function to take user input and return as DataFrame
def user_input_features():
    st.sidebar.header('Enter Customer Information')

    

    # User Data Input
    st.sidebar.header("Enter Your Information")
    age = st.sidebar.number_input("Enter your Age:", min_value=1, max_value=100, value=25, step=1)
    annual_income = st.sidebar.number_input("Enter your Annual Income (k$):", min_value=10, max_value=150, value=50, step=1)
    spending_score = st.sidebar.slider("Enter your Spending Score (1-100):", min_value=1, max_value=100, value=50)
    genre = st.sidebar.radio("Select your Gender:", options=["Male", "Female"])

    # Creating a dataframe from the inputs
    data = {'Genre': genre,
            'Age': age,
            'Annual Income (k$)': annual_income,
            'Spending Score (1-100)': spending_score}

    return pd.DataFrame([data])

# Load and preprocess data for fitting K-means
def load_and_preprocess_data():
    # Loading the dataset
    df = pd.read_csv('Mall_Customers.csv')

    # Preprocessing: Encode Genre, scale Age, Annual Income, and Spending Score
    df['Genre'] = encoder.fit_transform(df['Genre'])
    X = df[['Genre', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

    # Standardizing the numerical features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, scaler

# Function to preprocess user input the same way the dataset was preprocessed
def preprocess_user_input(input_data, scaler):
    # Encode 'Genre' only for the user input
    input_data['Genre'] = encoder.transform(input_data['Genre'])

    # Standardize the features
    input_scaled = scaler.transform(input_data)

    return input_scaled

# Function to predict cluster using the K-means model
def predict_cluster(model, input_scaled):
    cluster_label = model.predict(input_scaled)
    return cluster_label

# Function to store data in a CSV
def save_data_to_csv(user_data):
    # Load existing data or create new DataFrame if file doesn't exist
    try:
        existing_data = pd.read_csv('user_data.csv')
        new_data = pd.concat([existing_data, user_data], ignore_index=True)
    except FileNotFoundError:
        new_data = user_data

    # Save the updated DataFrame to CSV
    new_data.to_csv('user_data.csv', index=False)

    return new_data

# Main app function
def main():
    st.title("Customer Segmentation and Data Collection")

    # Load and preprocess the dataset for training the K-means model
    X_scaled, scaler = load_and_preprocess_data()

    # Train the K-means model (assuming 5 clusters as an example)
    kmeans_model = KMeans(n_clusters=5, random_state=42)
    kmeans_model.fit(X_scaled)

    # Take user input
    user_data = user_input_features()

    # Show a submit button
    if st.sidebar.button("Submit"):
        # Preprocess user input for the model
        input_scaled = preprocess_user_input(user_data, scaler)

        # Predict the cluster for the user's input
        cluster = predict_cluster(kmeans_model, input_scaled)

        # Add the predicted cluster to the user data
        user_data['Cluster'] = cluster[0]

        # Save the user data to a CSV and get the updated DataFrame
        updated_data = save_data_to_csv(user_data)

        # Display the predicted cluster
        st.write(f"The customer belongs to Cluster: {cluster[0]}")

        # Display the updated table with all user inputs
        st.write("Updated User Data:")
        st.dataframe(updated_data)

if __name__ == "__main__":
    main()
