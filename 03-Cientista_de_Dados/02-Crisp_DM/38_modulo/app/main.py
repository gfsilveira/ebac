import streamlit as st
import pandas as pd
from joblib import load

from src.pepilineProprio import PepilineProprio
from src.modelos import Modelos

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

        # st.write(os.listdir())
        link = "03-Cientista_de_Dados/02-Crisp_DM/38_modulo/app/data/reg_redc_summary_frame"
        reg_redc_summary_frame = load(link)
        enviar_transform = (
            df,
            reg_redc_summary_frame
        )
        df_final = rotina_pipe_import.transform(enviar_transform)
        st.dataframe(df_final.head())

        modelos = Modelos(df_final=df_final)
        reg = modelos.regrecao_linear()
        st.write(reg.summary())

        reg_linear = modelos.load_reg_linear()
        st.write(reg_linear.summary())

        df_final['renda_log_pred'] = reg_linear.predict(df_final)
        st.dataframe(df_final.head())

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    inicia()
