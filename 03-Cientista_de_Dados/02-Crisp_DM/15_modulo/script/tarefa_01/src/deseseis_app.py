import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


def deseseis_app() -> None:
    st.title("Gráfico de Dispersão com coloração em escala")
    
    st.subheader("Define a custom colorscale")
    df = px.data.iris()
    fig = px.scatter(
        df,
        x="sepal_width",
        y="sepal_length",
        color="sepal_length",
        color_continuous_scale="reds",
    )

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    with tab2:
        st.plotly_chart(fig, theme=None, use_container_width=True)    
    st.markdown("---")
    return None