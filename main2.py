import gradio as gr
import pandas as pd
from pygwalker.api.gradio import PYGWALKER_ROUTE, get_html_on_gradio
 
with gr.Blocks() as demo:
    df = pd.read_csv("kaggle_income.csv", encoding='latin-1')
    gr.Markdown("# Data Visualization with PyGWalker")
 
    with gr.Tab("PyGWalker Explorer"):
        pyg_html = get_html_on_gradio(df, spec="./gw_config.json")
        gr.HTML(pyg_html)
 
    with gr.Tab("Data Summary"):
        gr.DataFrame(df.describe())
 
    with gr.Tab("Raw Data"):
        gr.DataFrame(df)
 
app = demo.launch(share=True,app_kwargs={"routes": [PYGWALKER_ROUTE]})