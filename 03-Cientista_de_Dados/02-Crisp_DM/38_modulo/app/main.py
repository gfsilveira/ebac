import streamlit as st
import pandas as pd
from joblib import load
from pycaret.classification import predict_model
from sklearn.metrics import accuracy_score

from src.pepilineProprio import PepilineProprio
from src.modelos import Modelos

def inicia() -> None:
    with st.sidebar:
        # Upload de arquivo
        entrada_cvs = False
        uploaded_file = st.file_uploader("Choose a CSV file")
        if uploaded_file is not None:
            entrada_cvs = True

    if entrada_cvs:
        st.markdown("# Base incial")
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())

        st.markdown("# Transformações Pipeline")
        pipe_import = PepilineProprio()
        rotina_pipe_import = pipe_import.inicia_rotina()
        st.write(rotina_pipe_import.steps)

        # st.write(os.listdir())
        st.markdown("# PCA base incial")
        link = "03-Cientista_de_Dados/02-Crisp_DM/38_modulo/app/data/reg_redc_summary_frame"
        reg_redc_summary_frame = load(link)
        enviar_transform = (
            df,
            reg_redc_summary_frame
        )
        df_final = rotina_pipe_import.transform(enviar_transform)
        st.dataframe(df_final.head())

        st.markdown("# Modelo Regressão Pipeline")
        modelos = Modelos(df_final=df_final)
        reg_linear = modelos.load_reg_linear()
        st.write(reg_linear.summary())

        st.markdown("# Previsão Modelo Regressão Pipeline")
        df_final['renda_log_pred'] = reg_linear.predict(df_final)
        st.dataframe(df_final.iloc[:, -2:].head())

        st.markdown("# Modelo Classificação PyCaret")
        df['data_ref'] = pd.to_datetime(df['data_ref'])
        link = "03-Cientista_de_Dados/02-Crisp_DM/38_modulo/app/data/final_lightgbm_pycaret"
        final_lightgbm_pycaret = load(link)
        unseen_predictions = predict_model(final_lightgbm_pycaret, data=df)
        st.dataframe(unseen_predictions.iloc[:, -4:].head())

        st.markdown("# Acurácia Classificação PyCaret")
        score = accuracy_score(unseen_predictions.mau, unseen_predictions.prediction_label)
        st.write(f"Acurácia: {score*100:.2f}%")

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    inicia()
