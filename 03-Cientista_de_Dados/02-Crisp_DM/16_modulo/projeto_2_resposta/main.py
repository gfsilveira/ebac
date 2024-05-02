import streamlit as st

from src.pages import dados_brutos, univariada, bivariada, modelos

def bone() -> None:
    st.set_page_config(
        page_title="EBAC - Análise Renda",
        layout="wide"
    )
    st.markdown("""
        <style>
               .block-container {
                    padding-top: 1.4rem;
                    padding-bottom: 0rem;
                    padding-left: 2rem;
                    padding-right: 2rem;
                }
        </style>
        """, unsafe_allow_html=True)
    
    col = st.columns([3,1])
    with col[0]:
        st.markdown("# Análise do banco de dados de renda".title())
    
    with col[1]:
        page_names_to_funcs = {
            "Dados Brutos": dados_brutos,
            "Univariada": univariada,
            "Bivariada": bivariada,
            "Modelos": modelos,
        }
        nome_app = st.selectbox("Escolha uma Visualização", page_names_to_funcs.keys())
    page_names_to_funcs[nome_app]()

if __name__ == "__main__":
    bone()
