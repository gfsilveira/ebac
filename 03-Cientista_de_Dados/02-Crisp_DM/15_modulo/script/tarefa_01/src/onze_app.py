import streamlit as st
import pandas as pd
import numpy as np

def onze_app() -> None:
    st.title("Gráfico de Área")
    
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    st.area_chart(chart_data)
    st.markdown("---")
    return None