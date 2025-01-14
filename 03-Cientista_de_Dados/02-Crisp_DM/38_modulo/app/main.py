import streamlit as st
import pandas as pd

from src.pepilineProprio import PepilineProprio


def inicia() -> None:
    # Entrada
    st.markdown("Entrada")

    with st.sidebar:
        # Upload de arquivo
        entrada_cvs = False
        uploaded_file = st.file_uploader("Choose a CSV file")
        if uploaded_file is not None:
            entrada_cvs = True

    if entrada_cvs:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())

    pipe_import = PepilineProprio()
    rotina_pipe_import = pipe_import.inicia_rotina()
    st.write(rotina_pipe_import.steps)

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    inicia()
