import streamlit as st
import pandas as pd

def inicia() -> None:
    # Entrada
    st.markdown("Entrada")

    with st.sidebar:
        # Upload de arquivo
        uploaded_file = st.file_uploader("Choose a CSV file")
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.dataframe(df.head())

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    inicia()
