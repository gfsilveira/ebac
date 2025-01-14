import streamlit as st
import pandas as pd

def inicia() -> None:
    st.markdown("Entrada")
    uploaded_file = st.file_uploader("Choose a CSV file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())

if __name__ == "__main__":
    inicia()
