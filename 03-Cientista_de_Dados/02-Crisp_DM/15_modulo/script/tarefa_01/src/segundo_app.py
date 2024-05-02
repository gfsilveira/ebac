import streamlit as st
import pandas as pd
import numpy as np

def segundo_app() -> None:
    st.title("Mostra uma DataFrame, com valores máximos destacados")
    
    
    df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

    st.dataframe(df.style.highlight_max(axis=0))
    st.markdown("---")
    return None