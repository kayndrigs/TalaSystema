from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)
uploaded_file = st.file_uploader("your csv data")

# Add Title
st.title("Use Pygwalker In Streamlit")

# You should cache your pygwalker renderer, if you don't want your memory to explode
@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    df = pd.read_csv(uploaded_file,encoding='latin-1')
    # If you want to use feature of saving chart config, set `spec_io_mode="rw"`
    return StreamlitRenderer(df, spec="./gw_config.json", spec_io_mode="rw", kernel_computation=True)

if uploaded_file is not None:
    renderer = get_pyg_renderer()

    renderer.viewer()