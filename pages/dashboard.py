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
    gender_counts = df['Genre'].value_counts()
    fig_gender = px.pie(values=gender_counts, names=gender_counts.index, title='Gender Distribution of Customers')
    st.plotly_chart(fig_gender)

# 6. Heatmap: Correlations between features
with col6:
    # Check for non-numeric columns
    non_numeric_columns = df.select_dtypes(exclude=['number']).columns.tolist()
    if non_numeric_columns:
        st.write("### Non-Numeric Columns Detected")
        st.write(non_numeric_columns)
    
    # Filter only numeric columns
    df_numeric = df.select_dtypes(include=['number'])
    
    # Drop rows with NaN values in numeric columns
    df_numeric_clean = df_numeric.dropna()
    
    # Debug: Show the cleaned numeric DataFrame
    st.write("### Cleaned Numeric DataFrame for Correlation")
    st.write(df_numeric_clean.head())
    
    # Calculate correlation matrix if there are numeric columns
    if not df_numeric_clean.empty:
        corr = df_numeric_clean.corr()
        st.write("### Correlation Matrix")
        st.write(corr)
        
        # Plot Heatmap
        st.write("#### Feature Correlation Heatmap")
        fig_heatmap = go.Figure(data=go.Heatmap(
            z=corr.values,
            x=corr.columns,
            y=corr.columns,
            colorscale='Viridis'))
        fig_heatmap.update_layout(title='Correlation between Features', xaxis_nticks=36)
        st.plotly_chart(fig_heatmap)
    else:
        st.error("No numeric columns available for correlation.")
st.markdown(""" ###conclusion:
    1. Age Distribution Insights:
Age range: The majority of customers seem to be between 20 and 40 years old.
Peak age group: The highest bar indicates that the most common age range for customers is around 30 years.
Spread and outliers: The box plot shows that the age distribution is fairly spread out, with some customers in older age brackets (above 60) being possible outliers.
What to learn: This could indicate that the business primarily attracts younger adults, suggesting that marketing efforts may need to focus on this demographic, or alternatively, strategies could be developed to attract older customers.

2. Annual Income Distribution Insights:
Income range: Most customers have an annual income between 40k and 80k.
Peak income group: The highest concentration of customers falls in the middle-income group (~60k).
Outliers: There seems to be a few customers with significantly higher income (beyond 100k), which might represent high-end or premium customers.
What to learn: Understanding this income distribution can help in tailoring product offerings and pricing strategies. For example, if a large portion of customers have mid-range incomes, products and services should be priced accordingly.

3. Spending Score Distribution Insights:
Spending score range: The spending scores are spread widely across the scale (1–100), with notable peaks around both lower and higher scores.
Bimodal pattern: There are two prominent clusters, one around a low spending score (~30) and another around a high spending score (~70).
What to learn: This suggests two distinct customer segments based on spending behavior—one that spends relatively less and another that spends significantly more. This could inform differentiated marketing approaches or product recommendations for low vs. high spenders.
    
General Insights:
Customer segmentation: These distributions suggest there are potential segments to focus on. For example, younger, middle-income, high-spending customers could be one target group, while older, high-income, low-spending customers might require a different strategy.
Pricing and marketing strategies: The bimodal spending score distribution indicates that offering a mix of premium and budget products/services could capture the different spending behaviors.
Understanding these patterns helps in aligning marketing efforts, product development, and customer engagement strategies based on the characteristics of your customer base
    """)
