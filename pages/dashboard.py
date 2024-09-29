import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Load the dataset
df = pd.read_csv("Mall_Customers.csv")

# Display the dataframe for reference
st.write(df.head())

# Create two rows with three columns each to distribute the charts

# Row 1: Age Distribution, Annual Income Distribution, Spending Score Distribution
st.write("### Row 1: Basic Distributions")
col1, col2, col3 = st.columns(3)

# 1. Age Distribution
with col1:
    st.write("#### Age Distribution")
    fig_age = px.histogram(df, x='Age', nbins=20, title='Age Distribution of Customers', marginal='box')
    st.plotly_chart(fig_age)

# 2. Annual Income Distribution
with col2:
    st.write("#### Annual Income Distribution")
    fig_income = px.histogram(df, x='Annual Income (k$)', nbins=20, title='Annual Income Distribution of Customers', marginal='box')
    st.plotly_chart(fig_income)

# 3. Spending Score Distribution
with col3:
    st.write("#### Spending Score Distribution")
    fig_spending = px.histogram(df, x='Spending Score (1-100)', nbins=20, title='Spending Score Distribution of Customers', marginal='box')
    st.plotly_chart(fig_spending)

# Row 2: Scatter Plot, Gender Distribution, Heatmap
st.write("### Row 2: Advanced Visualizations")
col4, col5, col6 = st.columns(3)

# 4. Scatter Plot: Annual Income vs Spending Score
# Load your DataFrame (assuming it's already loaded)
df = pd.read_csv('Mall_Customers.csv')

# Check the columns and data types
st.write("### DataFrame Columns and Data Types")
st.write(df.dtypes)

# Display the first few rows of the DataFrame
st.write("### Preview of DataFrame")
st.write(df.head())
with col4:
    st.write("### Available Columns in DataFrame")
    st.write(df.columns.tolist())
    
    # Strip whitespace from column names
    df.columns = df.columns.str.strip()
    
    # Check columns again after stripping
    st.write("### Available Columns After Stripping Whitespace")
    st.write(df.columns.tolist())
    
    # Filter out rows with missing values in the specified columns
    try:
        df_filtered = df.dropna(subset=['Annual Income (k$)', 'Spending Score (1-100)', 'Genre', 'Age'])
    except KeyError as e:
        st.error(f"KeyError: One of the specified columns does not exist: {e}")
        st.stop()
    
    # Row 2: Scatter Plot: Annual Income vs Spending Score
    st.write("#### Annual Income vs Spending Score")
    fig_scatter = px.scatter(df_filtered, x='Annual Income (k$)', y='Spending Score (1-100)', 
                             title='Annual Income vs Spending Score', color='Genre', hover_data=['Age'])
    st.plotly_chart(fig_scatter)

with col5:
    st.write("#### Gender Distribution")
    gender_counts = df['Gender'].value_counts()
    fig_gender = px.pie(values=gender_counts, names=gender_counts.index, title='Gender Distribution of Customers')
    st.plotly_chart(fig_gender)

# 6. Heatmap: Correlations between features
with col6:
    st.write("#### Feature Correlation Heatmap")
    corr = df.corr()
    fig_heatmap = go.Figure(data=go.Heatmap(
        z=corr.values,
        x=corr.columns,
        y=corr.columns,
        colorscale='Viridis'))
    fig_heatmap.update_layout(title='Correlation between Features', xaxis_nticks=36)
    st.plotly_chart(fig_heatmap)
