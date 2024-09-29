
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample function to load your clustered data
# Assuming you have a 'Segment' column indicating customer segment
def load_data():
    st.title("Upload Your Dataset")
    uploaded_file = st.file_uploader("Upload your CSV file", type="csv")
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
        except UnicodeDecodeError:
            data = pd.read_csv(uploaded_file, encoding='ISO-8859-1')
        except Exception as e:
            st.error(f"Error reading the file: {e}")
            return None

# Load data
df = load_data()

# Page title
st.title("Customer Profiles / Segments")
with open('model (1).pkl', 'rb') as file:
    kmeans = pickle.load(file)

# Predict the clusters using the K-Means model
df['Cluster'] = kmeans.predict(df)

# Now, you can access the unique clusters
unique_segments = df['Cluster'].unique()
# Select customer segment to display its characteristics
unique_segments = df['Cluster'].unique()
selected_segment = st.selectbox("Select Customer Segment", unique_segments)

# Filter the dataset for the selected segment
segment_data = df[df['Cluster'] == selected_segment]

# Display key statistics of the selected segment
st.write(f"### Overview of Segment {selected_segment}")
st.write(segment_data.describe())

# Visualize the distribution of features for the selected segment
st.write("### Feature Distributions")

# Create a few important plots for each feature
for col in df.columns:
    if col != 'Predicted_Cluster':  # Exclude the 'Segment' column itself
        fig, ax = plt.subplots()
        sns.histplot(segment_data[col], kde=True, ax=ax)
        ax.set_title(f"Distribution of {col} for Segment {selected_segment}")
        st.pyplot(fig)

# Radar chart for comparing means of key features in the segment
st.write("### Radar Chart of Key Features")

# Define key features to visualize (replace with your own)
key_features = ['Quantity', 'UnitPrice', 'CustomerID']  # Replace with relevant features

# Create a dataframe to store the mean of these features
segment_means = segment_data[key_features].mean()

# Create radar chart
fig = plt.figure()
categories = list(segment_means.index)
values = segment_means.values.flatten().tolist()
values += values[:1]  # Closing the loop of the radar chart

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

ax = plt.subplot(111, polar=True)
ax.fill(angles, values, color='blue', alpha=0.25)
ax.plot(angles, values, color='blue', linewidth=2)
ax.set_yticklabels([])

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

st.pyplot(fig)
