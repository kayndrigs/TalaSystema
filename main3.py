import pandas as pd
import streamlit as st

# Load sales data and product data from CSV files
sales_df = pd.read_csv('sales_data.csv')
products_df = pd.read_csv('products.csv')

# Merge the tables based on 'product_id' to create a relationship
merged_df = pd.merge(sales_df, products_df, on='product_id')

# Display the merged data in Streamlit
st.write("Merged Sales and Products Data", merged_df)
