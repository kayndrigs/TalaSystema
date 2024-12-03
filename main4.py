import pandas as pd
import streamlit as st

# Load CSV files into dataframes
sales_df = pd.read_csv('sales_data.csv')
products_df = pd.read_csv('products.csv')

# Display data in Streamlit
st.write("Sales Data", sales_df.head())
st.write("Products Data", products_df.head())

# Merge tables to establish a relationship based on 'product_id'
merged_df = pd.merge(sales_df, products_df, on='product_id', how='inner')

# Display the merged data
st.write("Merged Data", merged_df.head())

# Calculate total sales for each row
merged_df['total_sales'] = merged_df['quantity_sold'] * merged_df['unit_price']

# Display the updated data
st.write("Data with Calculated Column (Total Sales)", merged_df.head())

# Calculate total sales (similar to a measure in Power BI)
total_sales = merged_df['total_sales'].sum()

# Display the total sales in Streamlit
st.metric("Total Sales", f"${total_sales:,.2f}")

from graphviz import Digraph

# Create a Graphviz diagram
dot = Digraph(comment='Data Model')
dot.node('A', 'Sales')
dot.node('B', 'Products')
dot.edge('A', 'B', label='product_id')

# Save and display the diagram in Streamlit
dot.render('data_model', format='png', cleanup=True)

# Display the diagram in Streamlit
st.image('data_model.png')

# Create a filter to select product category
category = st.selectbox('Select Product Category', merged_df['category'].unique())

# Filter the data based on selected category
filtered_data = merged_df[merged_df['category'] == category]

# Display the filtered data
st.write("Filtered Data by Category", filtered_data)

import plotly.express as px

# Create a bar chart of total sales by product
fig = px.bar(merged_df, x='product_name', y='total_sales', title='Total Sales by Product')

# Display the chart in Streamlit
st.plotly_chart(fig)

# Group by product and calculate total sales
summary_df = merged_df.groupby('product_name').agg(total_sales=('total_sales', 'sum')).reset_index()

# Display the summary table
st.write("Summary by Product", summary_df)
