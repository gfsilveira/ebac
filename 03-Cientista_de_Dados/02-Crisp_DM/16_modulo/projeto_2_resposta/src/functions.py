import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def estruturacao_df(link: str) -> pd.DataFrame:
      df = pd.read_csv(link)
      df = (
            df.drop(["Unnamed: 0","id_cliente"], axis='columns')
            .dropna()
            .assign(data_ref=pd.to_datetime(df['data_ref']))
            .drop_duplicates()
            .assign(renda_media_movel=df['renda'].rolling(len(df) // 100).mean())
            .fillna(np.median(df['renda']))
            .query("tipo_residencia == 'Casa' & estado_civil == 'Casado'")
            .drop(labels=['tipo_residencia', 'estado_civil'], axis="columns")
            .astype({'qtd_filhos':"category",'qt_pessoas_residencia':"category"})
      )
      return df


def __insere_mes(df: pd.DataFrame) -> pd.DataFrame:
      '''
      Função insere a coluna mês na DataFrame.
      :param df (pd.DataFrame): DataFrame para ser modificada.
      '''
      x = "mes"
      df_select = df.copy()
      df_select[x] = df_select['data_ref'].dt.to_period("M")
      return df_select


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
plt.show()


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
      plt.show()

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
      return None

def grafico_pontos_intervalo(df: pd.DataFrame, coluna: str, eixos) -> None:
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
            ax=eixos
      )
      ax.set(
            title=coluna.title(),
            xlabel=coluna.title(),
            ylabel="Renda",
      )
      eixos.tick_params(rotation=90, axis="x")
      
      plt.subplots_adjust(wspace=0.3, hspace=0.5)
      return None