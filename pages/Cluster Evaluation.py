import streamlit as st
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page setup
st.set_page_config(page_title="K-means Model Evaluation", layout="wide")

# Introduction
st.title("Evaluate K-means Model")
st.write("In this section, we evaluate the K-means clustering model to find the optimal number of clusters.")

# Load dataset (for demonstration, replace with actual data loading)
@st.cache
def load_data():
    # Assuming the dataset is similar to the Mall_Customers.csv
    data = pd.read_csv('Mall_Customers.csv')
    return data

df = load_data()

# Sidebar for cluster selection
st.sidebar.header("K-means Model Parameters")
num_clusters = st.sidebar.slider("Select number of clusters (K):", min_value=2, max_value=10, value=5)

# Extract features (e.g., age, income, spending score)
features = df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

# K-means Model
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
cluster_labels = kmeans.fit_predict(features)

# Evaluation metrics
st.write("### Model Evaluation")

# Inertia (within-cluster sum of squares)
inertia = kmeans.inertia_
st.write(f"**Inertia (Within-cluster sum of squares)**: {inertia:.2f}")

# Silhouette Score
silhouette_avg = silhouette_score(features, cluster_labels)
st.write(f"**Silhouette Score**: {silhouette_avg:.2f} (ranges from -1 to 1, higher is better)")

# Elbow method (visualizing inertia for different K values)
def plot_elbow_method(data):
    inertia_values = []
    k_range = range(1, 11)
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        inertia_values.append(kmeans.inertia_)
    
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=list(k_range), y=inertia_values, marker='o')
    plt.title("Elbow Method to Determine Optimal K")
    plt.xlabel("Number of Clusters (K)")
    plt.ylabel("Inertia")
    plt.xticks(k_range)
    st.pyplot(plt.gcf())

# Display elbow method plot
st.write("### Elbow Method for Optimal Number of Clusters")
plot_elbow_method(features)

# Optional: Visualizing clusters (scatter plot)
st.write("### Cluster Visualization")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue=cluster_labels, data=df, palette='viridis', ax=ax)
plt.scatter(kmeans.cluster_centers_[:, 1], kmeans.cluster_centers_[:, 2], s=200, c='red', label='Centroids', marker='X')
plt.title(f'K-means Clustering with {num_clusters} Clusters')
plt.legend()
st.pyplot(fig)
