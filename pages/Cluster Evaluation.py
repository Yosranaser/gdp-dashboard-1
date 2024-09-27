import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Function for the "Cluster Evaluation" page
def cluster_evaluation(X):
    st.title("Cluster Evaluation")

    # Elbow Method
    st.header("Elbow Method for Optimal K")
    
    # Define the range of K values to evaluate
    K_values = range(1, 11)
    inertia = []
    
    # Compute K-Means for different values of K and store inertia (sum of squared distances to centroids)
    for k in K_values:
        kmeans = KMeans(n_clusters=k, random_state=42).fit(X)
        inertia.append(kmeans.inertia_)
    
    # Plot the Elbow graph
    fig, ax = plt.subplots()
    ax.plot(K_values, inertia, 'bo-', markersize=8)
    ax.set_xlabel('Number of Clusters (K)')
    ax.set_ylabel('Inertia (WCSS)')
    ax.set_title('Elbow Method for Determining Optimal K')
    st.pyplot(fig)

    st.markdown("""
    In the **Elbow Method**, we plot the inertia (within-cluster sum of squares) against the number of clusters. 
    The 'elbow' point in the plot suggests the optimal number of clusters.
    """)

    # Silhouette Score
    st.header("Silhouette Score")
    
    # Compute Silhouette Scores for different values of K (>= 2)
    silhouette_scores = []
    for k in range(2, 11):
        kmeans = KMeans(n_clusters=k, random_state=42).fit(X)
        score = silhouette_score(X, kmeans.labels_)
        silhouette_scores.append(score)

    # Plot the Silhouette Score
    fig, ax = plt.subplots()
    ax.plot(range(2, 11), silhouette_scores, 'bo-', markersize=8)
    ax.set_xlabel('Number of Clusters (K)')
    ax.set_ylabel('Silhouette Score')
    ax.set_title('Silhouette Score for Different K')
    st.pyplot(fig)
    
    st.markdown("""
    The **Silhouette Score** measures how similar a data point is to its own cluster compared to other clusters. 
    A higher silhouette score indicates better-defined clusters. Typically, the score ranges from -1 to 1, 
    where a value near 1 indicates that the sample is far away from the neighboring clusters, while a value near 0 indicates overlapping clusters.
    """)

# Function to load CSV data from user input
# Function to load CSV data from user input
def load_data():
    st.title("Upload Your Dataset")
    uploaded_file = st.file_uploader("Upload your CSV file", type="csv")
    
    if uploaded_file is not None:
        try:
            # Attempt to read the CSV file with UTF-8 encoding
            data = pd.read_csv(uploaded_file)
        except UnicodeDecodeError:
            # If UTF-8 fails, try reading with ISO-8859-1 encoding
            data = pd.read_csv(uploaded_file, encoding='ISO-8859-1')
        except Exception as e:
            st.error(f"Error reading the file: {e}")
            return None
            
        st.write("Dataset preview:")
        st.write(data.head())
        return data
    else:
        st.warning("Please upload a CSV file.")
        return None


# Preprocessing function to prepare the dataset for K-means
def preprocess_data(data):
    # Assuming you want to cluster on numerical columns
    # Replace 'Quantity', 'UnitPrice', 'CustomerID' with actual column names from your dataset
    features = data[['Quantity', 'UnitPrice', 'CustomerID']] 
    
    # Standardize the features
    scaler = StandardScaler()
    X = scaler.fit_transform(features)
    
    return X

# Main function
def main():
    # Sidebar navigation
    page = st.sidebar.selectbox("Choose a page", ["User Input", "Dashboard", "Model Overview", "Cluster Evaluation"])
    
    if page == "Cluster Evaluation":
        data = load_data()  # Get user input
        if data is not None:
            X = preprocess_data(data)
            cluster_evaluation(X)

if __name__ == "__main__":
    main()
