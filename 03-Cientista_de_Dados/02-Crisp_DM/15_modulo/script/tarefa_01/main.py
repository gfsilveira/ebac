import streamlit as st

from src.primeiro_app import primeiro_app
from src.segundo_app import segundo_app
from src.terceiro_app import terceiro_app
from src.quarto_app import quarto_app
from src.quinto_app import quinto_app
from src.sexto_app import sexto_app
from src.setimo_app import setimo_app
from src.oitavo_app import oitavo_app
from src.nono_app import nono_app
from src.dez_app import dez_app
from src.onze_app import onze_app
from src.doze_app import doze_app
from src.treze_app import treze_app
from src.quatorze_app import quatorze_app
from src.quinze_app import quinze_app
from src.deseseis_app import deseseis_app
from src.dessesete_app import dessesete_app
from src.dezoito_app import dezoito_app
from src.dezenove_app import dezenove_app
from src.vinte_app import vinte_app


def inicia_app() -> None:
    st.set_page_config(
        page_title="EBAC - Tarefa 01",
        layout="wide"
    )

    page_names_to_funcs = {
        "---": intro,
        "Primeiro Código": primeiro_app,
        "Segundo Código": segundo_app,
        "Terceiro Código": terceiro_app,
        "Quarto Código": quarto_app,
        "Quinto Código": quinto_app,
        "Sexto Código": sexto_app,
        "Sétimo Código": setimo_app,
        "Oitavo Código": oitavo_app,
        "Nono Código": nono_app,
        "Décimo Código": dez_app,
        "Décimo Primeiro Código": onze_app,
        "Décimo Segundo Código": doze_app,
        "Décimo Terceiro Código": treze_app,
        "Décimo Quarto Código": quatorze_app,
        "Décimo Quinto Código": quinze_app,
        "Décimo Sexto Código": deseseis_app,
        "Décimo Sétimo Código": dessesete_app,
        "Décimo Oitavo Código": dezoito_app,
        "Décimo Nono Código": dezenove_app,
        "Vigésimo Código": vinte_app,
    }

    nome_app = st.sidebar.selectbox("Escolha um Código", page_names_to_funcs.keys())
    page_names_to_funcs[nome_app]()


def intro() -> None:
    st.title("Selecione um Código na barra laterial")

    st.markdown("---")
    return None

if __name__ == "__main__":
    inicia_app()