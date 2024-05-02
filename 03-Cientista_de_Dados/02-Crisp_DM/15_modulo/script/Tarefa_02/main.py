import streamlit as st
import pandas as pd

from src.gera_grafico import gera_graficos

def __edita_data(data) -> str:
    data = str(data.strftime('%d/%m/%Y'))
    return data


def inicializa() -> None:
    '''
        Função de inicialização do app.
    '''
    st.set_page_config(
        page_title="SINASC Rondônia",
        page_icon='https://upload.wikimedia.org/wikipedia/commons/e/ea/Flag_map_of_Rondonia.png',
        layout="wide"
    )
    st.title("Análise SINASC")

    
    try:

        link = "https://raw.githubusercontent.com/gfsilveira/ebac/main/"
        link += "03-Cientista_de_Dados/02-Crisp_DM/15_modulo/script/"
        link += "Tarefa_02/data/SINASC_RO_2019.csv"

        # Lendo arquivo com os dados
        df = pd.read_csv(link)

        df.DTNASC = pd.to_datetime(df.DTNASC)

        min_date = df.DTNASC.min()
        max_date = df.DTNASC.max()

        data_incial = st.sidebar.date_input(
                                            "Data Inicial",
                                            value=min_date,
                                            min_value=min_date,
                                            max_value=max_date
        )

        data_final = st.sidebar.date_input(
                                            "Data Final",
                                            value=max_date,
                                            min_value=min_date,
                                            max_value=max_date
        )

        filtro = (df.DTNASC <= pd.to_datetime(data_final)) & (df.DTNASC >= pd.to_datetime(data_incial))
        df_copy = df[filtro].copy()

        st.sidebar.write(f"# Min: {__edita_data(df_copy.DTNASC.min())}")
        st.sidebar.write(f"# Max: {__edita_data(df_copy.DTNASC.max())}")

        gera_graficos(df_copy)

    except:
        st.write(f"Dados não encontraddos.")
        return None


if __name__ == "__main__":
    # Rodando a função de inicialização do app
    inicializa()