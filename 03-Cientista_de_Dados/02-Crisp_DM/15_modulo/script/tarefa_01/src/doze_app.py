import streamlit as st
import pandas as pd
import numpy as np

def doze_app() -> None:
    st.title("Gráfico de Barras empilhadas")
    
    chart_data = pd.DataFrame(
    {
        "col1": list(range(20)) * 3,
        "col2": np.random.randn(60),
        "col3": ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
    }
    )

    st.bar_chart(chart_data, x="col1", y="col2", color="col3")
    st.markdown("---")
    return None