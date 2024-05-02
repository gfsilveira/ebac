import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from joblib import load
import urllib.request
from sklearn.metrics import r2_score
from scipy.stats import pearsonr


@st.cache_data
def estruturacao_df(link: str) -> pd.DataFrame:
      df = pd.read_csv(link)
      df = (
            df.drop(["Unnamed: 0","id_cliente"], axis='columns')
            .dropna()
            .assign(data_ref=pd.to_datetime(df['data_ref']))
            .drop_duplicates()
            .assign(renda_media_movel=df['renda'].rolling(len(df) // 100).mean())
            .fillna(np.median(df['renda']))
            .assign(tempo_emprego_media_movel=df['tempo_emprego'])
            # .assign(tempo_emprego_media_movel=df['tempo_emprego'].rolling(len(df) // 100).mean())
            # .fillna(np.median(df['tempo_emprego']))
            .query("tipo_residencia == 'Casa' & estado_civil == 'Casado'")
            .drop(labels=['tipo_residencia', 'estado_civil'], axis="columns")
            .astype({'qtd_filhos':"category",'qt_pessoas_residencia':"category"})
      )
      return df


@st.cache_data
def __insere_mes(df: pd.DataFrame) -> pd.DataFrame:
      '''
      Função insere a coluna mês na DataFrame.
      :param df (pd.DataFrame): DataFrame para ser modificada.
      '''
      x = "mes"
      df_select = df.copy()
      df_select[x] = df_select['data_ref'].dt.to_period("M")
      return df_select


@st.cache_data
def grafico_barras_stack(df: pd.DataFrame, coluna: str) -> None:
      '''
      Função de plot de gráfico de barras empilhado com a frequência 
      de instâncias para a variável selecionada ao longo do tempo.
      :param df (pd.DataFrame): DataFrame para ser modificada.
      :param coluna (str): Coluna de interesse.
      '''
      x = "mes"
      df_select = __insere_mes(df)

      tab = pd.crosstab(df_select[x] ,df_select[coluna])
      tab = tab.div(tab.sum(axis=1), axis=0)

      title = f"Renda média ao longo dos meses: {coluna.replace('_',' ').title()}"

      tab.plot.bar(
            figsize=(18,5),
            title=title,
            xlabel=x.title(),
            ylabel="Frequência "+coluna.title(),
            stacked=True
      )
      plt.legend(bbox_to_anchor=(1.02, 1.05), loc=2, borderaxespad=0.)
      st.pyplot(fig=plt)
      return None


@st.cache_data
def grafico_pontos(df: pd.DataFrame, coluna: str) -> None:
      '''
      Função de plot de gráfico de pontos, com interfavo de confiança de 95%,
      da renda em instância selecionada ao longo do tempo.
      :param df (pd.DataFrame): DataFrame para ser modificada.
      :param coluna (str): Coluna de interesse.
      '''
      x = "mes"
      y = "renda"
      df_select = __insere_mes(df)

      title = f"Renda média ao longo dos meses para {coluna.replace('_',' ').title()}"

      plt.figure(figsize=(18,5))

      f = sns.pointplot(
            x=x,
            y=y,
            hue=coluna,
            errorbar=('ci', 95),
            data=df_select,
      )
      f.set(
            title=title,
            xlabel=x.title(),
            ylabel=y.title()
      )

      plt.legend(bbox_to_anchor=(1.02, 1.05), loc=2, borderaxespad=0.)
      st.pyplot(fig=plt)
      return None


@st.cache_data
def grafico_barras(df: pd.DataFrame, coluna: str) -> None:
      '''
      Função de plot de gráfico de barras da renda em instância selecionada ao
      longo do tempo.
      :param df (pd.DataFrame): DataFrame para ser modificada.
      :param coluna (str): Coluna de interesse.
      '''
      x = "mes"
      y = "renda"
      df_select = __insere_mes(df)

      plt.figure(figsize=(18,5))
      f = sns.barplot(
            x=x,
            y=y,
            hue=coluna,
            data=df_select
      )
      f.set(
            xlabel=x.replace("_"," ").title(),
            ylabel=y.replace("_"," ").title()+" média"
      )
      plt.legend(bbox_to_anchor=(1.02, 1.05), loc=2, borderaxespad=0.)
      st.pyplot(fig=plt)
      return None


@st.cache_data
def grafico_boxplot(df: pd.DataFrame, coluna: str) -> None:
      '''
      Função de plot de gráfico boxplot.
      :param df (pd.DataFrame): DataFrame para ser modificada.
      :param coluna (str): Coluna de interesse.
      '''
      title = f"Distribuição para {coluna.replace('_',' ').title()}"
      plt.figure(figsize=(15,5))
      f = sns.boxplot(
            x=coluna,
            data=df
      )
      f.set(
            title=title,
            xlabel=coluna.title(),
      )
      st.pyplot(fig=plt)
      return None


@st.cache_data
def grafico_serie_temp(df: pd.DataFrame, coluna: str = "idade") -> None:
      '''
      Função de plot de gráfico boxplot.
      :param df (pd.DataFrame): DataFrame para ser modificada.
      :param coluna (str): Coluna de interesse.
      '''
      title = f"Distribuição para {coluna.replace('_',' ').title()}"
      plt.figure(figsize=(15,5))
      f = sns.lineplot(
            x="data_ref",
            y=coluna,
            data=df
      )
      f.set(
            title=title,
            xlabel="Data",
            ylabel=coluna.title(),
      )
      st.pyplot(fig=plt)
      return None


@st.cache_data
def grafico_correlacao(df_corr_quantitativas: pd.DataFrame) -> None:
      # Plotando as correlações
      cmap = sns.diverging_palette(
            h_neg=125,
            h_pos=350,
            as_cmap=True,
            sep=60,
            center="light"
      )

      g = sns.clustermap(
            data=df_corr_quantitativas,
            figsize=(7,7),
            center=0,
            cmap=cmap,
            vmin=-1,
            vmax=1,
            # mask=mask
      )
      g.ax_row_dendrogram.set_visible(False)
      g.fig.suptitle("Correlação entre as variáveis quantitativas", y=1.05, size=10)

      st.pyplot(fig=plt)
      return None


@st.cache_data
def grafico_regressao(
            df: pd.DataFrame,
            prim: str = "renda",
            segun: str = "tempo_emprego"
      ) -> None:
      # Plotando a relação entre a variável dependente e a com maior correlação
      sns.jointplot(
            x=prim,
            y=segun,
            kind="reg",
            data=df,
      )
      title_prim = prim.title().replace("_", " ")
      title_segun = segun.title().replace("_", " ")
      title = f"Correlação {title_prim} e {title_segun}"
      plt.suptitle(title, y=1.05, size=16)
      
      st.pyplot(fig=plt)
      return None


@st.cache_data
def grafico_pontos_intervalo(df: pd.DataFrame, coluna: str, _eixos) -> None:
      '''
      Função de plot de gráfico dispersão.
      :param df (pd.DataFrame): DataFrame para ser modificada.
      :param coluna (str): Coluna de interesse.
      '''
      ax = sns.pointplot(
            x=coluna,
            y="renda",
            data=df,
            dodge=True,
            errorbar=('ci', 95),
            ax=_eixos
      )
      ax.set(
            title=coluna.title().replace("_"," "),
            # xlabel=coluna.title().replace("_"," "),
            ylabel="Renda",
      )
      _eixos.tick_params(rotation=90, axis="x")
      
      plt.subplots_adjust(wspace=0.3, hspace=0.5)
      return None


@st.cache_data
def grafico_pontos_intervalo_bivariada(
      df: pd.DataFrame, 
      df_qualitativas: pd.DataFrame, 
      ) -> None:
      # Plot das variáveis qualitativas posse de imóvel e veículo.
      figura, eixos = plt.subplots(3,3, figsize=(15,15))
      figura.delaxes(eixos[2,1])
      figura.delaxes(eixos[2,2])

      plt.suptitle('Variáveis Qualitativas em relação à Renda', size=16)

      c = 0
      for k in [0,1,2]:
            for v in [0,1,2]:
                  coluna = df_qualitativas.columns[c]
                  grafico_pontos_intervalo(df=df, coluna=coluna, _eixos=eixos[k,v])
                  c += 1
                  if k == 2 and v == 0:
                        break

      st.pyplot(fig=plt)
      return None

@st.cache_data
def busca_regressoes(modelos_reg: list) -> dict:
    link = "https://github.com/gfsilveira/ebac/raw/main/"
    link += "03-Cientista_de_Dados/02-Crisp_DM/16_modulo/"
    link += "projeto_2_resposta/output/modelos/"

    regressoes = {modelo: load(urllib.request.urlopen(link+modelo)) for modelo in modelos_reg}

    return regressoes


@st.cache_data
def compara_modelos(modelos_reg: list) -> dict:
      regressoes = busca_regressoes(modelos_reg=modelos_reg)
      # Organizando as métricas dos modelos obtidos
      modelos = "Benchmarks Ridge LASSO Forward Stepwise".split(" ")
      df_metricas = pd.DataFrame(
            data={
                  "Modelo": modelos,
                  "R²": [
                        regressoes["regressao_benchmarks"].rsquared,
                        regressoes["regressao_ridge"].rsquared,
                        regressoes["regressao_lasso"].rsquared,
                        regressoes["regressao_forward"].rsquared,
                        regressoes["regressao_stepwise"].rsquared
                  ],
                  "R² adj": [
                        regressoes["regressao_benchmarks"].rsquared_adj,
                        regressoes["regressao_ridge"].rsquared_adj,
                        regressoes["regressao_lasso"].rsquared_adj,
                        regressoes["regressao_forward"].rsquared_adj,
                        regressoes["regressao_stepwise"].rsquared_adj
                  ],
                  "AIC": [
                        regressoes["regressao_benchmarks"].aic,
                        regressoes["regressao_ridge"].aic,
                        regressoes["regressao_lasso"].aic,
                        regressoes["regressao_forward"].aic,
                        regressoes["regressao_stepwise"].aic
                  ],
                  "N vari": [
                        len(regressoes["regressao_benchmarks"].pvalues),
                        len(regressoes["regressao_ridge"].pvalues),
                        len(regressoes["regressao_lasso"].pvalues),
                        len(regressoes["regressao_forward"].pvalues),
                        len(regressoes["regressao_stepwise"].pvalues)
                  ],
                  "Média p-value": [
                        np.mean(regressoes["regressao_benchmarks"].pvalues),
                        np.mean(regressoes["regressao_ridge"].pvalues),
                        np.mean(regressoes["regressao_lasso"].pvalues),
                        np.mean(regressoes["regressao_forward"].pvalues),
                        np.mean(regressoes["regressao_stepwise"].pvalues)
                  ],
            }
      )
      return df_metricas


def grafico_predito(regressao, nome_modelo) -> None:
      
      link = "https://github.com/gfsilveira/ebac/raw/main/"
      link += "03-Cientista_de_Dados/02-Crisp_DM/16_modulo/"
      link += "projeto_2_resposta/data/"

      y_test = load(urllib.request.urlopen(link+"y_test"))
      y_test = y_test.values.reshape(1,-1)[0]
      
      # Analisando os resíduos
      x = y_test
      y = regressao.resid[:len(y_test)]
      sns.scatterplot(
            x=x,
            y=y,
      )

      plt.plot(x, [0]*len(x), '-r')

      plt.title(f"Resíduos do modelo de {nome_modelo.replace('ssao_','ssão ').title()}")
      plt.xlabel("Conta Líquida")
      plt.ylabel("Resíduos")
      
      st.pyplot(fig=plt)
      return None