import streamlit as st
import pandas as pd
import numpy as np

from src.st_functions import *


def __chamada_df() -> pd.DataFrame:
    # Carregando base de dados
    link = "https://raw.githubusercontent.com/gfsilveira/ebac/main/"
    link += "03-Cientista_de_Dados/02-Crisp_DM/16_modulo/"
    link += "projeto_2_resposta/data/previsao_de_renda.csv"
    df = estruturacao_df(link=link)

    return df

def dados_brutos() -> None:
    '''
    link_relatorio = "https://raw.githubusercontent.com/gfsilveira/ebac/main/"
    link_relatorio += "03-Cientista_de_Dados/02-Crisp_DM/16_modulo/"
    link_relatorio += "projeto_2_resposta/output/renda_analisys.html"

    link_relatorio_html = f"<a href='{link_relatorio}' target='_blank' >Relatório</a>"

    st.markdown(link_relatorio_html, unsafe_allow_html=True)
    '''

    st.markdown("## Dados Brutos")
    df = __chamada_df()
    st.table(df.head())

    col = st.columns([2,2,1], gap='medium')
    with col[0]:
        df_qualitativas = df.select_dtypes(['category','object','bool']).copy()
        df_quantitativas = df.select_dtypes(['float64','int64']).copy()

        st.markdown("## Variáveis Quantitativas")
        st.table(df_quantitativas.describe())
    
    with col[1]:

        st.markdown("## Variáveis Qualitativas")
        st.table(df_qualitativas.describe())
    
    with col[2]:

        st.markdown("## Classes")
        st.table(df.dtypes)
    
    st.markdown("---")
    
    return None

def univariada() -> None:
    df = __chamada_df()
    df_qualitativas = df.select_dtypes(['category','object','bool']).copy()
    df_quantitativas = df.select_dtypes(['float64','int64']).copy()

    coluna = list(df_qualitativas.columns)
    coluna += list(df_quantitativas.columns)

    variable_names = {}
    number = 0
    for c in coluna:
        name = c.title().replace("_", " ")
        variable_names[name] = number
        number += 1

    col = st.columns([0.5,6,0.5])
    with col[1]:
        st.markdown("## Análise Univariada")
        nome_variavel = st.selectbox("Escolha uma Variável", variable_names.keys())
        c = int(variable_names[nome_variavel])

        if c < 7:
            grafico_barras_stack(df=df, coluna=coluna[c])
            grafico_barras(df=df, coluna=coluna[c])
            grafico_pontos(df=df, coluna=coluna[c])
        else:
            grafico_boxplot(df=df, coluna=coluna[c])
            grafico_serie_temp(df=df, coluna=coluna[c])

    st.markdown("---")
    return None

def bivariada() -> None:
    df = __chamada_df()
    df_quantitativas = df.select_dtypes(['float64','int64']).copy()
    df_corr_quantitativas = df_quantitativas.corr()
    
    col = st.columns([1,3,3,1])
    with col[1]:
        st.markdown("## Análise Bivariada")
        grafico_correlacao(df_corr_quantitativas=df_corr_quantitativas)

    with col[2]:
        coluna = df_quantitativas.columns.values
        variables_names = {}
        num = 0
        for c in coluna:
            name = c.title().replace("_", " ")
            variables_names[name] = num
            num += 1
        
        col_1 = st.columns([1,1])

        with col_1[0]:
            nome_prim = st.selectbox("Primeira Variável:", variables_names.keys())
            prim = int(variables_names[nome_prim])
            del variables_names[coluna[prim].title().replace("_", " ")]

        with col_1[1]:
            nome_segun = st.selectbox("Segunda Variável:", variables_names.keys())
            segun = int(variables_names[nome_segun])


        grafico_regressao(df=df_quantitativas, prim=coluna[prim], segun=coluna[segun])
    
    col = st.columns([1,6,1])
    with col[1]:
        df_qualitativas = df.select_dtypes(['category','object','bool']).copy()
        grafico_pontos_intervalo_bivariada(df=df, df_qualitativas=df_qualitativas)
    st.markdown("---")
    return None


def modelos() -> None:
    modelos_reg_explicado = {
            "regressao_benchmarks": "Modelo de regressão com todas as variáveis.",
            "regressao_forward": "Modelo onde o valor de p-value das variáveis para beta = 0 é menor que o limite de 0,01",
            "regressao_lasso": "Modelo com regularização LASSO",
            "regressao_ridge": "Modelo com regularização Ridge",
            "regressao_stepwise": "Regressão usando a técnica de seleção de modelos por stepwise.",
    }

    modelos_reg = [
            "regressao_benchmarks",
            "regressao_forward",
            "regressao_lasso",
            "regressao_ridge",
            "regressao_stepwise",
    ]
    col_2 = st.columns([2,2,2])
    with col_2[0]:
        st.markdown("## Análise dos Modelos")
        nome_modelo = st.selectbox("Selecione um modelo", modelos_reg)
        st.markdown(f"### {nome_modelo.replace('ssao_','ssão ').title()}")
        st.write(modelos_reg_explicado[nome_modelo])
    with col_2[2]:
        st.write(compara_modelos(modelos_reg=modelos_reg))

    col = st.columns([3,2])
    with col[0]:
    
        regressoes = busca_regressoes(modelos_reg=modelos_reg)

        st.write(regressoes[nome_modelo].summary())
    
    with col[1]:
        grafico_predito(regressao=regressoes[nome_modelo], nome_modelo=nome_modelo)
        
    
    st.markdown("---")
    return None