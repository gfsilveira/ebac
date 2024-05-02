import streamlit as st
import pandas as pd
import numpy as np

def quatorze_app() -> None:
    st.title("Gráfico de Pontos")
    
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    st.scatter_chart(chart_data)
    st.markdown("---")
    return None