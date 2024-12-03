import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from graphviz import Digraph

# Function to read the uploaded CSV file
def read_csv(file):
    """Reads a CSV file and returns it as a pandas DataFrame"""
    df = pd.read_csv(file, encoding='latin-1')
    return df

# Function to generate an ER diagram using networkx
def generate_er_diagram(df):
    """Generates a basic ER diagram based on CSV columns"""
    # Create a new directed graph
    G = nx.DiGraph()

    # Add nodes for each column in the CSV
    for column in df.columns:
        G.add_node(column)

    # Generate random relationships between columns (for example purposes)
    # Ideally, relationships would be inferred from the data or defined by the user
    for i in range(len(df.columns)-1):
        G.add_edge(df.columns[i], df.columns[i+1])

    return G

# Function to plot ER diagram using networkx and matplotlib
def plot_er_diagram(G):
    """Plot the ER diagram using NetworkX and Matplotlib"""
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color='lightblue', node_size=3000, font_size=12, font_weight='bold', edge_color='gray')
    plt.title("Entity-Relationship Diagram")
    plt.show()

# Function to generate ER diagram using Graphviz (more visually appealing)
def generate_graphviz_er(df):
    """Generates an ER diagram using Graphviz"""
    dot = Digraph()

    # Add nodes for each column
    for column in df.columns:
        dot.node(column)

    # Add edges between the columns (simple example)
    for i in range(len(df.columns)-1):
        dot.edge(df.columns[i], df.columns[i+1])

    return dot

# Streamlit interface for generating and displaying the ER diagram
def main():
    """Main Streamlit app function"""
    st.title("ER Diagram Generator from CSV")

    # File uploader to upload a CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read CSV data
        df = read_csv(uploaded_file)
        st.write("CSV Data Preview:", df.head())

        # Generate and display ER diagram using NetworkX
        G = generate_er_diagram(df)
        st.write("Generated ER Diagram (NetworkX):")
        plot_er_diagram(G)

        # Generate and display ER diagram using Graphviz
        dot = generate_graphviz_er(df)
        st.write("Generated ER Diagram (Graphviz):")
        st.graphviz_chart(dot)

# Running Streamlit (This should be run in the terminal, not in the notebook)
if __name__ == "__main__":
    main()
