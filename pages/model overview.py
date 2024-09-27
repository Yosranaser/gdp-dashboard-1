import streamlit as st

# Define a function for the "Model Overview" page
def model_overview():
    st.title("K-Means Model Overview")
    
    # Explanation using markdown
    st.markdown("""
    ## What is K-Means Clustering?
    
    K-Means is an unsupervised machine learning algorithm that groups similar data points into clusters. The algorithm aims to partition a given dataset into **K clusters**, where each data point belongs to the cluster with the nearest mean, also called the **centroid**.
    
    ### Steps of the K-Means Algorithm:
    
    1. **Initialization**: Choose the number of clusters (K) and randomly place K centroids.
    2. **Assignment Step**: Each data point is assigned to the nearest centroid, creating clusters.
    3. **Update Step**: The centroids are recalculated as the mean of all points in their cluster.
    4. **Repeat**: Steps 2 and 3 are repeated until the centroids no longer move or the maximum number of iterations is reached.
    
    """)
    
    # Visualizing how K-means works with images or diagrams
    st.image("https://miro.medium.com/max/1400/1*eVjxep2oKweAiu4WyRQjBg.gif", caption="K-Means Clustering in Action", use_column_width=True)

    st.markdown("""
    ### Choosing the Number of Clusters (K)
    
    One of the most important decisions in K-Means is choosing the number of clusters (K). Two common techniques to help with this decision are:
    
    - **Elbow Method**: Plotting the sum of squared distances from each point to its assigned centroid (called the "inertia" or WCSS) for a range of values of K. The "elbow" of the plot suggests the optimal K.
    - **Silhouette Score**: A measure of how similar an object is to its own cluster compared to other clusters. A high silhouette score indicates that the data is well-clustered.
    
    """)
    
    # Displaying the Elbow Method example plot (you can replace it with your own plot)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Elbow_method_plot.png/800px-Elbow_method_plot.png", caption="Elbow Method for Determining Optimal K", use_column_width=True)

# Add this to the navigation section of your app
# Example: Using the function for the page navigation
if st.sidebar.selectbox("Choose a page", ["User Input", "Dashboard", "Model Overview"]) == "Model Overview":
    model_overview()
